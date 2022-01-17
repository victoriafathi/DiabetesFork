from abc import abstractmethod
from .. import ETLComponent


class BaseExtractor(ETLComponent):

    @abstractmethod
    def extract(self):
        pass
