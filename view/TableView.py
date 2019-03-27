from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from controllers.TableController import TableController
from windows.py.Ui_database_window import Ui_database_window


class TableView(QtWidgets.QMainWindow):
    table_controller = TableController()

    def __init__(self):
        super(TableView, self).__init__()
        self.ui = Ui_database_window()
        self.ui.setupUi(self)
        self.ui.updateButton.clicked.connect(self.update_table)
        # Every list contains filename, trend, season, rand component

    def update_table(self):
        self.ui.tableWidget.clear()
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
