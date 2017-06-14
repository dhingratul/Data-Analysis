#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 15:46:56 2017

@author: dhingratul
"""

import numpy as np

# Subway ridership for 5 stations on 10 different days
ridership = np.array([
    [0,    0,    2,    5,    0],
    [1478, 3877, 3674, 2328, 2539],
    [1613, 4088, 3991, 6461, 2691],
    [1560, 3392, 3826, 4787, 2613],
    [1608, 4802, 3932, 4477, 2705],
    [1576, 3933, 3909, 4979, 2685],
    [95,  229,  255,  496,  201],
    [2,    0,    1,   27,    0],
    [1438, 3785, 3589, 4174, 2215],
    [1342, 4043, 4009, 4665, 3033]
])


def mean_riders_for_max_station(ridership):
    '''
    Fill in this function to find the station with the maximum riders on the
    first day, then return the mean riders per day for that station. Also
    return the mean ridership overall for comparsion.
    '''
    max_el = np.argmax(ridership[0, :])
    overall_mean = np.mean(ridership)
    mean_for_max = np.mean(ridership[:, max_el])
    return (overall_mean, mean_for_max)
