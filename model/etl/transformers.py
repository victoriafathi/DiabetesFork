from filecmp import dircmp
import os
import pandas as pd
import re

from base_transformer import BaseTransformer
from extractors import CSVExtractor



class CSVTransformer(BaseTransformer):
    def __init__(self, dir):
        self.extractor = CSVExtractor(dir)
        self.data = self.extractor.extract()
    
    def drop_na(self): 
        self.data.dropna(inplace=True)
    
    def clean_column_name(self):
        self.data.columns = self.data.columns.str.lower()
        self.data.columns = [re.sub('(,)|(:)|(-)', '', x) for x in self.data.columns] #remove special character
        self.data.columns = [re.sub('(_)', ' ', x) for x in self.data.columns] #replace underscore by space
        self.data.columns = [x.strip(' ') for x in self.data.columns] #remove space at the beginning and end
    
    def clean_str_column(self):
        for col in self.data.columns:
            if self.data[col].dtype == object:
                self.data[col] = self.data[col].str.lower()
                self.data[col] = self.data[col].str.replace('(,)|(:)|(-)', '', regex=True)
                self.data[col] = self.data[col].str.replace('(_)', ' ', regex=True)
                self.data[col] = self.data[col].str.strip(' ')

    

