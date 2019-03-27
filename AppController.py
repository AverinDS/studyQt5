from PyQt5 import QtWidgets

from view.DatabaseView import DatabaseView
import sys


app = QtWidgets.QApplication([])
application = DatabaseView()
application.show()
sys.exit(app.exec())