#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from forms.basewin import BaseWin
from edititem import Ui_MainWindow as UIMW
from forms.messagebox import MessageBox

class EditItem(BaseWin, UIMW):
	""" Окно редактирования соединения """

	is_conn = False
	
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
		self.connect(self.butSave, QtCore.SIGNAL("clicked()"), self._actionSave)
		self.connect(self.butExit, QtCore.SIGNAL("clicked()"), self._actionExit)
		self.connect(self.lineType, QtCore.SIGNAL("activated(QString)"), self._actionType)

	def default_value(self):
		""" Установка значений по умолчанию """
		data = []
		data.append({"id":"1", "name":"SSH"})
		data.append({"id":"2", "name":"FTP"})
		###
		if self.nID == -1:
			self.linePort.setText("22")
			for cmb in data:
				self.lineType.addItem(cmb["name"], cmb["id"])
			self.lineType.setCurrentIndex(0)
		elif self.nID >= 0:
			row = self.kernel.sshlist[self.nID]
			self.lineHost.setText(row['host'])
			self.linePort.setText(row['port'])
			self.lineRemDir.setText(row['remdir'])
			self.lineHomeDir.setText(row['homedir'])
			self.lineLogin.setText(row['login'])
			self.linePwd.setText(row['passwd'])
			self.is_conn = row['is_conn']
			###
			cur_id = 0
			itr = 0
			for cmb in data:
				self.lineType.addItem(cmb["name"], cmb["id"])
				if (cmb["id"] == row['type']):
					cur_id = itr
				itr = itr + 1
			###
			self.lineType.setCurrentIndex(cur_id)
			

	def _actionType(self, txt):
		""" Сигнал комбобокса """
		cur_id = self.lineType.itemData(self.lineType.currentIndex()).toString()
		if (self.nID == -1):
			if (cur_id == "1"):
				set_port = "22"
			elif (cur_id == "2"):
				set_port = "21"
			else:
				set_port = "22"
			###
			self.linePort.setText(set_port)
		elif (self.nID >= 0):
			MessageBox("Вы сменити тип соединения, проверте, верно ли указан порт", "info")

	def _actionExit(self):
		self.close()

	def closeEvent(self, event):
		del self.nID
		#del self.parent
		#del self.kernel

	def _actionSave(self):
		txt = "";
		###
		_host = str(self.lineHost.text())
		_port = str(self.linePort.text())
		_remdir = str(self.lineRemDir.text())
		_homedir = str(self.lineHomeDir.text())
		_login = str(self.lineLogin.text())
		_pwd = str(self.linePwd.text())
		_type = str(self.lineType.itemData(self.lineType.currentIndex()).toString())
		###
		if _host == '':
			txt = txt + "Не заполнено поле 'Хост'\n";
		if _port == '':
			txt = txt + "Не заполнено поле 'Порт'\n";
		if _remdir == '':
			txt = txt + "Не заполнено поле 'Удаленный каталог'\n";
		if _homedir == '':
			txt = txt + "Не заполнено поле 'Локальный каталог'\n";
		if _login == '':
			txt = txt + "Не заполнено поле 'Логин'\n";
		if _pwd == '':
			txt = txt + "Не заполнено поле 'Пароль'\n";
		###
		if txt != '':
			MessageBox(txt)
		else:
			if self.nID == -1:
				self.kernel.add_to_list(_host, _port, _remdir, _homedir, _login, _pwd, _type, self.is_conn)
			else:
				self.kernel.sshlist[self.nID]['host'] = _host
				self.kernel.sshlist[self.nID]['port'] = _port
				self.kernel.sshlist[self.nID]['remdir'] = _remdir
				self.kernel.sshlist[self.nID]['homedir'] = _homedir
				self.kernel.sshlist[self.nID]['login'] = _login
				self.kernel.sshlist[self.nID]['passwd'] = _pwd
				self.kernel.sshlist[self.nID]['is_conn'] = self.is_conn
				self.kernel.sshlist[self.nID]['type'] = _type
			###
			self.kernel.save_list_tofile()
			###
			self.parent.set_data_to_list()
			###
			self._actionExit()
