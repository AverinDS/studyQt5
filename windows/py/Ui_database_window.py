# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'database_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_database_window(object):
    def setupUi(self, database_window):
        database_window.setObjectName("database_window")
        database_window.resize(780, 470)
        database_window.setMinimumSize(QtCore.QSize(780, 470))
        database_window.setMaximumSize(QtCore.QSize(780, 470))
        self.centralwidget = QtWidgets.QWidget(database_window)
        self.centralwidget.setObjectName("centralwidget")
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(10, 380, 40, 40))
        self.updateButton.setMinimumSize(QtCore.QSize(40, 40))
        self.updateButton.setMaximumSize(QtCore.QSize(40, 40))
        self.updateButton.setAutoFillBackground(False)
        self.updateButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("././resources/refresh_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updateButton.setIcon(icon)
        self.updateButton.setCheckable(False)
        self.updateButton.setAutoRepeat(False)
        self.updateButton.setAutoExclusive(False)
        self.updateButton.setAutoDefault(False)
        self.updateButton.setDefault(False)
        self.updateButton.setFlat(False)
        self.updateButton.setObjectName("updateButton")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(60, 380, 40, 40))
        self.addButton.setMinimumSize(QtCore.QSize(40, 40))
        self.addButton.setMaximumSize(QtCore.QSize(40, 40))
        self.addButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("././resources/plus_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.addButton.setIcon(icon1)
        self.addButton.setObjectName("addButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(110, 380, 40, 40))
        self.deleteButton.setMinimumSize(QtCore.QSize(40, 40))
        self.deleteButton.setMaximumSize(QtCore.QSize(40, 40))
        self.deleteButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("././resources/minus_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.deleteButton.setIcon(icon2)
        self.deleteButton.setObjectName("deleteButton")
        self.showGraphicButton = QtWidgets.QPushButton(self.centralwidget)
        self.showGraphicButton.setGeometry(QtCore.QRect(640, 20, 113, 32))
        self.showGraphicButton.setMinimumSize(QtCore.QSize(113, 32))
        self.showGraphicButton.setMaximumSize(QtCore.QSize(113, 32))
        self.showGraphicButton.setObjectName("showGraphicButton")
        self.viewInFileButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewInFileButton.setGeometry(QtCore.QRect(640, 70, 113, 32))
        self.viewInFileButton.setMinimumSize(QtCore.QSize(113, 32))
        self.viewInFileButton.setMaximumSize(QtCore.QSize(113, 32))
        self.viewInFileButton.setObjectName("viewInFileButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 611, 361))
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        database_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(database_window)
        QtCore.QMetaObject.connectSlotsByName(database_window)

    def retranslateUi(self, database_window):
        _translate = QtCore.QCoreApplication.translate
        database_window.setWindowTitle(_translate("database_window", "MainWindow"))
        self.showGraphicButton.setText(_translate("database_window", "Show Graphic"))
        self.viewInFileButton.setText(_translate("database_window", "View in file"))


