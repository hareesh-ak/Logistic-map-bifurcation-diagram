# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 12:45:07 2018

@author: Hareesh
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x,a0,b0,L0):
    return a0*x*(1-x**(2-b0))+L0
# fp refers to fixed point
def find_fp(x0,a,b,L):
    x=np.array([x0])
    for i in range(1000):
        x=np.append(x,f(x[-1],a,b,L))
    return x[-200:-1]
lim=4
R=np.linspace(0,lim,5000)
l=0
b=1
x0=0.9
plt.figure(1)
for i in R:
    plt.figure(1)
    Xstar=find_fp(x0,i,b,l)
    plt.plot([i]*len(Xstar),find_fp(x0,i,b,l),'.r',markersize=1.8)
    
plt.xlim(0,lim)    
plt.title('Logistic Map \n$x_{n+1}$ = $rx_n$(1-$x_n$) \n' ,fontsize=18)    
plt.ylabel('$Attractor$\n$x_n$',fontsize=18)
plt.xlabel('$Parameter$\nr',fontsize=18)

plt.show()
