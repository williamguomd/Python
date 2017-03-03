# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 11:28:29 2017

@author: william.guo
"""

import cx_Oracle
import json
from datetime import datetime
from pandas import DataFrame

con = cx_Oracle.connect('QA_SF/Q44UEflI@qsis.czevdjzomfkp.eu-west-1.rds.amazonaws.com:1521/siris')
query = "select * from att_ord where ord_id like '571%'"
query01 = """select SIRIS.ORD.ORD_ID as ORDER.ID, ATTESTOR_CONTACT.ATTESTOR_ID AS ATTESTOR.ID
                from SIRIS.ORD
                join SIRIS.ATT_ATT_ORD
                on SIRIS.ORD.ORD_ID = SIRIS.ATT_ATT_ORD.ORD_ID
                join SIRIS.ATTESTOR
                on SIRIS.ATTESTOR.ATT_ATT_ORD_ID = SIRIS.ATT_ATT_ORD.ATT_ATT_ORD_ID
                and SIRIS.ATTESTOR.CURRENT_STEP is null
                join ATTESTOR_CONTACT
                on ATTESTOR_CONTACT.ATTESTOR_ID = SIRIS.ATTESTOR.ATTESTOR_ID
                and ATTESTOR_CONTACT.SENT_DATE < sysdate -9
                order by ORD_ID"""

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
    

    