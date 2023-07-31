import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os.path as path
from matplotlib.collections import LineCollection
from matplotlib.patches import Polygon
import matplotlib.animation as animation
from copy import copy

class Visualizer():
    def __init__(self):
        self.points_array = []
        self.line_segments_array = []
        self.polygons_array = []
        self.frames_stamps = []

    def add_points(self, points, color=None):
        points = np.array(points)

        if len(points.shape) >= 2 and points.shape[1:] == (2, ):
            self.points_array.append((points, color))
        else:
            raise ValueError('dimension mismatch')

    def add_line_segments(self, line_segments, color=None):
        line_segments = np.array(line_segments)

        if len(line_segments.shape) >= 2 and line_segments.shape[1:] == (2, 2):
            self.line_segments_array.append((line_segments, color))
        else:
            raise ValueError('dimension mismatch')
        
    def add_polygons(self, polygons, color=None):
        polygons = np.array(polygons)

        if len(polygons.shape) >= 3 and polygons.shape[2:] == (2, ):
            self.polygons_array.append((polygons, color))
        else:
            raise ValueError('dimension mismatch')

    def new_frame(self):
        self.frames_stamps.append((len(self.points_array), len(self.line_segments_array)))

    def make_gif(self, interval=600):
        fig, ax = plt.subplots()

        frame = 0
        frames_count = len(self.frames_stamps)
        points_idx = 0
        lines_idx = 0

        artists = []
        artist_frame = []

        artist_x = ax.set_xlabel('x')
        artist_y = ax.set_ylabel('y')

        artist_frame.append(artist_x)
        artist_frame.append(artist_y)

        while frame < frames_count:
            points_idx_last, lines_idx_last = self.frames_stamps[frame]

            while points_idx < points_idx_last:
                points, color = self.points_array[points_idx]
                points_artist = ax.scatter(points[:, 0], points[:, 1], color=color)
                artist_frame.append(points_artist)
                points_idx += 1

            while lines_idx < lines_idx_last:
                line_segments, color = self.line_segments_array[lines_idx]
                line_collection = LineCollection(line_segments, color=color)
                lines_artist = ax.add_collection(line_collection)
                artist_frame.append(lines_artist)
                lines_idx += 1

            artists.append(copy(artist_frame))
            frame += 1

        self.anim = animation.ArtistAnimation(fig=fig, artists=artists, interval=interval, blit=False)
        plt.show()

    def save_gif(self, filename):
        self.anim.save(filename=filename, writer="pillow")

    def __build_plot(self):
        fig, ax = plt.subplots()

        ax.set_xlabel('x')
        ax.set_ylabel('y')

        for points, color in self.points_array:
            ax.scatter(points[:, 0], points[:, 1], color=color)

        for line_segments, color in self.line_segments_array:
            line_collection = LineCollection(line_segments, color=color)
            ax.add_collection(line_collection)

        for polygons, color in self.polygons_array:
            for polygon in polygons:
                p = Polygon(polygon, color=color, alpha=0.4, zorder=0)
                ax.add_patch(p)

        ax.autoscale()

        return fig, ax

    def show(self):
        fig, _ = self.__build_plot()
        fig.show(warn=False)

    # save information about figure to file of given $file_name
    def save_plot(self, file_name):
        with open(file_name, "w") as file:
            for points, color in self.points_array:
                file.write(color+"\n")
                file.write("".join(f"{p[0]}, {p[1]}\n" for p in points))
            file.write("points_end\n")
            for line_segments, color in self.line_segments_array:
                raise RuntimeError("writing line_segments not implement yet")
                file.write(color)
                file.write(str(line_segments))

    def clear(self):
        self.points_array.clear()
        self.line_segments_array.clear()

    # clear current visualizer and fill it with elements from file of given name
    def open_plot(self, file_name):
        if not path.isfile(file_name):
            raise ValueError(f"{file_name} IS NOT A FILE")
        self.clear()
        with open(file_name, "r") as file:
            readed_color = file.readline()
            while "points_end\n" != readed_color:
                color = readed_color[:-1]
                points = []
                readed_point = file.readline()
                while "," in readed_point:
                    points.append(list(map(float, readed_point.split(","))))
                    readed_point = file.readline()
                self.add_points(points, color=color)
                readed_color = readed_point
            raise RuntimeError("load lines segments not implement yet")
        
    # save plot image to file of given $file_name
    def save_picture(self, file_name):
        fig, _ = self.__build_plot()
        fig.savefig(file_name)
        plt.close()
