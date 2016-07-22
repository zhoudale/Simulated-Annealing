# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:33:13 2015

@author: le
"""
import numpy as np
import random

# G is the adjacent matrix for 3-d cube
G = np.array([[0,1,0,1,1,0,0,0],
     [1,0,1,0,0,1,0,0]
    ,[0,1,0,1,0,0,1,0]
    ,[1,0,1,0,0,0,0,1]
    ,[1,0,0,0,0,1,0,1]
    ,[0,1,0,0,1,0,1,0]
    ,[0,0,1,0,0,1,0,1]
    ,[0,0,0,1,1,0,1,0]])

# G1 is the adjacent matrix for 4-d cube    
G1 = np.bmat([[G, np.eye(8)] ,[np.eye(8), G]])

# the objective funtion for 3-d and 4-d cube 2-color problem
def cube_color(x):
    return sum([G[i,j]*(x[i]+x[j]-1)**2 for i in range(8) for j in range(i)]) 

def cube4d_color(x):
    return sum([G1[i,j]*(x[i]+x[j]-1)**2 for i in range(16) for j in range(i)]) 
    
# G2 is the adjacent matrix for all connected 3-d cube
G2 = np.ones((8,8))

def connectcube_color(x):
    return sum([G2[i,j]*(x[i]==x[j])**2 for i in range(8) for j in range(i)]) 

#%%
# sinulated annealing
# input: f: objective function; n:number of nodes of the cube; color: number of color
# output: the color of each node
def SA(f,n,color):
    x = [0 for i in range(n)]
    t = 10000; count = 0; temp = list(range(n))
    while (count < n*10) and (t > 1e-1):
        random.shuffle(temp)
        xnew = x[:]
        for i in range(n):
            xnew[temp[i]] = (np.random.randint(color-1)+ 1 + xnew[temp[i]]) % color
            deltae = f(x) - f(xnew)
            if (deltae>=0):
                x = xnew[:]; count = 0
            else:
                if (random.uniform(0,1) < np.exp(deltae/t)):
                    x = xnew[:]; count = 0
                else:
                    count +=1
        t = t*0.98
    return x

#%% 
# solve the hypercube coloring problem
   
SA(cube_color,8,2)
a = SA(cube4d_color,16,2)
# the value of the objective function
cube4d_color(a)

a = SA(connectcube_color,8,3)
a = SA(connectcube_color,8,4)
connectcube_color(a)
