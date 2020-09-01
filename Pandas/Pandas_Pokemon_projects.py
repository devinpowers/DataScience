#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pokemon

@author: devinpowers
"""


import pandas as pd

df = pd.read_csv('pokemon_data.csv')



# reading data in Pandas

# Read Columns
#print(df.columns)


#print(df['Name'][0:10])

## Read each row
#print(df.iloc[0:4])

#print(df.columns)


#for index, row in df.iterrows():
    
    
    #print(index, row['Name'])
    
df.sort_values(['Type 1', 'HP'], ascending=[1,0])
