# -*- coding: utf-8 -*-
"""
Created on Fri Sep 14 10:01:33 2018

@author: studdockj
"""

class fibonacci():
    def __init__(self, retain=False):
        self.value = 0
        self.last = 1
        self.retain = retain
        self.n = 0
        if retain:
            self.items = [self.value]
   
    def next(self):
        cur = self.value   
        self.value = self.value + self.last
        self.last = cur
        self.n += 1
        if self.retain:
            self.items.append(self.value)
        
        return self.value
    
    def iterlist(self, times, ret=True):
        self.items.extend([self.next() for _ in range(times)])
        
        if ret:
            return self.items
        
    def ratio(self):
        if self.n > 1:
            return self.value / self.last
    

    