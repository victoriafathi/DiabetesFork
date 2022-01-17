from abc import ABC, abstractmethod


class BaseMetric(ABC):

    @abstractmethod
    def evaluate(self, prediction, ground_truth):
        pass

    @abstractmethod
    def get_name(self):
        pass
