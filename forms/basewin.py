#!/usr/bin/env python
#-*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui

class BaseWin(QtGui.QMainWindow):

	def centered(self):
		rect = QtGui.QApplication.desktop().screenGeometry()
		###
		iXpos = rect.width()/2 - self.width()/2;
		iYpos = rect.height()/2 - self.height()/2;
		###
		self.move(iXpos,iYpos)

	def keyPressEvent(self, event):
		if (event.key() == QtCore.Qt.Key_Escape):
			self.close()
