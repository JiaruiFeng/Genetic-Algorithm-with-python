# -*- coding: utf-8 -*-
"""
utils.py
"""
from __future__ import division

def decode(x):
    y=0+int(x,2)/(2**17-1)*9
    return y



def fitness(population,aimFunction):
    value=[]
    for i in range(len(population)):
        value.append(aimFunction(decode(population[i])))
        #weed out negative value
        if value[i]<0:
            value[i]=0
    return value