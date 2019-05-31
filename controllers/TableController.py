import math
import os

import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

from helpers.ClasteringHelper import ClasteringHelper
from helpers.ConstHolder import TermSetting
from helpers.FolderParser import FolderParser
from helpers.GraphicHelper import GraphicHelper
from helpers.TermHelper import TermHelper


class TableController:
    folder_parser = FolderParser()
    graphic_helper = GraphicHelper()
    term_helper = TermHelper()
    clasteringHelper = ClasteringHelper()
    TREND_BORDER = 400
    SEASON_BORDER = 100
    RANDOM_BORDER = 0.3

    # list of lists. Every list contains filename, trend, season, rand component
    def get_table_data(self):
        real_data = self.folder_parser.parse()
        for i in range(0, len(real_data)):
            real_data[i] = self.analyze_components(real_data[i])
        return real_data

    def show_graphic(self, filename):
        self.graphic_helper.points_y = []
        self.graphic_helper.points_x = []
        self.graphic_helper.count_of_plot = 1
        self.graphic_helper.name_graphic = filename

        points_x, points_y = self.folder_parser.get_points_from_file_by_filename(filename)
        points_x_anomaly, points_y_anomaly = self.folder_parser.get_anomaly_from_file(filename)
        self.graphic_helper.points_x_anomaly = points_x_anomaly
        self.graphic_helper.points_y_anomaly = points_y_anomaly
        self.graphic_helper.points_y = points_y
        self.graphic_helper.points_x = points_x
        self.graphic_helper.terms_graphics = self.terms_to_graphic_data(filename)
        self.graphic_helper.show_graphic()

    def open_file(self, filename):
        path_to_file = self.folder_parser.get_path_to_file(filename)
        if path_to_file is not None:
            os.system("open '" + path_to_file + "'")
            # os.system("start " + path_to_file)

    def terms_to_graphic_data(self, filename):

        terms = self.term_helper.get_terms(filename)
        graphics = []

        for term in terms:
            a = term[1]
            b = term[2]
            c = term[3]
            graphics.append([[0, TermSetting.MARGIN, 0], [a, b, c]])
        return graphics

    def analyze_components(self, components):
        x, y = self.folder_parser.get_points_from_file_by_filename(components[0])
        data_frame = pd.DataFrame(data=y)
        # print(data_frame)
        decomposed = seasonal_decompose(data_frame, model='additive', freq=10)
        # print(components[0])
        # decomposed.plot()
        # plt.show()
        # print(components[0])
        trend_component = y
        # trend_component = self.prepare_dataframe(decomposed.ob)
        season_component = y
        # season_component = self.prepare_dataframe(decomposed.observed)
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

    def show_clastering(self):
        normalize_real, predict_data = self.get_normal_data()
        self.clasteringHelper.clastering_show(normalize_real, predict_data)

    def find_the_bets_coef(self):
        real_data = self.get_table_data()
        best = len(real_data)
        BEST_TREND = 0
        BEST_SEASON = 0
        BEST_RAND = 0

        for i in range(0, int(self.getMaxValueFromGraphics()), 10):
            print("new step TREND", i)
            self.TREND_BORDER = i
            normalize_real, predict_data = self.get_normal_data()
            count_clast = self.clasteringHelper.clastering_count(normalize_real, predict_data)
            if count_clast < best:
                BEST_TREND = i
                best = count_clast
                print("NEW BEST_TREND", BEST_TREND)
                print("COUNT_CLAST", best)

        for i in range(0, int(self.getMaxValueFromGraphics()),10):
            print("new step SEASON", i)
            self.SEASON_BORDER = i
            normalize_real, predict_data = self.get_normal_data()
            count_clast = self.clasteringHelper.clastering_count(normalize_real, predict_data)
            if count_clast < best:
                BEST_SEASON = i
                best = count_clast
                print("NEW BEST_SEASON", BEST_SEASON)
                print("COUNT_CLAST", best)

        i = 0
        count_clast = 0
        while i < 10:
            print("new step RAND", i)
            self.RANDOM_BORDER = i
            normalize_real, predict_data = self.get_normal_data()
            count_clast = self.clasteringHelper.clastering_count(normalize_real, predict_data)
            if count_clast < best:
                BEST_RAND = i
                best = count_clast
                print("NEW BEST RAND", BEST_RAND)
                print("COUNT_CLAST", best)

            i+=0.1

        print("BEST TREND", BEST_TREND)
        print("BEST SEASON", BEST_SEASON)
        print("BEST RAND", BEST_RAND)
        print("COUNT_CLAST", best)






    def getMaxValueFromGraphics(self):
        maxV = 0
        real_data = self.get_table_data()
        for arr in real_data:
            x, y = self.folder_parser.get_points_from_file_by_filename(arr[0])
            if max(y) > maxV:
                maxV = max(y)

        return maxV

    def get_normal_data(self):
        real_data = self.get_table_data()
        normalize_real = []
        predict_data = []
        for index in range(len(real_data)):
            predict = []
            real = []
            for i in range(1, 4):
                if real_data[index][i].count('+') > 0:
                    real.append(2)
                else:
                    real.append(1)

                if real_data[index][i + 3].count('+') > 0:
                    predict.append(2)
                else:
                    predict.append(1)

            normalize_real.append(real)
            predict_data.append(predict)
        return normalize_real, predict_data



