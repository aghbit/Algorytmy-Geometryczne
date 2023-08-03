from bitalg.visualizer.objects.Object import Object

class Point(Object):
    def __init__(self, data, options):
        super().__init__(data, options)
    
    def add_to_plot(self, ax):
        ax.scatter([self.data[0]], [self.data[1]], **self.options)