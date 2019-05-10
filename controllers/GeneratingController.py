from helpers.ConstHolder import AnomalyConst
from helpers.GeneratorTS import GeneratorTS


class GeneratingController:
    components = []
    anomaly = AnomalyConst.AVOID
    clear_data = True
    # default values
    count_anomaly = 20
    count_of_points_ts = 800
    count_of_terms = 5

    def set_clear_data(self, is_clear):
        self.clear_data = is_clear

    def set_anomaly(self, anomaly_const):
        self.anomaly = anomaly_const

    def set_count_anomaly(self, count_anomaly):
        self.count_anomaly = count_anomaly

    def set_count_terms(self, count_terms):
        self.count_of_terms = count_terms

    def set_count_points_ts(self, count_points_ts):
        self.count_of_points_ts = count_points_ts

    def add_component(self, component):
        if self.components.count(component) == 0:
            self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def generate_data(self):
        generator = GeneratorTS(
            components=self.components,
            anomaly_strategy=self.anomaly,
            should_data_cleared=self.clear_data,
            count_of_points_ts=self.count_of_points_ts,
            count_of_anomaly=self.count_anomaly,
            count_of_terms=self.count_of_terms
        )
        generator.start_generating()
