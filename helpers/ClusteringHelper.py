import numpy
import scipy.cluster.hierarchy as hcluster
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


class ClusteringHelper:

    def mape(self, y_predict, y_real, x_count):
        summ = 0
        for i in range(0, len(y_real)):
            summ += abs(y_real[i] - y_predict[i]) / y_real[i]

        if x_count * summ == 0:
            return 1

        return 1 / x_count * summ

    def get_k_means(self, data):
        km = KMeans(n_clusters=3)
        print(data)
        data_without_name = data.drop(data.columns[0], 1)
        scaler = StandardScaler()
        X = scaler.fit_transform(data_without_name)
        data[len(data.columns)] = km.fit_predict(data_without_name)
        return data

    def get_ierarch(self, data):
        thresh = 0
        data_without_name = data.drop(data.columns[0], 1)
        scaler = StandardScaler()
        X = scaler.fit_transform(data_without_name)
        data[len(data.columns)] = hcluster.fclusterdata(data_without_name, thresh, criterion="distance")
        return data

    def clastering_count(self, real, predict):
        X = [i for i in range(len(real))]
        Y = [self.mape(predict[i], real[i], len(real[i])) for i in range(0, len(real))]
        Data = numpy.array(Y).reshape(len(Y), 1)

        thresh = 0
        clusters = hcluster.fclusterdata(Data, thresh, criterion="distance")
        count_max = 0
        for i in clusters:
            if i == clusters.max():
                count_max += 1

        return len(set(clusters)), clusters.max(), count_max
        # plt.scatter(x=X, y=numpy.transpose(Data), c=clusters)
        # plt.axis("equal")
        # title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
        # plt.title(title)
        # plt.show()
