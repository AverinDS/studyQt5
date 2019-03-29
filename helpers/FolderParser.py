import os
import re

random_name = "RAND"
season_name = "SEASON"
lin_name = "LIN"
lin_season_name = "LIN_SEASON"
lin_rand_name = "LIN_RAND"
lin_rand_season_name = "LIN_RAND_SEASON"
rand_season_name = "RAND_SEASON"

folders = [random_name, season_name, lin_name, lin_season_name, lin_rand_name, lin_rand_season_name, rand_season_name]
path_to_timeseries = "../modelling/timeseries/"

up = "Рост "
down = "Падение "


class FolderParser:
    # list of lists. Every list contains filename, trend, season, rand component
    features = []
    req_expr_a = re.compile("A=[+-?]\d*")

    def parse(self):
        self.features.clear()
        for folder in folders:
            if not os.path.exists(path_to_timeseries + folder):
                continue

            file_names = os.listdir(path_to_timeseries + folder)

            for file_name in file_names:
                patterns_file = [file_name]

                # find A coef
                if self.req_expr_a.findall(file_name, 0):
                    coef_a = int(str(self.req_expr_a.findall(file_name, 0)[0]).replace("A=", ""))
                    if coef_a is not None and coef_a > 0:
                        patterns_file.append(up + str(coef_a))
                    else:
                        if coef_a is not None and coef_a < 0:
                            patterns_file.append(down + str(coef_a))
                        else:
                            patterns_file.append("-")

                # find trend component
                if folder.__contains__(lin_name):
                    patterns_file.append("+")
                else:
                    patterns_file.append("-")

                #  find season component
                if folder.__contains__(season_name):
                    patterns_file.append("+")
                else:
                    patterns_file.append("-")

                # find rand component
                if folder.__contains__(random_name):
                    patterns_file.append("+")
                else:
                    patterns_file.append("-")

                self.features.append(patterns_file)

        return self.features

    def get_points_from_file_by_filename(self, filename):
        points_x = []
        points_y = []
        for folder in folders:
            if not os.path.exists(path_to_timeseries + folder):
                continue
            file_names = os.listdir(path_to_timeseries + folder)
            if file_names.__contains__(filename):
                with open(path_to_timeseries + folder + "/" + filename) as file:
                    for line in file.readlines():
                        if len(line.split(" ")) != 2:
                            continue
                        points_x.append(float(line.split(" ")[0]))
                        points_y.append(float(line.split(" ")[1]))
        return points_x, points_y

    def get_path_to_file(self, filename):
        for folder in folders:
            if not os.path.exists(path_to_timeseries + folder):
                continue
            file_names = os.listdir(path_to_timeseries + folder)
            if file_names.__contains__(filename):
                return path_to_timeseries + folder + "/" + filename
        return None
