from .figure import Figure
import numpy as np
from matplotlib.lines import Line2D
from matplotlib.transforms import Bbox, BboxTransformTo


class AxLine(Line2D):
    def __init__(self, xy1, xy2, **kwargs):
        super().__init__([0, 1], [0, 1], **kwargs)
        self._xy1 = xy1
        self._xy2 = xy2

    def get_transform(self):
        ax = self.axes
        points_transform = self._transform - ax.transData + ax.transScale

        (x1, y1), (x2, y2) = \
            points_transform.transform([self._xy1, self._xy2])
        dx = x2 - x1
        dy = y2 - y1
        if np.allclose(x1, x2):
            if np.allclose(y1, y2):
                raise ValueError(
                    f"Cannot draw a line through two identical points "
                    f"(x={(x1, x2)}, y={(y1, y2)})")
            slope = np.inf
        else:
            slope = dy / dx

        (vxlo, vylo), (vxhi, vyhi) = ax.transScale.transform(ax.viewLim)
        if np.isclose(slope, 0):
            start = vxlo, y1
            stop = vxhi, y1
        elif np.isinf(slope):
            start = x1, vylo
            stop = x1, vyhi
        else:
            _, start, stop, _ = sorted([
                (vxlo, y1 + (vxlo - x1) * slope),
                (vxhi, y1 + (vxhi - x1) * slope),
                (x1 + (vylo - y1) / slope, vylo),
                (x1 + (vyhi - y1) / slope, vyhi),
            ])

        # handling half line
        if x1 < x2:
            start = (x1, y1)
        elif x1 > x2:
            stop = (x1, y1)
        elif y1 < y2:
            start = (x1, y1)
        elif y1 > y2:
            stop = (x1, y1)

        return (BboxTransformTo(Bbox([start, stop]))
                + ax.transLimits + ax.transAxes)


def axline(ax, xy1, xy2, **kwargs):
    datalim = [xy1] if xy2 is None else [xy1, xy2]
    if "transform" in kwargs:
        datalim = []
    line = AxLine(xy1, xy2, **kwargs)
    ax.add_line(line)
    ax.update_datalim(datalim)
    return line


class HalfLine(Figure):
    def __init__(self, data, options):
        data = np.array(data).reshape(-1, 2, 2)
        super().__init__(data, options)

    def draw(self, ax):
        artist = []
        for half_line in self.data:
            artist.append(ax.scatter(*half_line[0], s=1e-8, color='white', alpha=0))
            artist.append(
                axline(ax, half_line[0], half_line[1], **self.options))
        return artist
