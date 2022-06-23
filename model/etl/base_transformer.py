from abc import abstractmethod
from base_etl import ETLComponent


class BaseTransformer(ETLComponent):

    @abstractmethod
    def apply(self, x):
        pass
