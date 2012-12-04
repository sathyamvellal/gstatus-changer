# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created: Tue Dec  4 22:35:37 2012
#      by: PyQt4 UI code generator 4.9.5
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
        MainWindow.resize(578, 288)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.start = QtGui.QPushButton(self.centralwidget)
        self.start.setGeometry(QtCore.QRect(10, 120, 201, 51))
        self.start.setCheckable(False)
        self.start.setChecked(False)
        self.start.setObjectName(_fromUtf8("start"))
        self.username = QtGui.QLineEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(90, 20, 121, 21))
        self.username.setObjectName(_fromUtf8("username"))
        self.password = QtGui.QLineEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(90, 50, 121, 21))
        self.password.setText(_fromUtf8(""))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.username_label = QtGui.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.username_label.setObjectName(_fromUtf8("username_label"))
        self.password_label = QtGui.QLabel(self.centralwidget)
        self.password_label.setGeometry(QtCore.QRect(10, 50, 81, 16))
        self.password_label.setObjectName(_fromUtf8("password_label"))
        self.interval_label = QtGui.QLabel(self.centralwidget)
        self.interval_label.setGeometry(QtCore.QRect(10, 80, 71, 16))
        self.interval_label.setObjectName(_fromUtf8("interval_label"))
        self.interval = QtGui.QLineEdit(self.centralwidget)
        self.interval.setGeometry(QtCore.QRect(90, 80, 121, 21))
        self.interval.setObjectName(_fromUtf8("interval"))
        self.statuses = QtGui.QTextEdit(self.centralwidget)
        self.statuses.setGeometry(QtCore.QRect(230, 20, 331, 221))
        self.statuses.setObjectName(_fromUtf8("statuses"))
        self.stop = QtGui.QPushButton(self.centralwidget)
        self.stop.setGeometry(QtCore.QRect(10, 190, 201, 51))
        self.stop.setCheckable(False)
        self.stop.setChecked(False)
        self.stop.setObjectName(_fromUtf8("stop"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 578, 19))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.start.setText(QtGui.QApplication.translate("MainWindow", "Start", None, QtGui.QApplication.UnicodeUTF8))
        self.username_label.setText(QtGui.QApplication.translate("MainWindow", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.password_label.setText(QtGui.QApplication.translate("MainWindow", "Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.interval_label.setText(QtGui.QApplication.translate("MainWindow", "Interval:", None, QtGui.QApplication.UnicodeUTF8))
        self.interval.setText(QtGui.QApplication.translate("MainWindow", "0", None, QtGui.QApplication.UnicodeUTF8))
        self.stop.setText(QtGui.QApplication.translate("MainWindow", "Stop", None, QtGui.QApplication.UnicodeUTF8))

