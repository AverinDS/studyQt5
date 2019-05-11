from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from controllers.TermInGraphicController import TermInGraphicController
from windows.py.UiTermsInGraphic import UiTermsInGraphic


class TermInGraphicForm(QtWidgets.QMainWindow):
    termInGraphicController = TermInGraphicController()
    filename = ''

    def __init__(self, filename):
        super(TermInGraphicForm, self).__init__()
        self.filename = filename
        self.ui = UiTermsInGraphic()
        self.ui.setupUi(self)
        self.set_up_data_table()

    def set_up_data_table(self):
        rows_table, term_names = self.termInGraphicController.get_table_data(filename=self.filename)
        self.ui.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("X"))
        self.ui.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Y"))

        count_column = len(term_names) + 2  # plus x point and y point
        self.ui.tableWidget.setColumnCount(count_column)
        self.ui.tableWidget.setRowCount(len(rows_table))
        for i in range (0, len(term_names)):
            self.ui.tableWidget.setHorizontalHeaderItem(i + 2, QTableWidgetItem(str(term_names[i]))) # plus 2 because X and Y

        for i in range(0, len(rows_table)):
            for j in range(0, count_column):
                cell_info = QTableWidgetItem(str(rows_table[i][j]))
                self.ui.tableWidget.setItem(i, j, cell_info)

        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.setSortingEnabled(True)
