from .figure import Figure
import numpy as np
from matplotlib.patches import Polygon as Polygo


class Polygon(Figure):
    def __init__(self, data, options):
        data = data[:]
        multiple_polygons = False
        for i in range(len(data)):
            if np.array(data[i]).shape != (2, ):
                multiple_polygons = True
                break
        if multiple_polygons:
            for i in range(len(data)):
                data[i] = np.array(data[i])
        else:
            data = np.array(data).reshape(1, -1, 2)
        super().__init__(data, options)

    def draw(self, ax):
        artist = []
        for polygon in self.data:
            p = Polygo(polygon, **self.options)
            artist.append(ax.add_patch(p))
        return artist
