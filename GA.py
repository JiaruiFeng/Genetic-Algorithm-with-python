# -*- coding: utf-8 -*-
"""
Genetic Algorithm
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
import math
import utils 
from selection import selection
from crossover import crossover
from mutation import mutation

def aimFunction(x):
    y=x+5*math.sin(5*x)+2*math.cos(3*x)
    return y


x=[i/100 for i in range(900)]
y=[0 for i in range(900)]
for i in range(900):
    y[i]=aimFunction(x[i])
#plt.plot(x,y)


#initiate population
population=[]
for i  in range(10):
    entity=''
    for j in range(17):  
        entity=entity+str(np.random.randint(0,2))
    population.append(entity)

    
t=[]
for i in range(1000):
    #selection
    value=utils.fitness(population,aimFunction)
    population_new=selection(population,value)
    #crossover
    offspring =crossover(population_new,0.7)
    #mutation
    population=mutation(offspring,0.02)
    result=[]
    for j in range(len(population)):
        result.append(aimFunction(utils.decode(population[j])))
    t.append(max(result))
    
plt.plot(t)
plt.axhline(max(y), linewidth=1, color='r')            
        

    


