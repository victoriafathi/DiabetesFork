from abc import ABC, abstractmethod


# Base class for all plots
class BasePlot(ABC):

    @abstractmethod
    def produce_plot(self):
        pass

# Base class for plots which are treated as image files
class ImagePlot(BasePlot):

    @abstractmethod
    def get_filename(self):
        pass
    
    @abstractmethod
    def set_save_directory(self, save_directory):
        pass
