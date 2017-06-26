#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 15:01:09 2017

@author: dhingratul
"""
import pandas as pd

df = pd.DataFrame({
    'a': [4, 5, 3, 1, 2],
    'b': [20, 10, 40, 50, 30],
    'c': [25, 20, 5, 15, 10]
})


def twoLarge(array):
    idx = array.argmax()
    out = array.drop(array.index[idx])
    return out.max()


def second_largest(df):
    '''
    Fill in this function to return the second-largest value of each
    column of the input DataFrame.
    '''

    return df.apply(twoLarge)
