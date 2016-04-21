# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 13:33:13 2015

@author: le
"""
import numpy as np
import random

G = np.array([[0,1,0,1,1,0,0,0],
     [1,0,1,0,0,1,0,0]
    ,[0,1,0,1,0,0,1,0]
    ,[1,0,1,0,0,0,0,1]
    ,[1,0,0,0,0,1,0,1]
    ,[0,1,0,0,1,0,1,0]
    ,[0,0,1,0,0,1,0,1]
    ,[0,0,0,1,1,0,1,0]])

def cube_color(x):
    return sum([G[i,j]*(x[i]+x[j]-1)**2 for i in range(8) for j in range(i)]) 
    
G1 = np.array([[0,1,0,1,1,0,0,0,1,0,0,0,0,0,0,0,],
     [1,0,1,0,0,1,0,0,0,1,0,0,0,0,0,0]
    ,[0,1,0,1,0,0,1,0,0,0,1,0,0,0,0,0]
    ,[1,0,1,0,0,0,0,1,0,0,0,1,0,0,0,0]
    ,[1,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0]
    ,[0,1,0,0,1,0,1,0,0,0,0,0,0,1,0,0]
    ,[0,0,1,0,0,1,0,1,0,0,0,0,0,0,1,0]
    ,[0,0,0,1,1,0,1,0,0,0,0,0,0,0,0,1]
    ,[1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0],
     [0,1,0,0,0,0,0,0,1,0,1,0,0,1,0,0]
    ,[0,0,1,0,0,0,0,0,0,1,0,1,0,0,1,0]
    ,[0,0,0,1,0,0,0,0,1,0,1,0,0,0,0,1]
    ,[0,0,0,0,1,0,0,0,1,0,0,0,0,1,0,1]
    ,[0,0,0,0,0,1,0,0,0,1,0,0,1,0,1,0]
    ,[0,0,0,0,0,0,1,0,0,0,1,0,0,1,0,1]
    ,[0,0,0,0,0,0,0,1,0,0,0,1,1,0,1,0]])    

def cube4d_color(x):
    return sum([G1[i,j]*(x[i]+x[j]-1)**2 for i in range(16) for j in range(i)]) 
    

G2 = np.array([[1,1,1,1,1,1,1,1],
     [1,1,1,1,1,1,1,1]
    ,[1,1,1,1,1,1,1,1]
    ,[1,1,1,1,1,1,1,1]
    ,[1,1,1,1,1,1,1,1]
    ,[1,1,1,1,1,1,1,1]
    ,[1,1,1,1,1,1,1,1]
    ,[1,1,1,1,1,1,1,1]])

def connectcube_color(x):
    return sum([G2[i,j]*(x[i]==x[j])**2 for i in range(8) for j in range(i)]) 


def SA(f,n,color):
    x = [0 for i in range(n)]
    t = 10000; count = 0; temp = range(n)
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
    
SA(cube_color,8,2)
a = SA(cube4d_color,16,2)
cube4d_color(a)

a = SA(connectcube_color,8,3)
a = SA(connectcube_color,8,4)
connectcube_color(a)

# problem 2

def f_1(x):
    #return 0.5*(x[0]+x[1]-1)**2 + (x[0]-2)**2 + x[1]**2
    return (x[0]-2)**2 + x[1]**2

def SAC(f,n):
    x = [0 for i in range(n)]
    alpha = [10 for i in range(n)]
    count = [0 for i in range(n)]
    t = 10000; temp = range(n);num=0
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
    
    
    
    
    
    
    
    