import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython.display import Image
import os


class Plot:
    @staticmethod
    def __build_plot(plot_data, data):
        fig, ax = plt.subplots()
        ax.set_xlabel('x')
        ax.set_ylabel('y')

        if 'title' in plot_data:
            ax.set_title(plot_data['title'])
        if 'grid' in plot_data:
            ax.grid()

        for figure in data:
            figure.draw(ax)
        ax.autoscale()
        return fig, ax

    @staticmethod
    def __build_gif(plot_data, data, interval):
        fig, ax = plt.subplots()
        artists = []
        frames = [ax.set_xlabel('x'), ax.set_ylabel('y')]
        artists.append(frames[:])

        if 'title' in plot_data:
            ax.set_title(plot_data['title'])
        if 'grid' in plot_data:
            ax.grid()

        for figure in data:
            artist = figure.draw(ax)
            frames.extend(artist)
            artists.append(frames[:])
        ax.autoscale()
        return animation.ArtistAnimation(fig=fig, artists=artists, interval=interval, blit=True)

    @staticmethod
    def show(plot_data, data):
        fig, _ = Plot.__build_plot(plot_data, data)
        fig.show(warn=False)

    @staticmethod
    def save(plot_data, data, filename):
        fig, _ = Plot.__build_plot(plot_data, data)
        fig.savefig(filename)
        plt.close()

    @staticmethod
    def show_gif(plot_data, data, interval):
        Plot.save_gif(plot_data, data, interval,
                      f'{__file__}.__tmp_animation_holder__')
        plt.close()
        gif = Image(f'{__file__}.__tmp_animation_holder__.gif')
        os.remove(f'{__file__}.__tmp_animation_holder__.gif')
        return gif

    @staticmethod
    def save_gif(plot_data, data, interval, filename):
        anim = Plot.__build_gif(plot_data, data, interval)
        anim.save(filename=f'{filename}.gif', writer='pillow')
        plt.close()
