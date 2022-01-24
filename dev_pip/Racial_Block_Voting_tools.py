'''
Analysis poltical geogrpahies to determin if there is Racial Polirizing Voting

Usage:
--------------
PARAMETERS: 

OUTPUT:
    Default: {Index-Type}.csv 
        option: filename = {filename}-{Index-Type}.csv

'''


import pandas as pd
import matplotlib.pyplot as plt
import os 
import numpy as np
import statsmodels.api as sm
import logging

def Homogeneous_Precinct(df, idx, MajorityPopCol, MinorityPopCol, TotalPopCol, Party1, Party2):
    if len(df.index) < 2:
        raise Exception('Dataframe needs 2 or more rows to compare')
    df['Minority_Percentage'] = df[MinorityPopCol]/df[TotalPopCol]
    df['Majority_Percentage'] = df[MajorityPopCol]/df[TotalPopCol]
    df['Group'] = None
    df = df.reset_index(drop=True)

    for i ,row in df.iterrows():
        if row['Minority_Percentage'] >= .9:
            df['Group'].iloc[i] = 'T0%'
        if row['Minority_Percentage'] < .9:
            df['Group'].iloc[i] = 'T60%'
        if row['Minority_Percentage'] < .6:
            df['Group'].iloc[i] = 'N50%'
        if row['Minority_Percentage'] <= .4:
            df['Group'].iloc[i] = 'O60%'
        if row['Minority_Percentage'] <= .1:
            df['Group'].iloc[i] = 'O90%'

    Min_df = df[[idx,'Minority_Percentage',Party2,Party1,TotalPopCol, MinorityPopCol]][(df['Group'] == 'T60%') | (df['Group'] == 'T90%')]
    Maj_df = df[[idx,'Majority_Percentage',Party2,Party1,TotalPopCol, MajorityPopCol]][(df['Group'] == 'O60%') | (df['Group'] == 'O90%')]
    Min_df['Minor_PartyTotal'] = Min_df[Party2] + Min_df[Party1]
    Maj_df['Major_PartyTotal'] = Maj_df[Party2] + Maj_df[Party1]
    Min_df[f'{Party2}_Percentage'] = Min_df[Party2] /(Min_df[Party2] + Min_df[Party1])
    Min_df[f'{Party1}_Percentage'] = Min_df[Party1] /(Min_df[Party2] + Min_df[Party1])
    Maj_df[f'{Party2}_Percentage'] = Maj_df[Party2] /(Maj_df[Party2] + Maj_df[Party1])
    Maj_df[f'{Party1}_Percentage'] = Maj_df[Party1] /(Maj_df[Party2] + Maj_df[Party1])
    Min_df['TurnOut_Percentage'] = Min_df[MinorityPopCol]/(Min_df[Party2] + Min_df[Party1])
    Maj_df['TurnOut_Percentage'] = Maj_df[MajorityPopCol]/(Maj_df[Party2] + Maj_df[Party1])
    df_out = pd.concat([Maj_df,Min_df])
    df_out.to_csv('Homogeneous_Precinct.csv',index=False)


def Ecological_Regression(df, TotalPopCol, TargetPopCol, Party1, Party2):
    if len(df.index) < 2:
        raise Exception('Dataframe needs 2 or more rows to compare')
    df['Target_Percentage'] = df[TargetPopCol]/df[TotalPopCol] 
    df['Vote_Percentage'] = df[Party1]/(df[Party2] + df[Party1])
    x = df[['Vote_Percentage']]
    y = df['Target_Percentage']
    x = sm.add_constant(x)
    model = sm.OLS(y, x).fit()
    plt.rc('figure', figsize=(12, 7))
    plt.text(0.01, 0.05, str(model.summary()), {'fontsize': 10}, fontproperties = 'monospace') 
    plt.axis('off')
    plt.tight_layout()
    plt.savefig('Ecological_Regression.png')
    fig = plt.figure(figsize=(12,8))
    fig = sm.graphics.plot_regress_exog(model, 'Vote_Percentage', fig=fig)
    fig.savefig('regress_plot.png')
    res = model.resid
    fig = sm.qqplot(res, fit=True, line="45")
    fig.savefig('qqplot.png')