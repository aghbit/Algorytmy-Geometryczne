import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.collections import LineCollection
from matplotlib.patches import Polygon
import matplotlib.animation as animation
from copy import copy
from IPython.display import Image

from bitalg.visualizer.types import Number, PointType

class Object():
    def __init__(self, type, data, options):
        self.type = type
        self.data = data
        self.options = options

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
        obj = Object('Point', (x, y), kwargs)
        self.data.append(obj)

    def add_line_segment(self, c1: PointType, c2: PointType, **kwargs) -> None:
        '''
        Args:
            c1: (x, y) - line segment begining coordinates 
            c2: (x, y) - line segment ending coordinates 
            **kwargs: options
                examples:
                    color="red" - color
                    alpha=0.5 - opacity
                    linewidth=5 - size
        '''
        obj = Object('Line_segment', (c1, c2), kwargs)
        self.data.append(obj)
        
    def add_polygon(self, polygon: list[PointType] | tuple[PointType], **kwargs) -> None:
        '''
        Args:
            polygon: list of points representing consecutive vertices
            **kwargs: options
                examples:
                    color="red" - color
                    alpha=0.5 - opacity
                    linewidth=5 - size
        '''
        polygon = np.array(polygon)

        if len(polygon.shape) >= 2 and polygon.shape[1:] == (2, ):
            obj = Object('Polygon', polygon, kwargs)
            self.data.append(obj)
        else:
            raise ValueError('dimension mismatch')
        
    def __build_plot(self):
        fig, ax = plt.subplots()

        ax.set_xlabel('x')
        ax.set_ylabel('y')

        for obj in self.data:
            if obj.type == 'Point':
                ax.scatter([obj.data[0]], [obj.data[1]], **obj.options)
            elif obj.type == 'Line_segment':
                line_collection = LineCollection([obj.data], **obj.options)
                ax.add_collection(line_collection)
            elif obj.type == 'Polygon':
                p = Polygon(obj.data, **obj.options)
                ax.add_patch(p)
        
        ax.autoscale()

        return fig, ax

    def show(self):
        fig, _ = self.__build_plot()
        fig.show(warn=False)

    # save plot image to file of given $file_name
    def save_picture(self, file_name='plot'):
        fig, _ = self.__build_plot()
        fig.savefig(file_name)
        plt.close()

    # Begin Important:
    # refactored this section
    # to better match workflow used
    # when showing and saving a picture
    # additinaly with this changed architecture
    # you dont need to explicitly call .new_frame()
    # after each update 
    # now just call save_gif/show_gif
    #
    # corresponding:
    # save_gif <-> save_picture
    # show_gif <-> show

    def __build_gif(self, interval=256):
        fig, ax = plt.subplots()

        artists = []
        artist_frame = []

        artist_frame.append(ax.set_xlabel('x'))
        artist_frame.append(ax.set_ylabel('y'))

        for obj in self.data:
            if obj.type == 'Point':
                obj_artist = ax.scatter([obj.data[0]], [obj.data[1]], **obj.options)
            elif obj.type == 'Line_segment':
                line_collection = LineCollection([obj.data], **obj.options)
                obj_artist = ax.add_collection(line_collection)
            elif obj.type == 'Polygon':
                p = Polygon(obj.data, **obj.options)
                obj_artist = ax.add_patch(p)

            ax.autoscale()
            artist_frame.append(obj_artist)
            artists.append(copy(artist_frame))

        return animation.ArtistAnimation(fig=fig, artists=artists, interval=interval, blit=False)

    def save_gif(self, filename='animation', interval=128):
        anim = self.__build_gif(interval)
        anim.save(filename=f'{filename}.gif', writer="pillow")
        plt.close()
    
    def show_gif(self, interval=128):
        self.save_gif(f'{__file__}.__tmp_animation_holder__', interval)
        plt.close()
        img = Image(f'{__file__}.__tmp_animation_holder__.gif')
        os.remove(f'{__file__}.__tmp_animation_holder__.gif')
        return img
    
    # end Important



    # Begin Important:
    # in this implementation saving plots should be rewritten we are using **kwargs
    # and passing them down 
    # there is a neat way to do it using pickle library
    #
    # to do:
    # 
    # save_to_pickle file
    # read_from_pickle file

    # save information about figure to file of given $file_name
    def save_plot(self, file_name):
        with open(file_name, "w") as file:
            for points, color in self.points:
                file.write(str(color)+"\n")
                file.write("".join(f"{p[0]}, {p[1]}\n" for p in points))
            file.write("end\n")
            for line_segments, color in self.line_segments:
                file.write(str(color)+"\n")
                file.write("".join(f"{p1[0]}, {p1[1]}; {p2[0]}, {p2[1]}\n" for p1, p2 in line_segments))
            file.write("end\n")
            for polygons, color in self.polygons:
                file.write(str(color)+"\n")
                for polygon in polygons:
                    file.write("".join(f"{px[0]}, {px[1]}; "for px in polygon)[:-2] + "\n")
            file.write("end\n")


    # convert string of format "a, b" into list float[a, b]
    def __read_point(self, line):
        return list(map(float, line.split(",")))

    # clear current visualizer and fill it with elements from file of given name
    def open_plot(self, file_name):
        if not os.path.isfile(file_name):
            raise ValueError(f"{file_name} IS NOT A FILE")
        self.clear()
        with open(file_name, "r") as file:
            readed_color = file.readline()

            # points
            while "end\n" != readed_color:
                color = readed_color[:-1]
                if color == "None": color = None
                points = []
                readed_point = file.readline()
                while "," in readed_point:
                    points.append(self.__read_point(readed_point))
                    readed_point = file.readline()
                self.add_points(points, color=color)
                readed_color = readed_point
            readed_color = file.readline()

            # lines_segments
            while "end\n" != readed_color:
                color = readed_color[:-1]
                if color == "None": color = None
                lines_segments = []
                readed_line = file.readline()
                while ";" in readed_line:
                    lines_segments.append([self.__read_point(point_str) for point_str in readed_line.split(";")])
                    readed_line = file.readline()
                self.add_line_segments(lines_segments, color=color)
                readed_color = readed_line
            readed_color = file.readline()

            # polygons
            while "end\n" != readed_color:
                color = readed_color[:-1]
                if color == "None": color = None
                polygons = []
                readed_polygon = file.readline()
                while ";" in readed_polygon:
                    polygons.append([self.__read_point(point_str) for point_str in readed_polygon.split(";")])
                    readed_polygon = file.readline()
                self.add_polygons(polygons, color=color)
                readed_color = readed_polygon
        
    # end Important



    # Begin Important:
    # clearning might not be usefull
    # if one decides to clean the plot it be done
    # by reinitializing Visualizer:
    # vis = Visualizer()

    # clear all elements that can by showed by methode self.show()
    def clear_data(self):
        self.points.clear()
        self.line_segments.clear()
        self.polygons.clear()

    # clear all frames that can be showed by self.make_gif()
    def clear_frames(self):
        self.frames_stamps.clear()

    # end Important
