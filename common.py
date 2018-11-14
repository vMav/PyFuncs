# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 15:44:06 2018

@author: studdockj
"""

import pandas as pd
import os
import datetime as dt


## DATE FUNCTIONS ----------------------------------
weekdays =  {0: 'Monday', 1:'Tuesday', 2:'Wednesday', 3:'Thursday', 4:'Friday', 5:'Saturday', 6:'Sunday'}
today = dt.date.today()


def monthlong(mon, year):
    start = dt.date(year, mon, 1).strftime('%Y-%m-%d')
    end = (dt.date(year, mon + 1, 1) - dt.timedelta(days=1)).strftime('%Y-%m-%d')
    return [start, end]

def date(arg):
    #input string i.e. 'fy18' or 'apr18-nov18' to return proper range
    
    #shortcuts for common ranges, membership here checked first
    arbitary_periods = {
            'fy17' : ['2016-07-01', '2017-06-30'],
            'fy18' : ['2017-07-01', '2018-06-30'],
            'cy17' : ['2017-01-01', '2017-12-31'],
            'cy18' : ['2018-01-01', '2018-12-31'],
            'fy19' : ['2018-07-01', '2019-06-30'],
            'tm' : monthlong(today.month, today.year),
            'lm' : monthlong(today.month - 1, today.year)
            }
 
    if arg in arbitary_periods:
        return arbitary_periods[arg]
    
    #mapped names to use for lookup
    month_num = {m : n for n, m in enumerate(['jan', 'feb', 'mar', 'apr', \
                'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'])}

    #string interpretation    
    if type(arg) == str:
        date_args = []
        
        #if range given
        if arg.find('-') > 0:
           drange = arg.split('-')
        
        #if single month given
        elif len(arg) == 5:
            drange = [arg, arg]
        
        #logic to create dates from start of first month to end of last
        for i, d in enumerate(drange):
            m = month_num[d[:3]]
            y = int(d[-2:]) + 2000
            date_args.append((dt.date(y, (m + i + 1), 1) -\
                              dt.timedelta(days=i)).strftime('%Y-%m-%d'))  

    return date_args
           
# ---------------------------------------------------

## PANDAS FUNCTIONS ---------------------------------

def pdwide(rows = 50, cols = 25,):
    #Resize dataframe (ROWS/COLS)
    pd.options.display.max_rows = cols
    pd.options.display.max_columns = rows

def label_days(df):
    #Replace standard pandas day numbers with name
    df.columns = [weekdays[i] if i in weekdays.keys() else i for i in  df.columns]
    return df

def freighter(df):
    return df[(df['Aircraft Type'].str.find('BAE146') > -1)|(df['Aircraft Type'].str.find('73F') > -1)\
          |(df['Aircraft Type'].str.find('73Y') > -1)|(df['Aircraft Type'].str.find('14Y') > -1)]
      
#------------------------------------------------------

golden = 1.61803398874989484820

class progress():
    def __init__(self,target):
        self.target = target
        self.i = None
        self.prog = [(str(10 * n)+'%', int(n * (self.target / 10))) for n in range(10, 0, -1)]
        self.active = True
        self.benchmarks = []
    
    def listen(self,i):
        
        if self.i == None:
            self.benchmarks.append(dt.datetime.now())
        
        self.i = i
        if self.active:
            
            
            
            if i > self.target:
                print('Target Exceeded')
                self.active = False
            
            elif i == self.prog[-1][1]:
                self.benchmarks.append(dt.datetime.now())
                print('Completed', self.prog.pop()[0], 'in:',self.benchmarks[-1] - self.benchmarks[0])
                
                if len(self.prog) == 0:
                    self.active = False
    
    def reset(self):
        self.__init__(self.target)