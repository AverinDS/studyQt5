# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'termForm.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class UiTermForm(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.okBtn = QtWidgets.QPushButton(self.centralwidget)
        self.okBtn.setGeometry(QtCore.QRect(670, 550, 113, 32))
        self.okBtn.setObjectName("okBtn")
        self.termTable = QtWidgets.QTableWidget(self.centralwidget)
        self.termTable.setGeometry(QtCore.QRect(20, 10, 771, 531))
        self.termTable.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.termTable.setRowCount(0)
        self.termTable.setColumnCount(4)
        self.termTable.setObjectName("termTable")
        self.addRowBtn = QtWidgets.QPushButton(self.centralwidget)
        self.addRowBtn.setGeometry(QtCore.QRect(10, 550, 113, 32))
        self.addRowBtn.setObjectName("addRowBtn")
        self.deleteBtn = QtWidgets.QPushButton(self.centralwidget)
        self.deleteBtn.setGeometry(QtCore.QRect(120, 550, 113, 32))
        self.deleteBtn.setObjectName("deleteBtn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.okBtn.setText(_translate("MainWindow", "Ok"))
        self.addRowBtn.setText(_translate("MainWindow", "Add item"))
        self.deleteBtn.setText(_translate("MainWindow", "Delete item"))


