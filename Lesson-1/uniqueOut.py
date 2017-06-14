#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 13:48:29 2017

@author: dhingratul
Input: Filename, columnName
Output : Unique number of a column of data
"""
import pandas as pd


def uniqueOut(filename, columnName):
    file = pd.read_csv(filename)
    return len(file[columnName].unique())

filename = '/home/dhingratul/Documents/Dataset/Data Analysis/\
daily_engagement_full.csv'

print(uniqueOut(filename, 'acct'))
