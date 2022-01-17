from abc import abstractmethod
from .. import ETLComponent


class BaseTransformer(ETLComponent):

    @abstractmethod
    def apply(self, x):
        pass
