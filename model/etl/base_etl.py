from abc import ABC, abstractmethod


# Base class for all classes in ETL pipeline to enable accurate logging
class ETLComponent(ABC):

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_params(self):
        pass

# Base class for ETL pipelines
class BaseETL(ETLComponent):

    # Loads one case in model compatible format
    @abstractmethod
    def _load_case(self, case):
        pass

# Base class for simple ETL pipelines that load one stream of data
class SimpleETL(BaseETL):

    @abstractmethod
    def load(self):
        pass

# Base class for ETL pipelines that load traning and validation data streams
class BaseTrainValidationETL(BaseETL):

    @abstractmethod
    def load_train(self):
        pass

    @abstractmethod
    def load_validation(self):
        pass

# Base class for ETL pipelines that perform cross-validation
class CrossValidationETL(BaseETL):

    @abstractmethod
    def get_folds(self):
        pass
    
    @abstractmethod
    def load_data(self, fold):
        pass
