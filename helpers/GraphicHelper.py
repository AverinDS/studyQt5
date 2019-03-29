from matplotlib import pyplot as plt


class GraphicHelper:
    points_x = []
    points_y = []
    count_of_plot = 1
    name_graphic = "Graphic"

    def show_graphic(self):
        plt.subplot(2, 1, self.count_of_plot)  # 2 строки и один столбец
        plt.plot(self.points_x, self.points_y, 'b', label=self.name_graphic)
        plt.show()
