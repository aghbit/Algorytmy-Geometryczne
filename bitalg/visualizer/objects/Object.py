from abc import ABC, abstractmethod

class Object(ABC):
    def __init__(self, data, options):
        self.data = data
        self.options = options

    @abstractmethod
    def add_to_plot(self, ax):
        pass


