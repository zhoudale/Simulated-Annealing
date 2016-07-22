# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:32:17 2016

@author: le
"""

# Generalize SA code to continuous real-valued variables

import numpy as np
import random

#example objective funtion
def f_1(x):
    #return 0.5*(x[0]+x[1]-1)**2 + (x[0]-2)**2 + x[1]**2
    return (x[0]-2)**2 + x[1]**2

# simulated annealing for continuous variables
# input: f: objective function; n: dimension of the variable
# output: x: optimal x for objective f(x); num: number of iter
def SAC(f,n):
    x = [0 for i in range(n)]
    alpha = [10 for i in range(n)]
    count = [0 for i in range(n)]
    t = 10000; temp = list(range(n));num=0
    while (max(alpha) > 1e-2) and (t > 1e-3):
        num += 1
        random.shuffle(temp)
        xnew = x[:]
        for i in range(n):
            xnew[temp[i]] = ((np.random.randint(2)-0.5)*alpha[temp[i]] + xnew[temp[i]]) 
            deltae = f(x) - f(xnew)
            if (deltae>=0):
                x = xnew[:]
            else:
                if (random.uniform(0,1) < np.exp(deltae/t)):
                    x = xnew[:]
                else:
                    count[temp[i]] +=1
        t = t*0.99
        if num%20==0:
            for i in range(n):
                if count[i]/float(num)<0.55:
                    alpha[i] = 2 * alpha[i]
                else:
                    if count[i]/float(num) > 0.65:
                        alpha[i] = alpha[i]/2.0
    return x,num
 
#%%
# take the average of the output to have a more precise result
q = [0 for i in range(20)]   
for i in range(20):
    q[i] = SAC(f_1,2)
   
ave1 = ave2 = ave3 = 0   
for i in range(20):
    ave1 += q[i][0][0]
    ave2 += q[i][0][1]
    ave3 += q[i][1]
    
ave1/20
ave2/20
ave3/20    