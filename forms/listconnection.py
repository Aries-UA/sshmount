#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from treelist import Ui_MainWindow as UIMW
from forms.basewin import BaseWin
from forms.editform import EditItem
from forms.pwdform import PwdItem
from forms.messagebox import MessageBox

class ListConnection(BaseWin, UIMW):
	""" Окно списка соединений """

	def __init__(self, parent = None, kernel = None):
		""" Инициализация объекта, установка начальных значений """
		self.kernel = kernel
		self.parent = parent
		###
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		###
		self.treeList.setRootIsDecorated(False)
		###
		self.treeList.headerItem().setText(0, '')
		###
		self.treeList.setIconSize(QtCore.QSize(24, 24))
		###
		headSize = (28, 36, 240, 38, 170, 120, 100, 100,)
		for i in range(0, self.treeList.columnCount()):
			self.treeList.header().resizeSection(i, headSize[i])
			self.treeList.headerItem().setTextAlignment(i, QtCore.Qt.AlignHCenter)
		###
		self.setWindowModified(False)
		###
		self.setSignals()
		###
		self.set_data_to_list()
		###
		self.centered()

	def setSignals(self):
		""" Установка всех сигналов """
		self.connect(self.actionExit, QtCore.SIGNAL("triggered()"), self._actionExit)
		self.connect(self.actionEdit, QtCore.SIGNAL("triggered()"), self._actionEdit)
		self.connect(self.actionDel, QtCore.SIGNAL("triggered()"), self._actionDel)
		self.connect(self.actionAdd, QtCore.SIGNAL("triggered()"), self._actionAdd)
		self.connect(self.actionConnect, QtCore.SIGNAL("triggered()"), self._actionConnect)
		self.connect(self.actionRefresh, QtCore.SIGNAL("triggered()"), self._actionRefresh)
		self.connect(self.treeList, QtCore.SIGNAL("itemDoubleClicked(QTreeWidgetItem *, int)"), self._itemDoubleClicked)

	def _itemDoubleClicked(self, item, column):
		row = self.getRow(8) - 1
		pwdItem = PwdItem(row, self.kernel, self)
		pwdItem.show()

	def _actionConnect(self):
		""" Монтирование / Отмонтирование """
		if (self.treeList.selectedItems()):
			row = self.getRow(8) - 1
			###
			if self.kernel.sshlist[row]['is_conn'] == False:
				self.kernel.mount_dir(row)
			elif self.kernel.sshlist[row]['is_conn'] == True:
				self.kernel.umount_dir(row)
			###
			self._actionRefresh()
		else:
			MessageBox(u"Выберите строку соединения в списке", 'info')

	def _actionExit(self):
		""" Закрытие окна """
		self.close()

	def closeEvent(self, event):
		del self.parent
		del self.kernel

	def _actionAdd(self):
		""" Добавление нового элемента """
		editItem = EditItem(-1, self.kernel, self)
		editItem.show()

	def _actionEdit(self):
		""" Редактирование элемента """
		if (self.treeList.selectedItems()):
			row = self.getRow(8) - 1
			editItem = EditItem(row, self.kernel, self)
			editItem.show()
		else:
			MessageBox(u"Выберите строку соединения в списке", 'info')

	def _actionDel(self):
		""" Удаление соединения """
		if (self.treeList.selectedItems()):
			row = self.getRow(8) - 1
			resp = MessageBox(u"Вы точно хотите удалить - '" + unicode(self.getRow(1, False)) + u"'", "quest")
			if (resp.response == 'yes'):
				del self.kernel.sshlist[row]
				self.kernel.save_list_tofile()
				self.set_data_to_list()
		else:
			MessageBox(u"Выберите строку соединения в списке", 'info')

	def _actionRefresh(self):
		""" Обновление списка """
		self.kernel.create_list()
		self.set_data_to_list()

	def getRow(self, col, strInt=True):
		""" Значение ячейки """
		if (strInt == True):
			return int(self.treeList.currentItem().text(col))
		else:
			return self.treeList.currentItem().text(col)

	def set_data_to_list(self):
		""" Заполняем дерево данными """
		self.treeList.setSortingEnabled(False)
		self.treeList.clear()
		###
		font = QtGui.QFont()
		font.setPointSize(10)
		font.setBold(True)
		###
		icon_conn = QtGui.QIcon()
		icon_disconn = QtGui.QIcon()
		###
		icon_conn.addPixmap(QtGui.QPixmap(":/newPrefix/stock_connect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		icon_disconn.addPixmap(QtGui.QPixmap(":/newPrefix/stock_disconnect.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
		i = 0
		for row in self.kernel.sshlist:
			item = QtGui.QTreeWidgetItem(self.treeList)
			###
			if (row['type'] == "1"):
				row_type = "SSH"
			elif (row['type'] == "2"):
				row_type = "FTP"
			###
			self.treeList.topLevelItem(i).setText(0, '')
			self.treeList.topLevelItem(i).setText(1, row_type)
			self.treeList.topLevelItem(i).setText(2, row['host'])
			self.treeList.topLevelItem(i).setText(3, row['port'])
			self.treeList.topLevelItem(i).setText(4, row['remdir'])
			self.treeList.topLevelItem(i).setText(5, row['homedir'])
			self.treeList.topLevelItem(i).setText(6, row['login'])
			self.treeList.topLevelItem(i).setText(7, row['passwd'])
			self.treeList.topLevelItem(i).setText(8, str(row['row']))
			###
			item.setFont(2, font)
			###
			if row['is_conn'] == True:
				item.setIcon(0, icon_conn)
				for k in range(0, self.treeList.columnCount()):
					self.treeList.topLevelItem(i).setBackground(k, QtGui.QColor(142, 174, 255, 150))
			else:
				item.setIcon(0, icon_disconn)
			###
			i = i + 1
		self.treeList.sortByColumn(2, QtCore.Qt.AscendingOrder)
		self.treeList.setSortingEnabled(True)
