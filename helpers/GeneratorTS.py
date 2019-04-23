import math
import os
import random
from itertools import cycle
from shutil import rmtree

from helpers.FolderParser import random_name, season_name, lin_name, lin_season_name, lin_rand_name, \
    lin_rand_season_name, rand_season_name
from .ConstHolder import *


class GeneratorTS:
    def __init__(self, components, anomaly_strategy, should_data_cleared) -> None:
        self.components = components
        self.anomaly_strategy = anomaly_strategy
        self.should_data_cleared = should_data_cleared

    components = []
    anomaly_strategy = AnomalyConst.AVOID
    should_data_cleared = True
    path_to_timeseries = "./timeseries/"

    colors = cycle('bgrcmk')

    # Linear function: ax+ b
    a = [random.randint(-20, 20) for _ in range(0, GeneratorSetting.COUNT_OF_MODELS)]
    b = [random.randint(-20, 20) for _ in range(0, GeneratorSetting.COUNT_OF_MODELS)]

    def make_real_time_series(self):
        list_of_points = []
        for _ in range(0, GeneratorSetting.MAX_TIME):
            list_of_points.append(random.randint(0, GeneratorSetting.MAX_VALUE))

        # save_model_to_file(list_of_points, path, "REAL")
        return list_of_points

    def random_time_series(self):
        list_of_points = []
        for _ in range(0, GeneratorSetting.MAX_TIME):
            list_of_points.append(random.randint(0, GeneratorSetting.MAX_VALUE))
        return list_of_points

    def get_a(self, index):
        return self.a[index]

    def get_b(self, index):
        return self.b[index]

    def get_name_a_b(self, index):
        return str(" A=" + str(self.a[index]) + " B=" + str(self.b[index]))

    # linear function:  kt + c
    def lin_function(self, k, c):
        list_of_points = []
        for t in range(0, GeneratorSetting.MAX_TIME):
            list_of_points.append(k * t + c)

        return list_of_points

    def season(self, index=-1):
        list_of_points = []
        for t in range(0, GeneratorSetting.MAX_TIME):
            if index != -1:
                list_of_points.append(math.sin(t) * self.get_a(index) * self.get_a(index))
            else:
                list_of_points.append(math.sin(t))

        return list_of_points

    def merge(self, list1=None, list2=None, list3=None):
        list_of_points = []

        if list3 is None:
            list3 = []

        if list2 is None:
            list2 = []

        if list1 is None:
            list1 = []

        if len(list1) == 0:
            list1 = [0 for _ in range(0, GeneratorSetting.MAX_TIME)]

        if len(list2) == 0:
            list2 = [0 for _ in range(0, GeneratorSetting.MAX_TIME)]

        if len(list3) == 0:
            list3 = [0 for _ in range(0, GeneratorSetting.MAX_TIME)]

        for t in range(0, GeneratorSetting.MAX_TIME):
            list_of_points.append(list1[t] + list2[t] + list3[t])

        self.add_anomaly(list_of_points)

        return list_of_points

    def add_anomaly(self, list_of_points):
        count_of_anomaly = int(GeneratorSetting.MAX_TIME / 15)
        if self.anomaly_strategy == AnomalyConst.AVOID:
            return list_of_points
        if self.anomaly_strategy == AnomalyConst.SINGLE:
            for i in range(0, count_of_anomaly):
                list_of_points[random.randint(0, GeneratorSetting.MAX_TIME - 1)] = random.randint(0,
                                                                                                  GeneratorSetting.MAX_VALUE)
        if self.anomaly_strategy == AnomalyConst.GROUP:
            for i in range(0, count_of_anomaly):
                group_size = random.randint(0, int(GeneratorSetting.MAX_TIME / 100))
                start_index = random.randint(0, GeneratorSetting.MAX_TIME)

                for j in range(start_index, start_index + group_size):
                    if j >= len(list_of_points):
                        continue
                    list_of_points[j] = random.randint(0, GeneratorSetting.MAX_VALUE)

    def save_model_to_file(self, list_points, path, filename):
        if not os.path.exists(self.path_to_timeseries):
            os.makedirs(self.path_to_timeseries)
        path = self.path_to_timeseries + path
        if not os.path.exists(path):
            os.makedirs(path)
        copy_mark = '(copy)'
        while os.path.exists(path + str(filename) + '.txt'):
            filename += copy_mark

        new_file = open(path + str(filename) + '.txt', 'w')
        new_file.write(str(len(list_points)) + '\n\n')
        for i in range(0, len(list_points)):
            new_file.write(str(i) + " " + str(list_points[i]) + '\n')

    def recreate_folder(self, folder_name):
        if os.path.exists(self.path_to_timeseries + folder_name):
            rmtree(self.path_to_timeseries + folder_name)
        os.makedirs(self.path_to_timeseries + folder_name)

    def start_generating(self):
        if self.should_data_cleared:
            if os.path.exists(self.path_to_timeseries):
                rmtree(self.path_to_timeseries)
                os.makedirs(self.path_to_timeseries)
            self.recreate_folder(random_name)
            self.recreate_folder(season_name)
            self.recreate_folder(lin_name)
            self.recreate_folder(lin_season_name)
            self.recreate_folder(lin_rand_name)
            self.recreate_folder(lin_rand_season_name)
            self.recreate_folder(rand_season_name)

        real_list_points = self.make_real_time_series()
        self.save_model_to_file(
            list_points=real_list_points,
            path="",
            filename="RealData"
        )

        if self.components.count(ComponentsConst.TREND) != 0:
            for j in range(0, GeneratorSetting.COUNT_OF_MODELS):
                list_points = self.merge(self.lin_function(self.get_a(j), self.get_b(j)))

                self.save_model_to_file(
                    list_points=list_points,
                    path=lin_name + "/",
                    filename="Lin" + str(j) + self.get_name_a_b(j)
                )

        if self.components.count(ComponentsConst.TREND) != 0 and self.components.count(ComponentsConst.SEASONS) != 0:
            for j in range(0, GeneratorSetting.COUNT_OF_MODELS):
                list_points = self.merge(self.lin_function(self.get_a(j), self.get_b(j)), self.season(index=j))

                self.save_model_to_file(
                    list_points=list_points,
                    path=lin_season_name + "/",
                    filename="LinSeason" + str(j) + self.get_name_a_b(j)
                )

        if self.components.count(ComponentsConst.TREND) != 0 and self.components.count(ComponentsConst.RANDOM) != 0:
            for j in range(0, GeneratorSetting.COUNT_OF_MODELS):
                list_points = self.merge(self.lin_function(self.get_a(j), self.get_b(j)), self.random_time_series())

                self.save_model_to_file(
                    list_points=list_points,
                    path=lin_rand_name + "/",
                    filename="LinRand" + str(j) + self.get_name_a_b(j)
                )

        if self.components.count(ComponentsConst.TREND) != 0 and self.components.count(ComponentsConst.SEASONS) != 0:
            for j in range(0, GeneratorSetting.COUNT_OF_MODELS):
                list_points = self.merge(self.lin_function(self.get_a(j), self.get_b(j)), self.season(),
                                         self.random_time_series())

                self.save_model_to_file(
                    list_points=list_points,
                    path=lin_rand_season_name + "/",
                    filename="LinRandSeason" + str(j) + self.get_name_a_b(j)
                )

        if self.components.count(ComponentsConst.SEASONS) != 0:
            for j in range(0, GeneratorSetting.COUNT_OF_MODELS):
                list_points = self.merge(self.season())
                self.save_model_to_file(
                    list_points=list_points,
                    path=season_name + "/",
                    filename="Season" + str(j)
                )

        if self.components.count(ComponentsConst.SEASONS) != 0 and self.components.count(ComponentsConst.RANDOM) != 0:
            for j in range(0, GeneratorSetting.COUNT_OF_MODELS):
                list_points = self.merge(self.season(), self.random_time_series())
                self.save_model_to_file(
                    list_points=list_points,
                    path=rand_season_name + "/",
                    filename="RandSeason" + str(j)
                )

        if self.components.count(ComponentsConst.RANDOM) != 0:
            for j in range(0, GeneratorSetting.COUNT_OF_MODELS):
                list_points = self.merge(self.random_time_series())
                self.save_model_to_file(
                    list_points=self.merge(self.random_time_series()),
                    path=random_name + "/",
                    filename="Rand" + str(j)
                )
