# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'clustering.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(842, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.clasteringTable = QtWidgets.QTableWidget(self.centralwidget)
        self.clasteringTable.setGeometry(QtCore.QRect(15, 11, 681, 551))
        self.clasteringTable.setObjectName("clasteringTable")
        self.clasteringTable.setColumnCount(0)
        self.clasteringTable.setRowCount(0)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(700, 10, 120, 91))
        self.groupBox.setObjectName("groupBox")
        self.radioButtonKmeans = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonKmeans.setGeometry(QtCore.QRect(10, 20, 100, 20))
        self.radioButtonKmeans.setObjectName("radioButtonKmeans")
        self.radioButtonIerarch = QtWidgets.QRadioButton(self.groupBox)
        self.radioButtonIerarch.setGeometry(QtCore.QRect(10, 50, 100, 20))
        self.radioButtonIerarch.setObjectName("radioButtonIerarch")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.radioButtonKmeans.setText(_translate("MainWindow", "Kmeans"))
        self.radioButtonIerarch.setText(_translate("MainWindow", "Ierarh"))


