import pandas as pd

from helpers.ClusteringHelper import ClusteringHelper
from helpers.ConstHolder import ClusteringConst
from helpers.DataHelper import DataHelper


class ClusteringController():

    clasteringHelper = ClusteringHelper()
    dataHelper = DataHelper()

    def getTableData(self, mode):
        if mode == ClusteringConst.KMEANS:
            return self.clasteringHelper.get_k_means(self.dataHelper.get_normal_data())
        if mode == ClusteringConst.IERH:
            return self.clasteringHelper.get_ierarch(self.dataHelper.get_normal_data())



