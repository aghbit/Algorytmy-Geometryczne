from .figure import Figure
import numpy as np
from matplotlib.patches import Circle as Circl


class Circle(Figure):
    def __init__(self, data, options):
        data = np.array(data).reshape(-1, 3)
        super().__init__(data, options)

    def draw(self, ax):
        artist = []
        for circle in self.data:
            c = Circl(circle[:2], radius=circle[2], **self.options)
            artist.append(ax.add_patch(c))
        return artist
