from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

from controllers.TermController import TermController
from windows.py.UiTermForm import UiTermForm


class TermForm(QtWidgets.QMainWindow):
    count_column = 4
    term_controller = TermController()
    filename = ''

    def __init__(self, filename):
        super(TermForm, self).__init__()
        self.ui = UiTermForm()
        self.ui.setupUi(self)
        self.filename = filename
        self.ui.addRowBtn.clicked.connect(self.add_row)
        self.ui.okBtn.clicked.connect(self.save_and_close)
        self.ui.deleteBtn.clicked.connect(self.delete_row)
        self.set_up_term_table()

    def set_up_term_table(self):
        self.ui.termTable.clear()
        self.ui.termTable.setSortingEnabled(False)
        self.ui.termTable.setHorizontalHeaderItem(0, QTableWidgetItem("Description"))
        self.ui.termTable.setHorizontalHeaderItem(1, QTableWidgetItem("Begin"))
        self.ui.termTable.setHorizontalHeaderItem(2, QTableWidgetItem("Top"))
        self.ui.termTable.setHorizontalHeaderItem(3, QTableWidgetItem("End"))
        self.load_data()
        self.ui.termTable.updateGeometry()

    def load_data(self):
        data = self.term_controller.get_data(filename=self.filename)

        self.ui.termTable.setRowCount(len(data))
        self.ui.termTable.setColumnCount(self.count_column)
        for i in range(0, len(data)):
            for j in range(0, len(data[i])):
                cell_info = QTableWidgetItem(str(data[i][j]))
                self.ui.termTable.setItem(i, j, cell_info)

    def add_row(self):
        self.ui.termTable.setRowCount(self.ui.termTable.rowCount()+1)
        self.ui.termTable.updateGeometry()

    def save_and_close(self):
        terms = []
        self.ui.termTable.setEnabled(False)
        for i in range(0, self.ui.termTable.rowCount()):
            item_term = []
            for j in range(0, self.ui.termTable.columnCount()):
                if self.ui.termTable.item(i, j) is None:
                    self.ui.termTable.setEnabled(True)
                    QMessageBox.warning(self, "Warning", "Some data is empty")
                    return
                item_term.append(self.ui.termTable.item(i, j).text())
            terms.append(item_term)
        self.ui.termTable.setEnabled(True)
        self.term_controller.save_data(terms, filename=self.filename)
        self.close()

    def delete_row(self):
        self.ui.termTable.removeRow(self.ui.termTable.currentRow())
