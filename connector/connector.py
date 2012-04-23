#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import pexpect

from commands import *
from forms.messagebox import MessageBox

class Connector(object):
	""" Класс ядра коннектора """

	sshlist = []
	home_dir = ""
	home_file = ""

	def __init__(self):
		""" Инициализаци объекта """
		self.home_dir = os.path.expanduser('~/') + '.sshconnector/'
		self.home_file = os.path.expanduser('~/') + '.sshconnector/sshlist'
		###
		self.valid_dir()
		self.valid_file()
		self.create_list()

	def valid_dir(self):
		""" Создание в домашней директории каталога .sshconnector"""
		if os.path.isdir(self.home_dir) == False:
			os.makedirs(self.home_dir)

	def valid_file(self):
		""" Создание файла списка удаленных хостов """
		if os.path.isfile(self.home_file) == False:
			sshlist = open(self.home_file, 'w')
			sshlist.close()

	def _s(self, row):
		""" Обрезка пробелов и переносов строки """
		row = row.strip("\n\t\r")
		return row.strip()

	def add_to_list(self, r0, r1, r2, r3, r4, r5, r6, r7):
		""" Добавление новой строки в массив """
		self.sshlist.append({'host':self._s(r0),
												 'port':self._s(r1),
												 'remdir':self._s(r2),
												 'homedir':self._s(r3),
												 'login':self._s(r4),
												 'passwd':self._s(r5),
												 'type':self._s(r6),
												 'is_conn':r7,
												 'row':len(self.sshlist)+1})

	def create_list(self):
		""" Заполняем список данными """
		self.sshlist = []
		mnt = self.get_sys_mount().split("\n")
		for f in open(self.home_file):
			row = f.split(" ")
			###
			try:
				row_type = row[6]
			except:
				row_type = "1"
			###
			isConn = self.isMounted(mnt, row[2], row[3], row[0], row_type)
			self.add_to_list(row[0], row[1], row[2], row[3], row[4], row[5], row_type, isConn)

	def get_sys_mount(self):
		return getoutput('mount')

	def isMounted(self, mnt, rem, home, host, row_type):
		ret = False
		row_type = row_type.strip()
		if (row_type == '1'):
			rem = ":" + rem
			for row in mnt:
				if (row.find("fuse.sshfs") >= 0):
					if (((row.find(rem) >= 0) or (row.find(rem[:-1]) >= 0)) and ((row.find(home) >= 0) or (row.find(home[:-1]) >= 0))):
						ret = True
						break
		elif (row_type == '2'):
			for row in mnt:
				if (row.find("curlftpfs#") >= 0):
					if (((row.find(host) >= 0) or (row.find(host[:-1]) >= 0)) and ((row.find(home) >= 0) or (row.find(home[:-1]) >= 0))):
						ret = True
						break
		return ret

	def save_list_tofile(self):
		""" Сохраняем данные в файл """
		if len(self.sshlist) > 0:
			sshlist = open(self.home_file, 'w')
			sshlist.truncate()
			for row in self.sshlist:
				print >> sshlist, row['host'], row['port'], row['remdir'], row['homedir'], row['login'], row['passwd'], row['type']
			sshlist.close()

	def mount_dir(self, nID=-1):
		""" Монтируем удаленный каталог в указаннную директорию """
		ok = False
		if nID >= 0:
			row = self.sshlist[nID]
			###
			self.mk_home_dir(row['homedir'], row['login'])
			###
			if (row["type"] == "1"):
				cmd = "".join(['sshfs ', row['login'], '@', row['host'], ':', row['remdir'], ' ', row['homedir'], row['login'], '/', ' -p ', row['port'],])
			elif (row["type"] == "2"):
				cmd = "".join(["curlftpfs ftp://", row['login'], ":", row['passwd'], "@", row['host'], ":", row['port'], " ", row['homedir'], row['login'], '/',])
			###
			self.sshfs = pexpect.spawn(cmd, env = {'SSH_ASKPASS':'/dev/null'})
			self.ssh_newkey = 'Are you sure you want to continue connecting'
			i = self.sshfs.expect([self.ssh_newkey, 'assword:', pexpect.EOF, pexpect.TIMEOUT])
			###
			if (i == 0):
				if (row["type"] == "1"):
					self.sshfs.sendline('yes')
					i = self.sshfs.expect([self.ssh_newkey, 'assword:', pexpect.EOF])
				elif (row["type"] == "2"):
					ok = True
			###
			if (i == 1):
				self.sshfs.sendline(row['passwd'])
				j = self.sshfs.expect([pexpect.EOF, 'assword:'])
				###
				if (j == 0):
					if (self.sshfs.before.strip() == ''):
						ok == True
						self.sshlist[nID]['is_conn'] = True
					else:
						MessageBox("Error found: %s" % self.sshfs.before)
				elif (j == 1):
					MessageBox("Password incorrect")
				elif (j == 0):
					print self.sshfs.before
			elif (i == 2):
				if (row["type"] == "1"):
					MessageBox("Error found: %s" % self.sshfs.before)
				elif (row["type"] == "2"):
					if (self.sshfs.before.strip() <> ''):
						MessageBox("Error found: %s" % self.sshfs.before)
					else:
						ok = True
						self.sshlist[nID]['is_conn'] = True
			elif (i == 3):
				if (row["type"] == "1"):
					MessageBox("Timeout: %s" % self.sshfs.before)
				elif (row["type"] == "2"):
					if (self.sshfs.before.strip() <> ''):
						MessageBox("Timeout: %s" % self.sshfs.before)
					else:
						ok = True
						self.sshlist[nID]['is_conn'] = True
			###
			self.sshfs.close(True)
		###
		return ok

	def umount_dir(self, nID=-1):
		""" Отмонтируем каталог """
		isOk = False
		if nID >= 0:
			try:
				txt = getoutput('fusermount -u -z ' + ''.join([self.sshlist[nID]['homedir'], self.sshlist[nID]['login'], '/']))
				if self._s(txt) <> '':
					MessageBox(txt)
				else:
					self.sshlist[nID]['is_conn'] = False
					isOk = True
			except:
				MessageBox(sys.exc_info()[1])
		return isOk

	def mk_home_dir(self, path, login):
		""" Создание директории для монтирования удалённого ресурса"""
		pth = ''.join([path, login, '/'])
		###
		if not os.path.isdir(pth):
			os.makedirs(pth)
