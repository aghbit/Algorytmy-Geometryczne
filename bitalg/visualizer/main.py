import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection


class Visualizer():
    def __init__(self):
        self.points_array = []
        self.line_segments_array = []

    def add_points(self, points, color=None):
        self.points_array.append((points, color))

    def add_line_segments(self, line_segments, color=None):
        self.line_segments_array.append((line_segments, color))

    def show(self):
        fig, ax = plt.subplots()

        ax.set_xlabel('x')
        ax.set_ylabel('y')

        for points, color in self.points_array:
            points = np.array(points)
            ax.scatter(points[:, 0], points[:, 1], color=color)

        for line_segments, color in self.line_segments_array:
            line_segments = np.array(line_segments)
            line_collection = LineCollection(line_segments, color=color)
            ax.add_collection(line_collection)

        ax.autoscale()

        fig.show(warn=False)

    # save informations about points and line segments of current Visualizer in file of given name $file_name
    def save_plot(self, file_name):
        with open(file_name, "w") as file:
            file.write("points\n")
            for points, color in self.points_array:
                file.write(color)
                file.write(points)
            file.write("\nline_segments\n")
            for line_segments, color in self.line_segments_array:
                file.write(color)
                file.write(line_segments)
        
    
    def _clear(self):
        self.points_array.clear()
        self.line_segments_array.clear()
    
    # clear current visualizer and fill it with elements from file of given name
    def open_plot(self, file_name):
        self._clear()
        with open(file_name, "r") as file:
            raise RuntimeError("not implement yet")