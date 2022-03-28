#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Libraries
import argparse
import pandas as pd
import cleaning_module as cleaning

# Constants
default_filepath = "../data/cerebral_perfusion_data/data_description/GE-75_data_summary_table.csv"


# Arguments
parser = argparse.ArgumentParser(description='data cleaning arguments for the perfusion dataset')
parser.add_argument('--path', '-p', type=str, required=False, default=default_filepath,
                    help='filepath to the perfusion dataset [default:../data/cerebral_perfusion_data/data_description/GE-75_data_summary_table.csv]')
parser.add_argument('-v', '--verbose', required=False, action="store_true", help='Talk a lot.')
args = parser.parse_args()


# Data Loading
df = pd.read_csv(args.path)


# Cleaning

##  String cleaning
if args.verbose:
    print('String cleaning')

## MRI features Filter
if args.verbose:
    print('MRI features Filter')

## Bio measures Filter
if args.verbose:
    print('Bio measures Filter')

## Medications Filter
if args.verbose:
    print('Medications Filter')


## Redundancy 
if args.verbose:
    print('Redundancy')

## Missing value
if args.verbose:
    print('Missing value')

