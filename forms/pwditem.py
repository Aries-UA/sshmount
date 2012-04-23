# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pwditem.ui'
#
# Created: Thu Jun 30 17:37:43 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(420, 173)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(420, 173))
        MainWindow.setMaximumSize(QtCore.QSize(420, 173))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/stock_connect.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(4, 0, 4, 0)
        self.gridLayout.setHorizontalSpacing(4)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineSsh = QtGui.QLineEdit(self.centralwidget)
        self.lineSsh.setObjectName(_fromUtf8("lineSsh"))
        self.gridLayout.addWidget(self.lineSsh, 0, 1, 1, 3)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineLogin = QtGui.QLineEdit(self.centralwidget)
        self.lineLogin.setObjectName(_fromUtf8("lineLogin"))
        self.gridLayout.addWidget(self.lineLogin, 1, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(185, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 3, 1, 1)
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.linePwd = QtGui.QLineEdit(self.centralwidget)
        self.linePwd.setObjectName(_fromUtf8("linePwd"))
        self.gridLayout.addWidget(self.linePwd, 2, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(138, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 3, 1, 1)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.lineHost = QtGui.QLineEdit(self.centralwidget)
        self.lineHost.setObjectName(_fromUtf8("lineHost"))
        self.gridLayout.addWidget(self.lineHost, 3, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(138, 24, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(450, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 2)
        self.butExit = QtGui.QPushButton(self.centralwidget)
        self.butExit.setMinimumSize(QtCore.QSize(75, 0))
        self.butExit.setMaximumSize(QtCore.QSize(75, 16777215))
        self.butExit.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/application-exit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butExit.setIcon(icon1)
        self.butExit.setObjectName(_fromUtf8("butExit"))
        self.gridLayout.addWidget(self.butExit, 5, 3, 1, 1)
        self.butTerm = QtGui.QPushButton(self.centralwidget)
        self.butTerm.setMaximumSize(QtCore.QSize(54, 16777215))
        self.butTerm.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/newPrefix/terminator.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.butTerm.setIcon(icon2)
        self.butTerm.setObjectName(_fromUtf8("butTerm"))
        self.gridLayout.addWidget(self.butTerm, 5, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineSsh, self.lineLogin)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Строка соединения SSH", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "ssh:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "login:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "password:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "host:", None, QtGui.QApplication.UnicodeUTF8))

import images_rc
