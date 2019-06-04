import os

from helpers.ClusteringHelper import ClusteringHelper
from helpers.ConstHolder import TermSetting
from helpers.DataHelper import DataHelper
from helpers.FolderParser import FolderParser
from helpers.GraphicHelper import GraphicHelper
from helpers.TermHelper import TermHelper


class TableController:
    folder_parser = FolderParser()
    graphic_helper = GraphicHelper()
    term_helper = TermHelper()
    clasteringHelper = ClusteringHelper()
    dataHelper = DataHelper()
    TREND_BORDER = 400
    SEASON_BORDER = 100
    RANDOM_BORDER = 0.3

    # list of lists. Every list contains filename, trend, season, rand component
    def get_table_data(self):
        return self.dataHelper.get_table_data()


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







