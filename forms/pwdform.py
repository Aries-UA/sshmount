#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import pexpect

from PyQt4 import QtCore, QtGui
from forms.basewin import BaseWin
from pwditem import Ui_MainWindow as UIMW

class PwdItem(BaseWin, UIMW):
	""" Окно создания строки соединения соединения """

	def __init__(self, nID = -1, kernel = None, parent = None):
		self.kernel = kernel
		self.nID = nID
		self.parent = parent
		###
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		###
		self.setSignals()
		###
		self.default_value()
		###
		self.centered()

	def setSignals(self):
		""" Установка всех сигналов """
		self.connect(self.butExit, QtCore.SIGNAL("clicked()"), self._actionExit)
		self.connect(self.butTerm, QtCore.SIGNAL("clicked()"), self._actionTerm)

	def default_value(self):
		if (self.nID >= 0):
			row = self.kernel.sshlist[self.nID]
			###
			if (row['type'] == "1"):
				self.lineSsh.setText("ssh " + row['login'] + "@" + row['host'] + " -p " + row['port'])
			elif (row['type'] == "2"):
				self.lineSsh.setText("ftp " + row['host'] + " " + row['port'])
			###
			self.lineLogin.setText(row['login'])
			self.linePwd.setText(row['passwd'])
			self.lineHost.setText(row['host'])
		else:
			self._actionExit()

	def closeEvent(self, event):
		del self.nID
		#del self.parent
		#del self.kernel

	def _actionExit(self):
		self.close()

	def _actionTerm(self):
		row = self.kernel.sshlist[self.nID]
		###
		if (row['type'] == "1"):
			arg = "".join(["ssh ", row['login'], "@", row['host'], " -p ", row['port'],])
			###
			clipboard = QtGui.QApplication.clipboard()
			clipboard.setText(row['passwd'], QtGui.QClipboard.Selection)
			#clipboard.setText(row['passwd'], QtGui.QClipboard.Clipboard)
		elif (row['type'] == "2"):
			arg = "".join(["ftp ", row['host'], ' ', row['port'],])
		###
		pid = os.spawnlp(os.P_NOWAIT, "terminator", "terminator", "-e", arg)
