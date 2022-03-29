#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

# CONSTANTS
YES_REPLACEMENT = 'yes'
NO_REPLACEMENT = 'no'

def clean_column_name(table):
    table.columns = table.columns.str.lower()
    table.columns = [re.sub('(,)|(:)|(-)', '', x) for x in table.columns]
    table.columns = [re.sub('(_)', ' ', x) for x in table.columns]
    table.columns = [x.strip(' ') for x in table.columns]
    
    # patient id column name normalization
    if 'subject number' in table.columns: 
        table = table.rename(mapper={'subject number': 'patient id'}, axis=1)
    elif 'patient id' in table.columns: 
        table = table.rename(mapper={'patient id': 'patient id'}, axis=1)



def clean_str_column(table):
    for col in table.columns:
        if table[col].dtype == object:
            table[col] = table[col].str.lower()
            table[col] = table[col].str.replace('(,)|(:)|(-)', '', regex=True)
            table[col] = table[col].str.replace('(_)', ' ', regex=True)
            table[col] = table[col].str.strip(' ')


