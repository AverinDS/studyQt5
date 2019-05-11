import math
import os
import random
from itertools import cycle
from shutil import rmtree

from helpers.FolderParser import random_name, season_name, lin_name, lin_season_name, lin_rand_name, \
    lin_rand_season_name, rand_season_name
from helpers.TermHelper import TermHelper
from .ConstHolder import *


class GeneratorTS:
    def __init__(self, count_of_points_ts, count_of_anomaly, count_of_terms, components, anomaly_strategy,
                 should_data_cleared) -> None:
        self.count_of_anomaly = int(count_of_anomaly)
        self.count_of_points_ts = int(count_of_points_ts)
        self.components = components
        self.anomaly_strategy = anomaly_strategy
        self.should_data_cleared = should_data_cleared
        self.count_of_terms = count_of_terms

    components = []
    count_of_points_ts = 800
    count_of_anomaly = 20
    count_of_terms = 5
    anomaly_strategy = AnomalyConst.AVOID
    should_data_cleared = True
    path_to_timeseries = "./timeseries/"
    path_to_anomaly = "./anomaly/"
    anomaly = []
    term_helper = TermHelper()

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
                list_of_points.append(math.sin(t) * GeneratorSetting.MAX_VALUE)

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

        # for t in range(0, GeneratorSetting.MAX_TIME):
        #     if list1[t] + list2[t] + list3[t] <= GeneratorSetting.MAX_VALUE:
        #         if list1[t] + list2[t] + list3[t] < 0:
        #             list_of_points.append(0)
        #         else:
        #             list_of_points.append(list1[t] + list2[t] + list3[t])
        #     else:
        #         list_of_points.append(GeneratorSetting.MAX_VALUE)

        self.add_anomaly(list_of_points)

        return list_of_points

    def add_anomaly(self, list_of_points):
        if self.anomaly_strategy == AnomalyConst.AVOID:
            return list_of_points
        if self.anomaly_strategy == AnomalyConst.SINGLE:
            for i in range(0, self.count_of_anomaly):
                list_index = random.randint(0, GeneratorSetting.MAX_TIME - 1)
                while self.anomaly_has_exist(list_index):
                    list_index = random.randint(0, GeneratorSetting.MAX_TIME - 1)

                anomaly_value = random.randint(int(min(list_of_points)), int(max(list_of_points)))
                list_of_points[list_index] = anomaly_value
                self.anomaly.append([list_index, anomaly_value])

        if self.anomaly_strategy == AnomalyConst.GROUP:
            for i in range(0, self.count_of_anomaly):
                group_size = random.randint(AnomalyConst.MIN_GROUP_SIZE, int(
                    GeneratorSetting.MAX_TIME / 100) + AnomalyConst.MIN_GROUP_SIZE)  # constraint interval from 2
                start_index = random.randint(0, GeneratorSetting.MAX_TIME - 1)  # not more that last - 1

                for j in range(start_index, start_index + group_size):
                    if j >= len(list_of_points) or self.anomaly_has_exist(j):
                        continue
                    anomaly_value = random.randint(int(min(list_of_points)), int(max(list_of_points)))
                    list_of_points[j] = anomaly_value
                    self.anomaly.append([j, anomaly_value])

    def anomaly_has_exist(self, index):
        for i, val in self.anomaly:
            if i == index:
                return True
        return False

    def save_model_to_file(self, list_points, path, filename):
        if not os.path.exists(self.path_to_timeseries):
            os.makedirs(self.path_to_timeseries)
        path = self.path_to_timeseries + path
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(self.path_to_anomaly):
            os.makedirs(self.path_to_anomaly)

        copy_mark = '(copy)'
        while os.path.exists(path + str(filename) + '.txt'):
            filename += copy_mark

        new_file = open(path + str(filename) + '.txt', 'w')
        new_file.write(str(len(list_points)) + '\n\n')
        for i in range(0, len(list_points)):
            new_file.write(str(i) + " " + str(list_points[i]) + '\n')
        new_file.close()

        anomaly_file = open(self.path_to_anomaly + str(filename) + '.txt', 'w')
        for point in self.anomaly:
            anomaly_file.write(str(point[0]) + " " + str(point[1]) + '\n')
        anomaly_file.close()
        self.anomaly = []

    def recreate_folder(self, folder_name):
        if os.path.exists(self.path_to_timeseries + folder_name):
            rmtree(self.path_to_timeseries + folder_name)
        os.makedirs(self.path_to_timeseries + folder_name)

    def start_generating(self):
        if os.path.exists(self.path_to_anomaly):
            rmtree(self.path_to_anomaly)

        GeneratorSetting.MAX_TIME = self.count_of_points_ts
        TermSetting.COUNT_OF_TERMS = self.count_of_terms
        self.term_helper.generate_terms()

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
                self.save_model_to_file(
                    list_points=self.merge(self.random_time_series()),
                    path=random_name + "/",
                    filename="Rand" + str(j)
                )
