from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from controllers.ClusteringController import ClusteringController
from helpers.ConstHolder import ClusteringConst
from windows.py.UiClusteringForm import UiClusteringForm


class ClasteringForm(QtWidgets.QMainWindow):
    clasteringController = ClusteringController()

    def __init__(self):
        super(ClasteringForm, self).__init__()
        self.ui = UiClusteringForm()
        self.ui.setupUi(self)
        self.ui.radioButtonKmeans.clicked.connect(self.kmeansClicked)
        self.ui.radioButtonIerarch.clicked.connect(self.ierhClicked)

    def kmeansClicked(self):
        self.updateTableData(self.clasteringController.getTableData(ClusteringConst.KMEANS))

    def ierhClicked(self):
        self.updateTableData(self.clasteringController.getTableData(ClusteringConst.IERH))

    def updateTableData(self, dataframe):
        self.ui.clasteringTable.clear()

        self.ui.clasteringTable.setColumnCount(len(dataframe.columns.values.tolist()))
        self.ui.clasteringTable.setRowCount(len(dataframe))
        for i in range(len(dataframe.columns.values.tolist())):
            self.ui.clasteringTable.setHorizontalHeaderItem(i, QTableWidgetItem(dataframe.columns.values.tolist()[i]))

        for i in range(0, len(dataframe.columns) - 1):
            for j in range(len(dataframe[i])):
                cell_info = QTableWidgetItem(str(dataframe[dataframe.columns[i]][j]))
                self.ui.clasteringTable.setItem(j, i, cell_info)

        for j in range(len(dataframe['cluster'])):
            cell_info = QTableWidgetItem(str(dataframe['cluster'][j]))
            self.ui.clasteringTable.setItem(j, 7, cell_info)

        self.ui.clasteringTable.resizeColumnsToContents()
        self.ui.clasteringTable.resizeRowsToContents()
        self.ui.clasteringTable.setSortingEnabled(True)
