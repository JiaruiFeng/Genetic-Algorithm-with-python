# -*- coding: utf-8 -*-
"""
crossover.py
"""
from __future__ import division
import numpy as np
def crossover(population_new, pc):
    
    half=int(len(population_new)/2)
    father=population_new[:half]
    mother=population_new[half:]
    np.random.shuffle(father)
    np.random.shuffle(mother)
    offspring=[]
    for i in range(half):      
        if np.random.uniform(0,1)<=pc:
            copint = np.random.randint(0,int(len(father[i])/2))
            son=father[i][:copint]+(mother[i][copint:])
            daughter=mother[i][:copint]+(father[i][copint:])
        else:
            son=father[i]
            daughter=mother[i]
        offspring.append(son)
        offspring.append(daughter)
    return offspring
