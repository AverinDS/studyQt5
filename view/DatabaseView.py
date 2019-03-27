from PyQt5 import QtWidgets

from windows.py.Ui_database_window import Ui_database_window


class DatabaseView(QtWidgets.QMainWindow):
    def __init__(self):
        super(DatabaseView, self).__init__()
        self.ui = Ui_database_window()
        self.ui.setupUi(self)

