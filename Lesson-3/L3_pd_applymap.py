#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 19 19:25:48 2017

@author: dhingratul
"""
import pandas as pd

grades_df = pd.DataFrame(
    data={'exam1': [43, 81, 78, 75, 89, 70, 91, 65, 98, 87],
          'exam2': [24, 63, 56, 56, 67, 51, 79, 46, 72, 60]},
    index=['Andre', 'Barry', 'Chris', 'Dan', 'Emilio',
           'Fred', 'Greta', 'Humbert', 'Ivan', 'James']
)


def gradeConverter(val):
    if val >= 90:
        return "A"
    elif val >= 80:
        return "B"
    elif val >= 70:
        return "C"
    elif val >= 60:
        return "D"
    else:
        return "F"


def convert_grades(grades):
    '''
    Fill in this function to convert the given DataFrame of numerical
    grades to letter grades. Return a new DataFrame with the converted
    grade.
    The conversion rule is:
        90-100 -> A
        80-89  -> B
        70-79  -> C
        60-69  -> D
        0-59   -> F
    '''
    return grades.applymap(gradeConverter)

# Driver Program
print(convert_grades(grades_df))
