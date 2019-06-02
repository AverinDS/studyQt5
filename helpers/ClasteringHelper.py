import matplotlib.pyplot as plt
import numpy
from pandas import DataFrame
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler, StandardScaler
import scipy.cluster.hierarchy as hcluster
import scipy.spatial.distance


class ClasteringHelper:

    def mape(self, y_predict, y_real, x_count):
        summ = 0
        for i in range(0, len(y_real)):
            summ += abs(y_real[i] - y_predict[i]) / y_real[i]

        if x_count * summ == 0:
            return 1

        return 1 / x_count * summ

    def clastering_show(self, data):

        km = KMeans(n_clusters=6)
        print(data)
        data_without_name = data.drop(data.columns[0], 1)
        scaler = StandardScaler()
        X = scaler.fit_transform(data_without_name)
        data['cluster'] = km.fit_predict(data_without_name)
        print(data)

        thresh = 0
        clusters = hcluster.fclusterdata(data_without_name, thresh, criterion="distance")
        print(clusters)
        plt.hist(data=data['cluster'], x=data[data.columns[0]])
        # plt.scatter( y=numpy.transpose(data_without_name), c=clusters)
        # plt.axis("equal")
        # title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
        # plt.title(title)
        plt.show()

    def clastering_count(self, real, predict):
        X = [i for i in range(len(real))]
        Y = [self.mape(predict[i], real[i], len(real[i])) for i in range(0, len(real))]
        Data = numpy.array(Y).reshape(len(Y), 1)

        thresh = 0
        clusters = hcluster.fclusterdata(Data, thresh, criterion="distance")
        count_max = 0
        for i in clusters:
            if i == clusters.max():
                count_max+=1

        return len(set(clusters)), clusters.max(), count_max
        # plt.scatter(x=X, y=numpy.transpose(Data), c=clusters)
        # plt.axis("equal")
        # title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
        # plt.title(title)
        # plt.show()
