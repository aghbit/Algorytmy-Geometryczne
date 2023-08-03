import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.collections import LineCollection
from matplotlib.patches import Polygon
import matplotlib.animation as animation
from copy import copy
from IPython.display import Image

from bitalg.visualizer.objects.Point import Point

Number = int | float
PointType = list[Number] | tuple[Number]

class Visualizer:
    def __init__(self):        
        self.data = []

    def add_point(self, x: Number, y: Number, **kwargs) -> None:
        '''
        Args:
            x: first coordinate
            y: second coordinate
            **kwargs: options
                examples:
                    color="red" - color
                    alpha=0.5 - opacity
                    linewidth=5 - size
        '''
        obj = Point((x, y), kwargs)
        self.data.append(obj)
        
    def __build_plot(self):
        fig, ax = plt.subplots()

        ax.set_xlabel('x')
        ax.set_ylabel('y')

        for obj in self.data:
            obj.add_to_plot(ax)
        
        ax.autoscale()

        return fig, ax

    def show(self):
        fig, _ = self.__build_plot()
        fig.show(warn=False)