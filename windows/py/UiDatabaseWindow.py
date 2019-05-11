# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'database_window.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class UiDatabaseWindow(object):
    def setupUi(self, database_window):
        database_window.setObjectName("database_window")
        database_window.resize(780, 470)
        self.centralwidget = QtWidgets.QWidget(database_window)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 751, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(6)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.updateButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.updateButton.setAutoFillBackground(False)
        self.updateButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("resources/refresh_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.updateButton.setIcon(icon)
        self.updateButton.setCheckable(False)
        self.updateButton.setAutoRepeat(False)
        self.updateButton.setAutoExclusive(False)
        self.updateButton.setAutoDefault(False)
        self.updateButton.setDefault(False)
        self.updateButton.setFlat(False)
        self.updateButton.setObjectName("updateButton")
        self.verticalLayout_2.addWidget(self.updateButton)
        self.splitter = QtWidgets.QSplitter(self.verticalLayoutWidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.viewInFileButton = QtWidgets.QPushButton(self.splitter)
        self.viewInFileButton.setMinimumSize(QtCore.QSize(113, 32))
        self.viewInFileButton.setObjectName("viewInFileButton")
        self.showGraphicButton = QtWidgets.QPushButton(self.splitter)
        self.showGraphicButton.setObjectName("showGraphicButton")
        self.generateBtn = QtWidgets.QPushButton(self.splitter)
        self.generateBtn.setObjectName("generateBtn")
        self.setTermBtn = QtWidgets.QPushButton(self.splitter)
        self.setTermBtn.setObjectName("setTermBtn")
        self.btnShowTerms = QtWidgets.QPushButton(self.splitter)
        self.btnShowTerms.setObjectName("btnShowTerms")
        self.verticalLayout_2.addWidget(self.splitter)
        database_window.setCentralWidget(self.centralwidget)

        self.retranslateUi(database_window)
        QtCore.QMetaObject.connectSlotsByName(database_window)

    def retranslateUi(self, database_window):
        _translate = QtCore.QCoreApplication.translate
        database_window.setWindowTitle(_translate("database_window", "MainWindow"))
        self.tableWidget.setSortingEnabled(True)
        self.viewInFileButton.setText(_translate("database_window", "View in file"))
        self.showGraphicButton.setText(_translate("database_window", "Show Graphic"))
        self.generateBtn.setText(_translate("database_window", "Generate new data"))
        self.setTermBtn.setText(_translate("database_window", "Set terms"))
        self.btnShowTerms.setText(_translate("database_window", "Show Terms"))


