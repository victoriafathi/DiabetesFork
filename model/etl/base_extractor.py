from abc import abstractmethod
from base_etl import ETLComponent

class BaseExtractor(ETLComponent):

    @abstractmethod
    def extract(self):
        pass
