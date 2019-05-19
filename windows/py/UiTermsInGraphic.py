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
        TermsInGraphic.resize(1004, 600)
        self.centralwidget = QtWidgets.QWidget(TermsInGraphic)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(5, 1, 791, 591))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(800, 10, 181, 171))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 30, 165, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radioButton_number_soft_matrix = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_number_soft_matrix.setChecked(True)
        self.radioButton_number_soft_matrix.setObjectName("radioButton_number_soft_matrix")
        self.verticalLayout.addWidget(self.radioButton_number_soft_matrix)
        self.radioButton_numbe_soft_vector = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_numbe_soft_vector.setObjectName("radioButton_numbe_soft_vector")
        self.verticalLayout.addWidget(self.radioButton_numbe_soft_vector)
        self.radioButton_number_linguistic = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_number_linguistic.setObjectName("radioButton_number_linguistic")
        self.verticalLayout.addWidget(self.radioButton_number_linguistic)
        self.radioButton_number_soft_linguistic = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_number_soft_linguistic.setObjectName("radioButton_number_soft_linguistic")
        self.verticalLayout.addWidget(self.radioButton_number_soft_linguistic)
        self.radioButton_number_number = QtWidgets.QRadioButton(self.verticalLayoutWidget)
        self.radioButton_number_number.setObjectName("radioButton_number_number")
        self.verticalLayout.addWidget(self.radioButton_number_number)
        TermsInGraphic.setCentralWidget(self.centralwidget)

        self.retranslateUi(TermsInGraphic)
        QtCore.QMetaObject.connectSlotsByName(TermsInGraphic)

    def retranslateUi(self, TermsInGraphic):
        _translate = QtCore.QCoreApplication.translate
        TermsInGraphic.setWindowTitle(_translate("TermsInGraphic", "MainWindow"))
        self.groupBox.setTitle(_translate("TermsInGraphic", "Mode"))
        self.radioButton_number_soft_matrix.setText(_translate("TermsInGraphic", "NFXM"))
        self.radioButton_numbe_soft_vector.setText(_translate("TermsInGraphic", "NFXV"))
        self.radioButton_number_linguistic.setText(_translate("TermsInGraphic", "NLX"))
        self.radioButton_number_soft_linguistic.setText(_translate("TermsInGraphic", "NLFX"))
        self.radioButton_number_number.setText(_translate("TermsInGraphic", "NNX"))


