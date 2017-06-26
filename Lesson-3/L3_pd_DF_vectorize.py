#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 15:25:05 2017

@author: dhingratul
"""

import pandas as pd

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)


def standardize(df):
    '''
    Fill in this function to standardize each column of the given
    DataFrame. To standardize a variable, convert each value to the
    number of standard deviations it is above or below the mean.

    This time, try to use vectorized operations instead of apply().
    You should get the same results as you did before.
    '''
    pd_mean = df.mean()
    pd_std = df.std(ddof=0)
    out = (df - pd_mean) / pd_std
    return out


def standardize_rows(df):
    '''
    Optional: Fill in this function to standardize each row of the given
    DataFrame. Again, try not to use apply().

    This one is more challenging than standardizing each column!
    '''
    pd_mean = df.mean('columns')
    pd_std = df.std('columns', ddof=0)
    out_inter = df.subtract(pd_mean, 'index')
    out = out_inter.div(pd_std, 'index')
    return out

# Driver
print(standardize(grades_df))
