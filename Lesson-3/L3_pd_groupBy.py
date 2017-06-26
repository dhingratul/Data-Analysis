#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 26 15:56:55 2017

@author: dhingratul
"""

import numpy as np
import pandas as pd

values = np.array([1, 3, 2, 4, 1, 6, 4])
example_df = pd.DataFrame({
    'value': values,
    'even': values % 2 == 0,
    'above_three': values > 3
}, index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])


filename = '/datasets/ud170/subway/nyc_subway_weather.csv'
subway_df = pd.read_csv(filename)
grouped_data = subway_df.groupby('station').mean()
print(grouped_data)
