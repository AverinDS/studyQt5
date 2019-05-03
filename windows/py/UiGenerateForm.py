# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generateForm.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class UiGenerateForm(object):
    def setupUi(self, GenerateWindow):
        GenerateWindow.setObjectName("GenerateWindow")
        GenerateWindow.resize(749, 234)
        GenerateWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(GenerateWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.removeAllDataCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.removeAllDataCheckBox.setGeometry(QtCore.QRect(50, 170, 141, 20))
        self.removeAllDataCheckBox.setChecked(True)
        self.removeAllDataCheckBox.setTristate(False)
        self.removeAllDataCheckBox.setObjectName("removeAllDataCheckBox")
        self.proceedButton = QtWidgets.QPushButton(self.centralwidget)
        self.proceedButton.setGeometry(QtCore.QRect(470, 170, 113, 32))
        self.proceedButton.setObjectName("proceedButton")
        self.cancelButton = QtWidgets.QPushButton(self.centralwidget)
        self.cancelButton.setGeometry(QtCore.QRect(600, 170, 113, 32))
        self.cancelButton.setObjectName("cancelButton")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(30, 10, 301, 141))
        self.groupBox.setObjectName("groupBox")
        self.seasonsCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.seasonsCheckBox.setGeometry(QtCore.QRect(10, 90, 87, 20))
        self.seasonsCheckBox.setObjectName("seasonsCheckBox")
        self.trendCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.trendCheckBox.setGeometry(QtCore.QRect(10, 30, 87, 20))
        self.trendCheckBox.setObjectName("trendCheckBox")
        self.randomCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.randomCheckBox.setGeometry(QtCore.QRect(10, 60, 87, 20))
        self.randomCheckBox.setObjectName("randomCheckBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(140, 30, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.textEditCountPosintsTS = QtWidgets.QTextEdit(self.groupBox)
        self.textEditCountPosintsTS.setGeometry(QtCore.QRect(140, 50, 121, 31))
        self.textEditCountPosintsTS.setObjectName("textEditCountPosintsTS")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(440, 10, 271, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.singleRadioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.singleRadioButton.setGeometry(QtCore.QRect(10, 30, 100, 20))
        self.singleRadioButton.setObjectName("singleRadioButton")
        self.groupRadioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.groupRadioButton.setGeometry(QtCore.QRect(10, 60, 131, 20))
        self.groupRadioButton.setObjectName("groupRadioButton")
        self.avoidRadioButton = QtWidgets.QRadioButton(self.groupBox_2)
        self.avoidRadioButton.setGeometry(QtCore.QRect(10, 90, 100, 20))
        self.avoidRadioButton.setChecked(True)
        self.avoidRadioButton.setObjectName("avoidRadioButton")
        self.textEditCountAnomaly = QtWidgets.QTextEdit(self.groupBox_2)
        self.textEditCountAnomaly.setGeometry(QtCore.QRect(160, 50, 101, 31))
        self.textEditCountAnomaly.setObjectName("textEditCountAnomaly")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(160, 30, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        GenerateWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GenerateWindow)
        QtCore.QMetaObject.connectSlotsByName(GenerateWindow)

    def retranslateUi(self, GenerateWindow):
        _translate = QtCore.QCoreApplication.translate
        GenerateWindow.setWindowTitle(_translate("GenerateWindow", "Generate timeseries"))
        self.removeAllDataCheckBox.setText(_translate("GenerateWindow", "Remove all data"))
        self.proceedButton.setText(_translate("GenerateWindow", "Proceed"))
        self.cancelButton.setText(_translate("GenerateWindow", "Cancel"))
        self.groupBox.setTitle(_translate("GenerateWindow", "Include components"))
        self.seasonsCheckBox.setText(_translate("GenerateWindow", "Seasons"))
        self.trendCheckBox.setText(_translate("GenerateWindow", "Trend"))
        self.randomCheckBox.setText(_translate("GenerateWindow", "Random"))
        self.label_2.setText(_translate("GenerateWindow", "Count of points for TS:"))
        self.textEditCountPosintsTS.setPlaceholderText(_translate("GenerateWindow", "800"))
        self.groupBox_2.setTitle(_translate("GenerateWindow", "Anomaly settings"))
        self.singleRadioButton.setText(_translate("GenerateWindow", "Single"))
        self.groupRadioButton.setText(_translate("GenerateWindow", "Group "))
        self.avoidRadioButton.setText(_translate("GenerateWindow", "Avoid"))
        self.textEditCountAnomaly.setPlaceholderText(_translate("GenerateWindow", "20"))
        self.label.setText(_translate("GenerateWindow", "Count of anomaly:"))


