from .figure import Figure
import numpy as np


class Line(Figure):
    def __init__(self, data, options):
        data = np.array(data).reshape(-1, 2, 2)
        super().__init__(data, options)

    def draw(self, ax):
        artist = []
        for line in self.data:
            artist.append(ax.axline(line[0], line[1], **self.options))
        return artist
