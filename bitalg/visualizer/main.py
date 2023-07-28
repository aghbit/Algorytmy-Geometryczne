import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
import matplotlib.animation as animation
from copy import copy

class Visualizer():
    def __init__(self):
        self.points_array = []
        self.line_segments_array = []
        self.frames_stamps = []

    def add_points(self, points, color=None):
        self.points_array.append((points, color))

    def add_line_segments(self, line_segments, color=None):
        self.line_segments_array.append((line_segments, color))

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
                points = np.array(points)
                points_artist = ax.scatter(points[:, 0], points[:, 1], color=color)
                artist_frame.append(points_artist)
                points_idx += 1

            while lines_idx < lines_idx_last:
                line_segments, color = self.line_segments_array[lines_idx]
                line_segments = np.array(line_segments)
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
            points = np.array(points)
            ax.scatter(points[:, 0], points[:, 1], color=color)

        for line_segments, color in self.line_segments_array:
            line_segments = np.array(line_segments)
            line_collection = LineCollection(line_segments, color=color)
            ax.add_collection(line_collection)

        ax.autoscale()

        return fig, ax

    def show(self):
        fig, _ = self.__build_plot()
        fig.show(warn=False)

    # save informations about points and line segments of current Visualizer in file of given name $file_name
    def save_plot(self, file_name):
        with open(file_name, "w") as file:
            file.write("points\n")
            for points, color in self.points_array:
                file.write(color)
                file.write(points)
            file.write("\nline_segments\n")
            for line_segments, color in self.line_segments_array:
                file.write(color)
                file.write(line_segments)

    def _clear(self):
        self.points_array.clear()
        self.line_segments_array.clear()

    # clear current visualizer and fill it with elements from file of given name
    def open_plot(self, file_name):
        self._clear()
        with open(file_name, "r") as file:
            raise RuntimeError("not implement yet")
