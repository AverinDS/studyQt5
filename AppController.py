import sys

from PyQt5 import QtWidgets

from view.TableForm import TableForm

app = QtWidgets.QApplication([])
application = TableForm()
application.show()
sys.exit(app.exec())
