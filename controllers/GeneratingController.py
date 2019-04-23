from helpers.ConstHolder import AnomalyConst
from helpers.GeneratorTS import GeneratorTS


class GeneratingController:
    components = []
    anomaly = AnomalyConst.AVOID
    clear_data = False

    def set_clear_data(self, is_clear):
        self.clear_data = is_clear

    def set_anomaly(self, anomaly_const):
        self.anomaly = anomaly_const

    def add_component(self, component):
        if self.components.count(component) == 0:
            self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def generate_data(self):
        generator = GeneratorTS(
            components=self.components,
            anomaly_strategy=self.anomaly,
            should_data_cleared=self.clear_data)
        generator.start_generating()
