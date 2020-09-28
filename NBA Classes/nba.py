#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 19:10:59 2020

@author: devinpowers
"""

from __future__ import print_function

import csv
with open("nba_2013.csv", "r") as f:
    reader = csv.reader(f, delimiter=',')
    nba = list(reader)
    
class Player():
    
    
    def __init__(self, data_row):
        
        sel.dpla