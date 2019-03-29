from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QMessageBox

from controllers.TableController import TableController
from windows.py.Ui_database_window import Ui_database_window


class TableView(QtWidgets.QMainWindow):
    table_controller = TableController()

    def __init__(self):
        super(TableView, self).__init__()
        self.ui = Ui_database_window()
        self.ui.setupUi(self)
        self.ui.updateButton.clicked.connect(self.update_table)
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.showGraphicButton.clicked.connect(self.show_graphic)

        self.update_table()
        # Every list contains filename, trend, season, rand component

    def update_table(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setSortingEnabled(False)
        self.ui.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Filename"))
        self.ui.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Trend"))
        self.ui.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Season"))
        self.ui.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Random component"))

        table_data = self.table_controller.get_table_data()
        self.ui.tableWidget.setRowCount(len(table_data))
        self.ui.tableWidget.setColumnCount(len(table_data[0]))
        for i in range(0, len(table_data)):
            for j in range(0, len(table_data[0])):
                cell_info = QTableWidgetItem(table_data[i][j])
                self.ui.tableWidget.setItem(i, j, cell_info)

        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.setSortingEnabled(True)

    def show_graphic(self):
        if len(self.ui.tableWidget.selectedItems()) > 0:
            self.table_controller.show_graphic(
                self.ui.tableWidget.selectedItems().__getitem__(0).text()
            )
        else:
            QMessageBox.warning(self, "Warning", "File not chosen")
