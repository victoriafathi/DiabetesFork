#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def column_name_cleaning(table):
    table.columns = table.columns.str.lower()
    table.columns = [re.sub('(,)|(:)|(-)', '', x) for x in table.columns]
    table.columns = [re.sub('(_)', ' ', x) for x in table.columns]
    table.columns = [x.strip(' ') for x in table.columns]
    
    # patient id column name normalization
    if 'subject number' in table.columns: 
        table = table.rename(mapper={'subject number': 'patient id'}, axis=1)
    elif 'patient id' in table.columns: 
        table = table.rename(mapper={'patient id': 'patient id'}, axis=1)



def str_column_cleaning(table):
    for col in table.columns:
        if table[col].dtype == object:
            table[col] = table[col].str.lower()
            table[col] = table[col].str.replace('(,)|(:)|(-)', '', regex=True)
            table[col] = table[col].str.replace('(_)', ' ', regex=True)
            table[col] = table[col].str.strip(' ')


if __name__ == "__main__":
