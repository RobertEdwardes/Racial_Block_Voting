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


def block_classification(df):
    df['Target_Percentage'] = df['Target_Pop']/df['Base_Pop']
    df['Group'] = None
    df = df.reset_index(drop=True)

    for i ,row in df.iterrows():
        if row['Target_Percentage'] >= .9:
            df['Group'].iloc[i] = 'T90%'
        if row['Target_Percentage'] < .9:
            df['Group'].iloc[i] = 'T60%'
        if row['Target_Percentage'] < .6:
            df['Group'].iloc[i] = 'N50%'
        if row['Target_Percentage'] <= .4:
            df['Group'].iloc[i] = 'O60%'
        if row['Target_Percentage'] <= .1:
            df['Group'].iloc[i] = 'O90%'
    quoat = df[['Party_A','Party_B']].sum()
    quoat = (quoat['Party_B'] + quoat['Party_A'])/2
    voteGroups = df[['Group','Party_B']].groupby('Group').sum().reset_index()
    voteGroups = voteGroups.values.tolist()
    return voteGroups, quoat


def bpi(group, quoat):
    idx = 0
    output = {}
    for i in range(1,len(group)+1):
        for j in itertools.combinations(group,i):
            c = 0
            for k in j:
                c += k[1]
                if c > quoat:
                    idx += 1
                    output[idx] = {}
                    output[idx]['Coliltion'] = j
                    output[idx]['Total'] = c
                    break
    crit_count = {'T90%':0,'T60%':0,'O90%':0,'O60%':0,'N50%':0}
    for key, value in output.items():
        wC = value['Total']
        for i in value['Coliltion']:
            if wC - i[1] < quoat:
                crit_count[i[0]] += 1
    df_share = pd.DataFrame(list(crit_count.items()),columns = ['Cat','T_Index'])
    B_IdxSum = df_share['T_Index'].sum()
    df_share['T_PowerShare'] = (df_share['T_Index']/B_IdxSum) * 100
    df_share['T_Critical_Vote'] = (df_share['T_Index']/(2**(5-1)))*100
    # NEEDS OUTPUT 


def ssi(group, quoat):
    output = {'B90%':0,'B60%':0,'W90%':0,'W60%':0,'N50%':0}
    for i in itertools.permutations(voteGroups):
        c = 0
        for j in i:
            c += j[1]
            if c > quoat:
                output[j[0]] += 1
                break
    df_share = pd.DataFrame(list(output.items()),columns = ['Cat','T_Count'])
    factorial = math.factorial(len(output.keys()))
    df_share['T_Index'] = df_share['T_Count']/factorial
    # NEEDS OUTPUT 


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
        if collections.Counter(df.columns) != collections.Counter(list(schema.keys())):
            Exception raise('Schema does not match Dataframe columns call PACKAGE_NAME.template for example.')
        df = df.rename(columns=schema)
        group, quoat = block_classification(df)
        if index is None or index == 'Banzhaf':
            bpi(group, quoat)
        if index is None or index == 'Shubik':
            ssi(group, quoat)