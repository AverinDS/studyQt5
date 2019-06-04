import math

import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

from helpers.FolderParser import FolderParser


class DataHelper:
    folder_parser = FolderParser()
    TREND_BORDER = 400
    SEASON_BORDER = 100
    RANDOM_BORDER = 0.3

    def get_normal_data(self):
        real_data = self.get_table_data()
        normalize_real = []
        for index in range(len(real_data)):
            real = []
            real.append(real_data[index][0])
            for i in range(1, 7):
                if real_data[index][i].count('+') > 0:
                    real.append(1)
                else:
                    real.append(0)

            normalize_real.append(real)
        return pd.DataFrame(normalize_real)

    def get_table_data(self):
        real_data = self.folder_parser.parse()
        for i in range(0, len(real_data)):
            real_data[i] = self.analyze_components(real_data[i])
        return real_data

    def analyze_components(self, components):
        x, y = self.folder_parser.get_points_from_file_by_filename(components[0])
        data_frame = pd.DataFrame(data=y)
        decomposed = seasonal_decompose(data_frame, model='additive', freq=10)
        trend_component = y
        season_component = y
        random_component = self.prepare_dataframe(decomposed.resid)

        if self.have_trend(trend_component, max(y)):
            components.append("T+")
        else:
            components.append("T-")

        if self.have_seasons(season_component, max(y)):
            components.append("S+")
        else:
            components.append("S-")

        if self.have_random(random_component, max(y)):
            components.append("R+")
        else:
            components.append("R-")

        return components

    def prepare_dataframe(self, data_frame):
        data = data_frame.ix[:, 0].tolist()
        for i in range(0, len(data_frame)):
            if math.isnan(data[i]):
                data[i] = 0
        return data

    def have_trend(self, data_frame, max_value):
        value_up = 0
        value_down = 0
        current = data_frame[0]
        for i in range(1, len(data_frame)):
            if current > data_frame[i]:
                value_down += (current - data_frame[i])
            else:
                value_up += (data_frame[i] - current)
            current = data_frame[i]
        if abs(value_up - value_down) > self.TREND_BORDER:
            return True
        else:
            return False

    def have_seasons(self, data_frame, max_value):
        value_up = 0
        value_down = 0
        current = data_frame[0]
        for i in range(1, len(data_frame)):
            if current > data_frame[i]:
                value_down += 1
            else:
                value_up += 1
            current = data_frame[i]
        if abs(value_up - value_down) < self.SEASON_BORDER and value_down != 0 and value_up != 0:
            return True
        else:
            return False

    def have_random(self, data_frame, max_value):
        if max(data_frame) == 0:
            return False
        if max(data_frame) / max_value > self.RANDOM_BORDER:
            return True
        else:
            return False
