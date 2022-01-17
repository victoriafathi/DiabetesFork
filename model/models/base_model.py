from abc import ABC, abstractmethod


class BaseModel(ABC):

    @abstractmethod
    def predict(self, x):
        pass

    @abstractmethod
    def fit(self, data):
        pass

    @abstractmethod
    def get_name(self):
        pass
