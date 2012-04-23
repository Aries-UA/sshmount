#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys

from PyQt4 import QtCore, QtGui
from connector.connector import Connector
from forms.listconnection import ListConnection as LC

########################################################################

def main():
	win = LC(None, kernel)
	win.show()
	sys.exit(app.exec_())
	exit(0)

if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	kernel = Connector()
	main()
