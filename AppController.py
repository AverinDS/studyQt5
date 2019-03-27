from PyQt5 import QtWidgets

from view.TableView import TableView
import sys

app = QtWidgets.QApplication([])
application = TableView()
application.show()
sys.exit(app.exec())
