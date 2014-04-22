#!/usr/bin/env python

import sys, os, urllib2
import try_auto
from PyQt4 import QtGui, QtCore

class Auto_connection(QtGui.QWidget):
    def __init__(self):
        super(Auto_connection, self).__init__()
        self.initUI()

    def initUI(self):

        name = QtGui.QLabel('Name')
        passwd = QtGui.QLabel('Passwd')
        
        self.nameEdit = QtGui.QLineEdit(self)
        self.passwdEdit = QtGui.QLineEdit(self)
        self.passwdEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.button_submit = QtGui.QPushButton('submit', self)
        self.button_exit = QtGui.QPushButton('exit', self)

        grid = QtGui.QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(name, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)
        grid.addWidget(passwd, 2, 0)
        grid.addWidget(self.passwdEdit, 2, 1)


        grid.addWidget(self.button_submit, 3, 3)
        grid.addWidget(self.button_exit, 3, 4)
        self.setLayout(grid)
        self.connect(self.button_submit, QtCore.SIGNAL('clicked()'), self.submit)
        self.connect(self.button_exit, QtCore.SIGNAL('clicked()'), self.exit)
        self.setWindowTitle('Auto Uni\'s wireless connection')
        self.setGeometry(250, 250, 400, 180)
    def submit(self):
        au_name = self.nameEdit.text()
        au_passwd = self.passwdEdit.text()
        self._connect(au_name, au_passwd)

    def exit(self):
        self.close()

    def _connect(self, name, passwd):
        try_auto.connection(name, passwd)
        self.close()
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    auto = Auto_connection()
    auto.show()
    app.exec_()
