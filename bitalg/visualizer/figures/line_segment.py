from .figure import Figure
from matplotlib.collections import LineCollection
import numpy as np


class LineSegment(Figure):
    def __init__(self, data, options):
        data = np.array(data).reshape(-1, 2, 2)
        super().__init__(data, options)

    def draw(self, ax):
        line_collection = LineCollection(self.data, **self.options)
        artist = [ax.add_collection(line_collection)]
        return artist
