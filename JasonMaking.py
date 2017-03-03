# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 11:28:29 2017

@author: william.guo
"""

import cx_Oracle
import json
from datetime import datetime
from pandas import DataFrame

con = cx_Oracle.connect('.......')
query = "select * from ....'"
query01 = """select ....."""

cur = con.cursor()
cur.execute(query01)

columns = cur.description
columnList = []
for i in range(0, len(columns)):    
    columnList.append(columns[i][0])

#resultList = cur.fetchall()
df = DataFrame(cur.fetchall())
df.columns = columnList
print(df)
'''
resultDic = []

with open('jsonFile_1.json', 'w', newline='') as jsonFile:  
    for result in resultList:
        rowDic = {}
        resultDic.append(rowDic)
        for index in range(0, len(result)):
            column = columns[index][0]
            item = result[index]
            if(isinstance(item, datetime)):
                item = str(item)
            rowDic[column] = item
#            print(result[index], type(result[index]))
#        print(rowDic)
    json.dump(resultDic, jsonFile, indent=4, sort_keys=True)
 '''      
cur.close()
con.close()      
    

    
