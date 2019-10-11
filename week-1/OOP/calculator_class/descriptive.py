#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:31:39 2019

@author: kennymiyasato
"""
import math 

class Calculator():
    
    def __init__(self, data):
        self.data = data
        self.length = len(self.data)

    def mean(self):
        self.mean = sum(self.data) / len(self.data)
    
    def median(self):
        self.data.sort()
        n = len(self.data)
        if n % 2:
            self.median = self.data[n/2]
        else:
            self.median = (self.data[n//2] + self.data[(n//2) - 1]) / 2
        
    def variance(self):
        sum_of_sqs = sum([(i - self.mean(self.data)) ** 2 for i in self.data ])
        self.variance = sum_of_sqs / (len(self.data) - 1)
    
    def stand_dev(self):
        self.stand_dev = math.sqrt(self.variance(self.data))