#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries
import argparse
import pandas as pd
import pickle
import re
import numpy as np
import cleaning_module as cleaning


# Constants
default_filepath = "../data/cerebral_perfusion_data/data_description/GE-75_data_summary_table.csv"


# Arguments
parser = argparse.ArgumentParser(description='data cleaning arguments for the perfusion dataset')
parser.add_argument('--path', '-p', type=str, required=False, default=default_filepath,
                    help='filepath to the perfusion dataset [default:../data/cerebral_perfusion_data/data_description/GE-75_data_summary_table.csv]')
parser.add_argument('--output', '-o', type=str, required=False, default='output.csv',
                    help='[default: output.csv]')
parser.add_argument('--threshold', '--t', required=False, type=float, default=(2/3), help='keep column with t-percentage of non missing value, drop otherwise, [default: 2/3')
parser.add_argument('-v', '--verbose', required=False, action="store_true", help='Talk a lot.')

args = parser.parse_args()


# Data Loading
pickle_in = open("perfusion_dict.pkl","rb")
perfusion_dict = pickle.load(pickle_in)

df = pd.read_csv(args.path)

# Cleaning

##  String cleaning
if args.verbose:
    print('String cleaning')
cleaning.clean_column_name(df)
cleaning.clean_str_column(df)

## MRI features Filter
if args.verbose:
    print('MRI features Filter')
df.drop(labels=perfusion_dict["brain_measures"], axis="columns", inplace=True)

## Bio measures Filter
if args.verbose:
    print('Bio measures Filter')
df.drop(labels=perfusion_dict["bio_measures"], axis="columns", inplace=True)

## Cognitives Tests Filter
if args.verbose:
    print('Cognitive Tests Filter')
df.drop(labels=perfusion_dict["cognitive_tests"], axis="columns", inplace=True)

## Irrelevant features Filter
if args.verbose:
    print('Medications Filter')
df.drop(labels=perfusion_dict["irrelevant_features"], axis="columns", inplace=True)

## Inconsistency
### patients annotated with and without diabetes
dm_history =  df[df["dm patient medical history"] == 'yes']['patient id']
dm_group = df[df['group']=='dm']['patient id']
inconsistent_patient = dm_group[~dm_group.isin(list(dm_history))]
df.drop(labels=inconsistent_patient.index, axis='index', inplace=True)


### spelling
unknown = re.compile("(unknown)")
no = re.compile("(^no$)|(^n$)")
yes = re.compile("(^yes$)|(^y$)|(^ye$)")
latino = re.compile("(non h/l)|(nonh/l)")
typo = re.compile("(^h/$)|(ch)")
df = df.replace(to_replace = {yes:cleaning.YES_REPLACEMENT, 
                              no: cleaning.NO_REPLACEMENT, 
                              unknown: np.nan,
                              latino: 'non h/l',
                              typo: np.nan}, 
                              regex=True)

### wrong column type
df["dm family history"] = pd.to_numeric(df["dm family history"], errors='ignore', downcast='integer')


## Redundancy 
if args.verbose:
    print('Redundancy')
df.drop(labels=['group', 'dm patient medical history'], axis='columns', inplace=True)
df.rename(mapper={'dm nondm stroke':'diabetes'}, axis=1, inplace=True)


df["dm family history"] = pd.to_numeric(df["dm family history"], errors='ignore', downcast='integer')
## Missing value
if args.verbose:
    print('Missing value')
thresh = args.threshold
df = df.dropna(thresh=len(df)*thresh, axis='columns')


# Write file
df.to_csv(args.output, index=False, encoding='utf-8')
print("file written")