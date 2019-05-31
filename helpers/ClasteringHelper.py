import matplotlib.pyplot as plt
import numpy
import scipy.cluster.hierarchy as hcluster


class ClasteringHelper:

    def mape(self, y_predict, y_real, x_count):
        summ = 0
        for i in range(0, len(y_real)):
            summ += abs(y_real[i] - y_predict[i]) / y_real[i]

        if x_count * summ == 0:
            return 1

        return 1 / x_count * summ

    def clastering_show(self, real, predict):
        X = [i for i in range(len(real))]
        Y = [self.mape(predict[i], real[i], len(real[i])) for i in range(0, len(real))]
        Data = numpy.array(Y).reshape(len(Y), 1)

        thresh = 0.16666666666
        clusters = hcluster.fclusterdata(Data, thresh, criterion="distance")
        plt.scatter(x=X, y=numpy.transpose(Data), c=clusters)
        plt.axis("equal")
        title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
        plt.title(title)
        plt.show()

    def clastering_count(self, real, predict):
        X = [i for i in range(len(real))]
        Y = [self.mape(predict[i], real[i], len(real[i])) for i in range(0, len(real))]
        Data = numpy.array(Y).reshape(len(Y), 1)

        thresh = 0
        clusters = hcluster.fclusterdata(Data, thresh, criterion="distance")
        return len(set(clusters))
        # plt.scatter(x=X, y=numpy.transpose(Data), c=clusters)
        # plt.axis("equal")
        # title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
        # plt.title(title)
        # plt.show()
