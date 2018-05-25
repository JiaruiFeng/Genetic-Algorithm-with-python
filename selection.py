# -*- coding: utf-8 -*-
"""
selection.py
"""
from __future__ import division
import numpy as np
def selection(population,value):
    
    #轮盘赌选择
    fitness_sum=[]
    for i in range(len(value)):
        if i ==0:
            fitness_sum.append(value[i])
        else:
            fitness_sum.append(fitness_sum[i-1]+value[i])
    
    for i in range(len(fitness_sum)):
        fitness_sum[i]/=sum(value)
    
    #select new population
    population_new=[]
    for i in range(len(value)):
        rand=np.random.uniform(0,1)
        for j in range(len(value)):
            if j==0:
                if 0<rand and rand<=fitness_sum[j]:
                    population_new.append(population[j])
                    
                
            else:
                if fitness_sum[j-1]<rand and rand<=fitness_sum[j]:
                    population_new.append(population[j])             
    return population_new