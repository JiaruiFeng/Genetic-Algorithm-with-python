# -*- coding: utf-8 -*-
"""
mutation.py
"""
from __future__ import division
import numpy as np
def mutation(offspring,pm):
    for i in range(len(offspring)):
        if np.random.uniform(0,1)<=pm:
            position=np.random.randint(0,len(offspring[i]))
            #'str' object does not support item assignment,cannot use = to change value
            if position!=0:
                if offspring[i][position]=='1':
                    offspring[i]=offspring[i][:position-1]+'0'+offspring[i][position:]
                else:
                    offspring[i]=offspring[i][:position-1]+'1'+offspring[i][position:]
            else:
                if offspring[i][position]=='1':
                    offspring[i]='0'+offspring[i][1:]
                else:
                    offspring[i]='1'+offspring[i][1:]
    return offspring