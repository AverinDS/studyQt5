from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox

from controllers.GeneratingController import GeneratingController
from helpers.ConstHolder import ComponentsConst, AnomalyConst
from windows.py.UiGenerateForm import UiGenerateForm


class GeneratingForm(QtWidgets.QMainWindow):
    generation_controller = GeneratingController()

    def __init__(self):
        super(GeneratingForm, self).__init__()
        self.ui = UiGenerateForm()
        self.ui.setupUi(self)
        self.ui.randomCheckBox.stateChanged.connect(self.random_check_changed)
        self.ui.seasonsCheckBox.stateChanged.connect(self.seasons_check_changed)
        self.ui.trendCheckBox.stateChanged.connect(self.trend_check_changed)
        self.ui.removeAllDataCheckBox.stateChanged.connect(self.remove_all_data_changed)
        self.ui.cancelButton.clicked.connect(self.cancel)
        self.ui.proceedButton.clicked.connect(self.proceed)
        self.ui.singleRadioButton.clicked.connect(self.single_anomaly_check)
        self.ui.groupRadioButton.clicked.connect(self.group_anomaly_check)
        self.ui.avoidRadioButton.clicked.connect(self.avoid_anomaly_check)
        self.ui.textEditCountAnomaly.textChanged.connect(self.count_anomaly_changed)
        self.ui.textEditCountPosintsTS.textChanged.connect(self.count_points_changed)
        self.ui.textEditCountOfTerms.textChanged.connect(self.count_terms_changed)

    def count_terms_changed(self):
        if not str(self.ui.textEditCountOfTerms.toPlainText()).__eq__(''):
            try:
                self.generation_controller.set_count_terms(int(self.ui.textEditCountOfTerms.toPlainText()))
            except Exception:
                self.generation_controller.set_count_terms(5)
                self.ui.textEditCountOfTerms.setText('5')


    def count_anomaly_changed(self):
        if not str(self.ui.textEditCountAnomaly.toPlainText()).__eq__(''):
            try:
                self.generation_controller.set_count_anomaly(int(self.ui.textEditCountAnomaly.toPlainText()))
            except Exception:
                self.generation_controller.set_count_anomaly(20)
                self.ui.textEditCountAnomaly.setText('20')

    def count_points_changed(self):
        if not str(self.ui.textEditCountPosintsTS.toPlainText()).__eq__(''):
            try:
                self.generation_controller.set_count_points_ts(int(self.ui.textEditCountPosintsTS.toPlainText()))
            except Exception:
                self.generation_controller.set_count_points_ts(800)
                self.ui.textEditCountPosintsTS.setText('800')

    def single_anomaly_check(self):
        self.generation_controller.anomaly = AnomalyConst.SINGLE

    def group_anomaly_check(self):
        self.generation_controller.anomaly = AnomalyConst.GROUP

    def avoid_anomaly_check(self):
        self.generation_controller.anomaly = AnomalyConst.AVOID

    def random_check_changed(self):
        if self.ui.randomCheckBox.isChecked():
            self.generation_controller.add_component(ComponentsConst.RANDOM)
        else:
            self.generation_controller.remove_component(ComponentsConst.RANDOM)

    def seasons_check_changed(self):
        if self.ui.seasonsCheckBox.isChecked():
            self.generation_controller.add_component(ComponentsConst.SEASONS)
        else:
            self.generation_controller.remove_component(ComponentsConst.SEASONS)

    def trend_check_changed(self):
        if self.ui.trendCheckBox.isChecked():
            self.generation_controller.add_component(ComponentsConst.TREND)
        else:
            self.generation_controller.remove_component(ComponentsConst.TREND)

    def remove_all_data_changed(self):
        if self.ui.removeAllDataCheckBox.isChecked():
            self.generation_controller.clear_data = True
        else:
            self.generation_controller.clear_data = False

    def cancel(self):
        self.close()

    def proceed(self):
        self.generation_controller.generate_data()
        QMessageBox.warning(self, "Notification", "Generating complete!")
        self.close()
