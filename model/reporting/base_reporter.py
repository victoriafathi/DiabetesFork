from abc import ABC, abstractmethod


class BaseReporter(ABC):

    @abstractmethod
    def report_metric(self, metric, value):
        pass
    
    # Add a plot to the report
    @abstractmethod
    def add_plot(self, plot):
        pass
    
    # Report all plots
    @abstractmethod
    def report_plots(self):
        pass
