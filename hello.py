# import modules used here -- sys is a very standard one

# !/usr/bin/env python
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

hacker = "me"


# Gather our code in a main() function
def main():
    print("sys.argv: ", sys.argv)
    # print ('Hello there', sys.argv[1])
    print(repeat('hello', True))
    localVariableExample()
    print("The global variable is ", hacker)

    dynamicType()

    #forEachTest()

    exceptionTest("hhh")

    dictTest()

    for num in range(10, 2, -1):
        print("Number in range: ", num)

    #print onthe same line
    print("Hello...", end='')
    print("World!!!")

    print("Current Working Directory: ", os.getcwd())

    fileAccess('file.txt', 'output.txt')
    '''
    for _ in (0,1,2,3,4,5):
        print("underscore...")
'''

# Command line args are in sys.argv[1], sys.argv[2] ...
# sys.argv[0] is the script name itself and can be ignored



# Defines a "repeat" function that takes 2 arguments.
def repeat(s, exclaim):
    """
    Returns the string 's' repeated 3 times.
    If exclaim is true, add exclamation marks.
    """

    result = s + s + s  # can also use "s * 3" which is faster (Why?)
    if exclaim:
        result = result + '!!!'
    return result


def localVariableExample():
    hacker = "you"
    print("The local variable is ", hacker)

#%%
def dynamicType():
    route = 86
    print(route, type(route))

    route = "hello..."
    print(route, type(route))
#%%

def forEachTest():
    strTest = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    for letter in strTest:
        if letter in "AEIOU":
            print(letter, " is a vowel")
        else:
            print(letter, " is a constant")


def exceptionTest(num):
    try:
        i = int(num)
        print("valid int: ", i)
    except ValueError as errorMsg:
        print(errorMsg)

    num.__class__.__name__.lower()


def dictTest():
    dict = {'a': 'apple', 'g': 'google', 'o': 'omega'}

    for k, v in dict.items():
        print(k, '->', v)

def fileAccess(inFile, outFile):
    '''data = open(file)
    for eachLine in data:
        if not eachLine.find(':') == -1:
            (role, sentence) = eachLine.split(':', 1)
            print(role, '->', end='')
            print(sentence, end='')

    data.close()'''
    try:
        data = open(inFile)
        out = open(outFile, 'w')
        for eachLine in data:
            out.write(eachLine)
            #print(eachLine, file = outFile)

            try:
                (role, sentence) = eachLine.split(':', 1)
                print(role, '->', end='')
                print(sentence, end='')
            except ValueError as valueError:
                #print(valueError)
                pass
    except IOError:
        print("the datafile is missing...")
    finally:
        if data in locals():
            data.close()
        if out in locals():
            out.close()
#%%
import pandas as pd
import numpy as np

def pandatest():
    dates = pd.date_range('20170101', periods=6)
    df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
    ds = df.sort_index(axis=1, ascending=False)
    
    print(ds)
#%%
def for_test():
    for ct in range(10, 1, -2):
        print(ct, end=' ')
#%%
def list_test():
    a = [12, 3, 22, 99, 25.4, 68]
    a.insert(11, 22.2)  #first parameter is the given position
    a.append(-9)
    print(a)
    print("length of the list: ",len(a))
    print("Last element: ",a[-1], "First element: ", a[0])  
    print("Element from 2nd one: ",a[2:])  
    print("Element from 2nd to 4th: ",a[2:4])  #this does not include the 4th one
    
    lis = ["tiger","python", "cat", "dog"]
    if "chicken" in lis:
        print("chicken is in the list")
    else:
        print("chicken is not in the list")
    if "dog" not in lis:
        print("dog is not in the list")
    else:
        print("dog is in the list")
        
    print("list: ", list(range(1, 13, 3)))
    print("###", range(1, 13, 3))
   
    ll = ['a', 'ab', 'a', 'as', 'c', 'a', 'c', 'b']
    print("count of 'a': ", ll.count('a'))
    
    l1 = [1,2,3]    
    l2 = [2,3,4]
    l3 = l1 + l2
    l4 = l1 * 4  #[1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3]
    
    b1 = [1,2,3]
    b2 = [1,2,3]
    if b1 == b2:
        print("b1 equals to b2")
    else:
        print("b1 does not equals to b2")
    if b1 is b2:
        print("b1 is b2")
    else:
        print("b1 is not b2")
        
        
#%%
def enumerate_test():
    season = ["spring","summer","fall","winter"]
    lis = list(enumerate(season, start = 10))
    
    print(lis)
#%%    
def string_test():
    str = "20170112, bmo, corporation, ON"
    str_list = str.split(',')
    print("Before strip: ", str_list)
    new_list = []
    for word in str_list:
        new_list.append(word.strip())
        
    print("After strip: ", new_list)
    
    glue = ';'
    glue_list = glue.join(new_list)
    print("Glue list: ", glue_list, "\n type is: ", type(glue_list))
    
