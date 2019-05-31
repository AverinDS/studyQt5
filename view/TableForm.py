from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QAbstractItemView, QMessageBox

from controllers.TableController import TableController
from view.GeneratingForm import GeneratingForm
from view.TermForm import TermForm
from view.TermInGraphicForm import TermInGraphicForm
from windows.py.UiDatabaseWindow import UiDatabaseWindow


class TableForm(QtWidgets.QMainWindow):
    table_controller = TableController()

    def __init__(self):
        super(TableForm, self).__init__()
        self.ui = UiDatabaseWindow()
        self.ui.setupUi(self)
        self.ui.updateButton.clicked.connect(self.update_table)
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.ui.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.showGraphicButton.clicked.connect(self.show_graphic)
        self.ui.viewInFileButton.clicked.connect(self.show_in_file)
        self.ui.setTermBtn.clicked.connect(self.edit_terms)
        self.ui.generateBtn.clicked.connect(self.go_to_generate_form)
        self.ui.btnShowTerms.clicked.connect(self.show_terms_for_graphic)
        self.ui.buttonClastering.clicked.connect(self.show_clastering)
        self.ui.buttonFindBest.clicked.connect(self.findTheBestCoef)

        self.update_table()
        # Every list contains filename, trend, season, rand component
    def show_clastering(self):
        print("asdsad")
        self.table_controller.show_clastering()

    def findTheBestCoef(self):
        print("SAd")
        self.table_controller.find_the_bets_coef()

    def show_terms_for_graphic(self):
        if len(self.ui.tableWidget.selectedItems()) > 0:
            self.ST = TermInGraphicForm(filename=self.ui.tableWidget.selectedItems().__getitem__(0).text())
            self.ST.show()
        else:
            QMessageBox.warning(self, "Warning", "File not chosen")

    def go_to_generate_form(self):
        self.GF = GeneratingForm()
        self.GF.show()

    def edit_terms(self):
        if len(self.ui.tableWidget.selectedItems()) > 0:
            self.TF = TermForm(filename=self.ui.tableWidget.selectedItems().__getitem__(0).text())
            self.TF.show()
        else:
            QMessageBox.warning(self, "Warning", "File not chosen")

    def update_table(self):
        self.ui.tableWidget.clear()
        self.ui.tableWidget.setSortingEnabled(False)
        self.ui.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem("Filename"))
        self.ui.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem("Trend"))
        self.ui.tableWidget.setHorizontalHeaderItem(2, QTableWidgetItem("Season"))
        self.ui.tableWidget.setHorizontalHeaderItem(3, QTableWidgetItem("Random component"))

        table_data = self.table_controller.get_table_data()
        self.ui.tableWidget.setRowCount(len(table_data))
        if len(table_data) != 0:
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

    def show_in_file(self):
        filename = self.get_current_filename()
        if filename is not None:
            self.table_controller.open_file(filename)

    def get_current_filename(self):
        if len(self.ui.tableWidget.selectedItems()) > 0:
            return self.ui.tableWidget.selectedItems().__getitem__(0).text()
        else:
            QMessageBox.warning(self, "Warning", "File not chosen")
            return None
