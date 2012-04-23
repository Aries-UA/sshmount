#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PyQt4 import QtGui

class MessageBox(object):
	""" Класс сообщений """

	response = None
	
	def __init__(self, message='', set_type='error'):
		""" Конструктор класса """
		if (set_type == 'error'):
			QtGui.QMessageBox.critical(None, '!!! Error !!!', QtGui.QApplication.translate(None, message, None, QtGui.QApplication.UnicodeUTF8), QtGui.QMessageBox.Cancel)
			self.response = 'cancel'
		elif (set_type == 'quest'):
			reply = QtGui.QMessageBox.question(None, 'Question', QtGui.QApplication.translate(None, message, None, QtGui.QApplication.UnicodeUTF8), QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
			if (reply == QtGui.QMessageBox.Yes):
				self.response = 'yes'
			elif (reply == QtGui.QMessageBox.No):
				self.response = 'no'
			else:
				self.response = 'none'
		elif (set_type == 'info'):
			QtGui.QMessageBox.information(None, 'Information', QtGui.QApplication.translate(None, message, None, QtGui.QApplication.UnicodeUTF8), QtGui.QMessageBox.Ok)
			self.response = 'ok'
