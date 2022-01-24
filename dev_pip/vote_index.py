'''
Compute voter power index for 2 party vote using either Banzhaf or Shapley–Shubik mehods

Usage:
--------------
INPUT: Dataframe and Schema
    Schema: JSON/Dict mapping of columns to Schema template 
    DataFrame: 5 columns following Schema JSON idx,Pop_a,Pop_B,Party_1,Party_2

PARAMETERS: Dataframes, Schema, Power Index
    Dataframes: One(1) or more dataframes in a list


'''
import pandas as pd
import os 
import itertools
import math
import collections 
import logging

logging.basicConfig(filename='power_index_debug.txt' level=logging.DEBUG, format=' %(asctime) - %(levelname)s - %(message)s')

def template:

    template = {'(REPLACE WITH Index/Precinct column Name)':'idx',
                '(REPLACE WITH White/Base Population column Name)':'Base_Pop', 
                '(REPLACE WITH Target Population column Name)':'Target_Pop',
                '(REPLACE WITH Party A Vote column Name)':'Party_A',
                '(REPLACE WITH Party A Vote column Name)': 'Party_B'}

    return template


def bpi(df):
    


def ssi(df):
    


def power_index(schema, index=None, init*):
    if len(init) < 1 or schema is None:
            Exception raise('Missing Dataframe or Schema')
    if len(init) == 1:
        df_init.append(df)
    else:
        df_init = init
    for df in df_init:
        if len(df.index) < 2:
            Exception raise('Dataframe needs 2 or more rows to compare')
        if len(df.column) != 5:
            Exception raise('Too few or many columns must be five(5) use template as guide')
        if collections.Counter(df.columns) == collections.Counter(list(schema.keys())):
            Exception raise('Schema does not match Dataframe columns call PACKAGE_NAME.template for examole.')
        df = df.rename(columns=schema)
        if index is None or index == 'Banzhaf':
            bpi(df)
        if index is None or index == 'Shubik':
            ssi(df)