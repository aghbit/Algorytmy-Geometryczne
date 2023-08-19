from .figure import Figure
import numpy as np


class Point(Figure):
    def __init__(self, data, options):
        data = np.array(data).reshape(-1, 2)
        super().__init__(data, options)

    def draw(self, ax):
        artist = [ax.scatter(self.data[:, 0], self.data[:, 1], **self.options)]
        return artist