#%%
import turtle

tess = turtle.Turtle()
alex = tess
alex.color("hotpink")
#%%
import random

def random_test():
    ls = ["tiger","python", "cat", "dog"]

    for i in range(5):
        animal = random.choice(ls)
        print("Randomly chose item is: ", animal)

#%%
def tuple_test():
    t1 = ("tiger","python", "cat", "dog")
    print(t1)
    
    print("1st one:", t1[0], "last one: ", t1[-1])
    
#%%   
def dictionary_test():
    employee = {'Name':'william', 'Age':'18', 'title':'CEO'}
    print(employee)
    print('Name:',employee['Name'])
    print('Age:',employee["Age"])
    
    for item in employee.items():
        print("ITEM: ", item)
    
    for key, value in employee.items():
        print(key, '->', value)
        
    for k in employee:
        print(k,'>>',employee[k])
        
    for value in employee.values():
        print('VALUE: ', value)
    
    if 'Name' in employee:
        print('Name is a key in employee')
    else:
        print('Name is not a key in employee')
        
    if 'NaMe' in employee:
        print('NaMe is a key in employee')
    else:
        print('NaMe is not a key in employee')
    
    same_employee = employee
    new_employee = employee.copy()
    employee['Name'] = 'Bill'
    print('In Employee: ', employee['Name'])
    print('In same_employee: ', same_employee['Name'])
    print('In new_employee: ', new_employee['Name'])
    
    print('>>>>>', employee.get('Name', 'HAHA'))
    print('>>>>>', employee.get('NaMe', 'HAHA'))
#%%
import numpy as np

def data_test():
    ls = ["tiger","python", "cat", "dog"]
    arr = np.array(ls)
    print('Type of arr: ', type(arr))
    
    arr = np.array([[1,2,3,4], [2,4,6,9]])
    print('SHAPE: ',arr.shape)
    
    print(np.ones((3, 4), dtype = np.int32))
#%%
import urllib.request as request

def url_test():
    with request.urlopen('http://www.google.com') as response:
        html = response.read()
    print(html)
#%%
import matplotlib.finance as finance
import datetime
import pandas as pd

def finance_test():
    today = datetime.date.today()
    start = (today.year-1, today.month, today.day)
        
    quotes = finance.fetch_historical_yahoo('AAPL', start, today)
    df = pd.DataFrame(list(quotes))
    print(df)
    
    
    
    
    
    
#%%
import pandas as pd
from pandas import DataFrame
import datetime
from pandas_datareader import data

sp500 = data.get_data_yahoo('%5EGSPC', 
                                 start=datetime.datetime(2000, 10, 1), 
                                 end=datetime.datetime(2012, 1, 1))

print(sp500.head())

#%%
import cx_Oracle

con = cx_Oracle.connect('pythonhol/welcome@127.0.0.1/orcl')
                 
ver = con.version.split(".")
print(ver)


#%%
import json
student = {"101":{"class":'V', "Name":'Rohit',  "Roll_no":7},
           "102":{"class":'V', "Name":'David',  "Roll_no":8},
           "103":{"class":'V', "Name":'Samiya', "Roll_no":12}}
print(json.dumps(student));

#%%

from test import *

print(username)
str1 = 'Hello'
str2 = str1 + ' ' + username
print(str2)

#%%

a = ['today', 'is','Friday']

for i, item in enumerate(a):
    print("{i}: {item}".format(i=i, item=item));

#%%

filename = 'foobar.txt'
basename, __, ext = filename.rpartition('.')
print(basename, ext)

#%%

def add100(x):
    return x + 100
    
hh = [11,22,33]  
#lst = list(map(add100, hh))
lst = [*map(add100, hh)]

print(lst)
#%%

myFun = lambda a, b: a*b
print('Result: ', myFun(2,9))

#%%

import numpy as np

n = np.arange(0, 30, 5)
n = n.reshape(3,2)

n = n.reshape(2, 3)
#%%
from functools import reduce

ma = reduce(lambda a, b: a if(a>b) else b, [47,11,42,100,13])
print(ma)

summ = reduce(lambda a, b: a +b, range(1, 10))
print(summ)

lst = [47,11,42,170,13]
maxx = lst.reduce(lambda a, b: a if(a>b) else b)
print(maxx)

#%%

dic = {'NT': 1, 'QC': 1, 'SK': 1, 'ON': 1}
for k, v in dic.items():
    print('Key: ', k, ' Value: ', v)
#%%
#use dictionary for switch:
def put2AB(index, value):
    AB_List[index] = value
def put2BC(index, value):
    BC_List[index] = value
...

takeaction = {
              'AB': put2AB, 
              'BC': put2BC,
              ...
              }
def put_dic2list(dics, index):
    for k,v in dics.items():
        takeaction[k](index, v)
#%%

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
