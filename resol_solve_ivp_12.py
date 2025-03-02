#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  1 17:46:46 2025

@author: francoisdeberdt
"""

import matplotlib.pyplot as plt
import numpy as np
import statistics
from scipy.integrate import solve_ivp
import sympy as sp

"""
yo = [5]

def fun(t,y): return -2*y[0]
sol = solve_ivp(fun, [0,1], yo, t_eval=np.linspace(0,1,20))

plt.figure()
plt.plot(sol.t, sol.y[0])
plt.xlabel('x')
plt.ylabel('y')

plt.show()


"""



"""
t=10

def fun(t,y): 
    y1, y2 = y
    return [ y2, np.cos(t)-4*y1]

yo=[0,0]

sol = solve_ivp(fun, [0,t], yo, t_eval=np.linspace(0,t,10*t))
plt.figure()
plt.scatter(sol.t, sol.y[0])
plt.xlabel('t')
plt.xlabel('y(t)')      
plt.show()

"""


t=40'(§"''

def fun(t,y):
    y1, y2 = y
    return [ y2, np.sin(t)+2*y2-5*y1 ]


y0 = [0,0]

sol = solve_ivp(fun, [0,t], y0, t_eval = np.linspace(0,t,t*10))

plt.figure()
plt.plot(sol.t, np.log(sol.y[0]))
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()






























