from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from controllers.TermInGraphicController import TermInGraphicController
from helpers.ConstHolder import TranslatingConst
from windows.py.UiTermsInGraphic import UiTermsInGraphic


class TermInGraphicForm(QtWidgets.QMainWindow):
    termInGraphicController = TermInGraphicController()
    filename = ''

    def __init__(self, filename):
        super(TermInGraphicForm, self).__init__()
        self.filename = filename
        self.ui = UiTermsInGraphic()
        self.ui.setupUi(self)
        self.ui.radioButton_numbe_soft_vector.clicked.connect(self.number_soft_vector)
        self.ui.radioButton_number_soft_matrix.clicked.connect(self.number_soft_matrix)
        self.ui.radioButton_number_linguistic.clicked.connect(self.number_linguistic)
        self.ui.radioButton_number_soft_linguistic.clicked.connect(self.number_soft_linguistic)
        self.ui.radioButton_number_number.clicked.connect(self.number_number)
        self.number_soft_matrix()

    def set_data(self, rows_table, term_names):
        # rows_table, term_names = self.termInGraphicController.get_number_soft_matrix_data(filename=self.filename)
        self.ui.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("X"))
        self.ui.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Y"))

        count_column = len(term_names) + 2  # plus x point and y point
        self.ui.tableWidget.setColumnCount(count_column)
        self.ui.tableWidget.setRowCount(len(rows_table))
        for i in range(0, len(term_names)):
            self.ui.tableWidget.setHorizontalHeaderItem(i + 2,
                                                        QTableWidgetItem(str(term_names[i])))  # plus 2 because X and Y

        if self.termInGraphicController.mode == TranslatingConst.NUMBER_SOFT_VECTOR\
                or self.termInGraphicController.mode == TranslatingConst.NUMBER_LINGUISTIC \
                or self.termInGraphicController.mode == TranslatingConst.NUMBER_NUMBER:
            self.set_data_strings(rows_table=rows_table, count_column=count_column)
        else:
            self.set_data_numbers(rows_table=rows_table, count_column=count_column)

        self.ui.tableWidget.resizeColumnsToContents()
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.setSortingEnabled(True)

    def set_data_numbers(self, rows_table, count_column):
        self.clear_table()
        for i in range(0, len(rows_table)):
            for j in range(0, count_column):
                cell_info = QTableWidgetItem(str(rows_table[i][j]))
                self.ui.tableWidget.setItem(i, j, cell_info)

    def set_data_strings(self, rows_table, count_column):
        self.clear_table()
        for i in range(0, len(rows_table)):
            cell_info = QTableWidgetItem(str(rows_table[i]))
            self.ui.tableWidget.setItem(i, 2, cell_info)

    def clear_table(self):
        for i in range(3, self.ui.tableWidget.columnCount()):
            for j in range(0, self.ui.tableWidget.rowCount()):
                cell_info = QTableWidgetItem("")
                self.ui.tableWidget.setItem(j, i, cell_info)

    def number_soft_vector(self):
        self.termInGraphicController.set_mode(TranslatingConst.NUMBER_SOFT_VECTOR)
        rows_table, term_names = self.termInGraphicController.get_table_data(filename=self.filename)
        self.set_data(rows_table=rows_table, term_names=term_names)

    def number_soft_matrix(self):
        self.termInGraphicController.set_mode(TranslatingConst.NUMBER_SOFT_MATRIX)
        rows_table, term_names = self.termInGraphicController.get_table_data(filename=self.filename)
        self.set_data(rows_table=rows_table, term_names=term_names)

    def number_linguistic(self):
        self.termInGraphicController.set_mode(TranslatingConst.NUMBER_LINGUISTIC)
        rows_table, term_names = self.termInGraphicController.get_table_data(filename=self.filename)
        self.set_data(rows_table=rows_table, term_names=term_names)

    def number_soft_linguistic(self):
        self.termInGraphicController.set_mode(TranslatingConst.NUMBER_LINGUISTIC_SOFT)
        rows_table, term_names = self.termInGraphicController.get_table_data(filename=self.filename)
        self.set_data(rows_table=rows_table, term_names=term_names)

    def number_number(self):
        self.termInGraphicController.set_mode(TranslatingConst.NUMBER_NUMBER)
        rows_table, term_names = self.termInGraphicController.get_table_data(filename=self.filename)
        self.set_data(rows_table=rows_table, term_names=term_names)
