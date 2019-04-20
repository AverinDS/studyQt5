from PyQt5 import QtWidgets

from windows.py.UiGenerateForm import UiGenerateForm


class GeneratingForm(QtWidgets.QMainWindow):
    def __init__(self):
        super(GeneratingForm, self).__init__()
        self.ui = UiGenerateForm()
        self.ui.setupUi(self)
