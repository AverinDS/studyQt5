from matplotlib import pyplot as plt
import random
import matplotlib.lines as mlines


class GraphicHelper:
    points_x = []
    points_y = []
    count_of_plot = 1
    name_graphic = "Graphic"
    points_x_anomaly = []
    points_y_anomaly = []
    terms_graphics = []
    color = ["b", "g", "r", "c", "m", "y", "k"]

    def show_graphic(self):
        plt.plot(self.points_x, self.points_y, 'b-', label=self.name_graphic)
        plt.plot(self.points_x_anomaly, self.points_y_anomaly, 'r.')
        for terms in self.terms_graphics:
            data_x = [float(i) for i in terms[0]]
            data_y = [float(i) for i in terms[1]]
            plt.plot(data_x,data_y)



        plt.show()

