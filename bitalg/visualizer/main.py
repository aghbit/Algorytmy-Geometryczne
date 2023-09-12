from .figures.point import Point
from .figures.line_segment import LineSegment
from .figures.circle import Circle
from .figures.polygon import Polygon
from .figures.line import Line
from .figures.half_line import HalfLine
from .plot.plot import Plot


class Visualizer:
    def __init__(self):
        self.data = []
        self.plot_data = {}

    def add_title(self, title):
        self.plot_data['title'] = title

    def add_grid(self):
        self.plot_data['grid'] = True

    def add_point(self, data, **kwargs):
        point = Point(data, kwargs)
        self.data.append(point)
        return point

    def add_line_segment(self, data, **kwargs):
        line_segment = LineSegment(data, kwargs)
        self.data.append(line_segment)
        return line_segment

    def add_circle(self, data, **kwargs):
        circle = Circle(data, kwargs)
        self.data.append(circle)
        return circle

    def add_polygon(self, data, **kwargs):
        polygon = Polygon(data, kwargs)
        self.data.append(polygon)
        return polygon

    def add_line(self, data, **kwargs):
        line = Line(data, kwargs)
        self.data.append(line)
        return line

    def add_half_line(self, data, **kwargs):
        semi_line = HalfLine(data, kwargs)
        self.data.append(semi_line)
        return semi_line

    def remove_figure(self, figure):
        figure.to_be_removed = True
        self.data.append(figure)

    def clear(self):
        self.data = []
        self.plot_data = {}

    def show(self):
        Plot.show(self.plot_data, self.data)

    def save(self, filename='plot'):
        Plot.save(self.plot_data, self.data, filename)

    def show_gif(self, interval=256):
        gif = Plot.show_gif(self.plot_data, self.data, interval)
        return gif

    def save_gif(self, filename='animation', interval=256):
        Plot.save_gif(self.plot_data, self.data, interval, filename)
