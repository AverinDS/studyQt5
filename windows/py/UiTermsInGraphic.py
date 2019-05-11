# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TermsInGraphic.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class UiTermsInGraphic(object):
    def setupUi(self, TermsInGraphic):
        TermsInGraphic.setObjectName("TermsInGraphic")
        TermsInGraphic.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(TermsInGraphic)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 1, 791, 591))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        TermsInGraphic.setCentralWidget(self.centralwidget)

        self.retranslateUi(TermsInGraphic)
        QtCore.QMetaObject.connectSlotsByName(TermsInGraphic)

    def retranslateUi(self, TermsInGraphic):
        _translate = QtCore.QCoreApplication.translate
        TermsInGraphic.setWindowTitle(_translate("TermsInGraphic", "MainWindow"))


