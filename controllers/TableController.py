import os

from helpers.FolderParser import FolderParser
from helpers.GraphicHelper import GraphicHelper


class TableController:
    folder_parser = FolderParser()
    graphic_helper = GraphicHelper()

    def get_table_data(self):
        return self.folder_parser.parse()

    def show_graphic(self, filename):
        self.graphic_helper.points_y = []
        self.graphic_helper.points_x = []
        self.graphic_helper.count_of_plot = 1
        self.graphic_helper.name_graphic = filename

        points_x, points_y = self.folder_parser.get_points_from_file_by_filename(filename)
        self.graphic_helper.points_y = points_y
        self.graphic_helper.points_x = points_x
        self.graphic_helper.show_graphic()

    def open_file(self, filename):
        path_to_file = self.folder_parser.get_path_to_file(filename)
        if path_to_file is not None:
            os.system("open '" + path_to_file + "'")
            # os.system("start " + path_to_file)