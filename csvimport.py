# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 10:54:33 2017

@author: william.guo
"""
#%%
# !/usr/bin/env python
import sys
import os
import csv

from collections import namedtuple

def importCSV(csvFile):
    with open(csvFile, 'r') as csvfile:
        reader = csv.reader(csvfile)
        headings = next(reader)
        Row = namedtuple('Row', headings)
        for r in reader:
            row = Row(*r)
            print (row)
            
    
#%%

import pandas as pd

def importCSV(csvFile):
    df = pd.read_csv(csvFile)
#    print(df.columns)
#    print(df.ix[3:6, 0:3])
    
#    print('DataFrame length: ', df)
    print("Specific value: ",df.iloc[2:3,1:2])
#%%
'''   
    for row in df.itertuples():
        print( getattr(row, "UNIQUE_ID"), getattr(row, "Customer_Nbr"))
'''
        
# work with missing value http://pandas.pydata.org/pandas-docs/stable/missing_data.html
# http://www.jianshu.com/p/682c24aef525
        
#%%
import pandas as pd
import cx_Oracle

con = cx_Oracle.connect('USERNAME','PASSWORD',cx_Oracle.makedsn('HOSTNAME',1521,'SERVICENAME'))
cur = con.cursor()

cur.executemany('''INSERT INTO HOTEL_DIMENSION (PROPERTY_ID,OID,
                                         HOTEL_NAME,CITY_CODE,CITY_NAME,
                                         COUNTRY_NAME,CHAIN_CODE, CHAIN_NAME,"LOCK",
                                         ADDR,MADE_ON) 
                                         VALUES (:2,:1,:3,:4,:5,:6,:7,:8,:9,:10,:11)''')
con.commit()

cur.close()
con.close()

#%%

