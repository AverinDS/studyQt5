from matplotlib import pyplot as plt


class GraphicHelper:
    points_x = []
    points_y = []
    count_of_plot = 1
    name_graphic = "Graphic"
    points_x_anomaly = []
    points_y_anomaly = []

    def show_graphic(self):
        plt.plot(self.points_x, self.points_y, 'b-', label=self.name_graphic)
        plt.plot(self.points_x_anomaly, self.points_y_anomaly, 'r.')

        plt.show()
