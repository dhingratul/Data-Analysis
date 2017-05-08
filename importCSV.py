#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 11:47:35 2017

@author: dhingratul
Input: Filename in CSV Formate
Output: List of dictionary, where key is the header from the data, and
value corresponds to the entries in the data
"""
import unicodecsv


def importCSV(filename):
    with open(filename, 'rb') as f:
        reader = unicodecsv.DictReader(f)
        out = list(reader)
    return out

output = importCSV('/home/dhingratul/Dropbox/Academics/OnlineCourses/\
Data Analysis/Data-Analysis/enrollments.csv')
print(output[0])
