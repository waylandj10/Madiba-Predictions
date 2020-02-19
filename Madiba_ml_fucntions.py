from __future__ import absolute_import, division, print_function, unicode_literals

import pandas as pd
import pathlib
import datetime
import plotly.express as px

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns



def configure_csv(data_filepath,header_filepath,metrics):
    cols = pd.read_csv(header_filepath,names='H',dtype=str)['H'].unique()
    df = pd.read_csv(data_filepath,names=cols,delimiter=';',low_memory=False)
    metric_df = df[df['0SMD_MENA'].isin(metrics)].sort_values(by='0SMD_TIHM',ignore_index=True)
    metric_df['TIMESTAMP'] = [datetime.datetime.strptime(str(x),'%Y%m%d%H%M%S') for x in metric_df['0SMD_TIHM']]
    metric_df = metric_df[metric_df['0SMD_LUID'].notna()][['0SMD_LUID','0SMD_MENA','0SMD_MUNI','0SMD_MAX','0CALDAY','TIMESTAMP']]
    return metric_df
    

def choose_metrics(df,metrics):
    """ Filter for a list of metrics,and return a df with time-ordered, 
    non-null values across all all systems. This will serve as the 
    training set for the predictions of a single system."""
    filtered_df = df[df['0SMD_MENA'].isin(metrics)]
    return filtered_df

def choose_LUIDs(df,LUIDs):
    system_df = df[df['0SMD_LUID'].isin(LUIDs)]
    metrics = df[['0SMD_MENA','0SMD_MUNI']].apply(tuple, axis=1).unique()
    print(f"The following dataframe tracks {LUIDs} and the following metrics are recorded: {[x[0] for x in metrics]}")
    return system_df,metrics








#units = {item[1] for item in metrics}
#create plots for each metric, seperated by units
#for unit in units: 
   # for metric in metric:
   #     if metric[1] == unit:
   #         splice = choose_metric(system_df,metric[0])
   #         fig.add_trace(go.Scatter(x=splice['TIMESTAMP'], y=splice['0SMD_MAX'],mode='lines+markers',name=metric[0]))
   # fig.show()




