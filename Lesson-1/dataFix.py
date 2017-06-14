#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  8 12:25:04 2017

@author: dhingratul
Fixes the data types for the imported values from CSV file using importCSV
"""
from importCSV import importCSV
from datetime import datetime as dt
output = importCSV('/home/dhingratul/Dropbox/Academics/OnlineCourses/\
Data Analysis/Data-Analysis/enrollments.csv')


def parse_date(date):
    if date == "":
        return None
    else:
        return dt.strptime(date, '%Y-%m-%d')


def parse_maybe_int(i):
    if i == "":
        return None
    else:
        return int(i)


for i in output:
    i['cancel_date'] = parse_date(i['cancel_date'])
    i['days_to_cancel'] = parse_maybe_int(i['days_to_cancel'])
    i['is_canceled'] = i['is_canceled'] is True
    i['is_udacity'] = i['is_udacity'] is True
    i['join_date'] = parse_date(i['join_date'])
