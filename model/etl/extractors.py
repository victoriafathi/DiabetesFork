import os
import pandas as pd
from base_extractor import BaseExtractor


class CSVExtractor(BaseExtractor):
    '''
    Extract CSV files from directory as pandas dataframes
    '''

    def __init__(self, dir):
        self.dir = dir

    def extract(self):
        try:
            return pd.read_csv(self.dir)
        except FileNotFoundError:
            print(f"No csv file available in {self.dir}")
    
    def get_name(self):
        return "csv extractor"
    
    def get_params(self):
        return {
            "dir": self.dir
        }