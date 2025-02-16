#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 24 15:56:32 2023

@author: douglassilvestre
"""

import matplotlib.pyplot as plt
import numpy as np
import math

# Mass (kg)
m  = 9.5;
# Spring Stiffness (N/m)
k  = 18000;
# Amplitude (m)
xo = 0.1;
# Inicial Velocity (m/s)
xo_dot = 1;

wn = math.sqrt(k/m)
print ('wn =', wn)

Cc = 2*math.sqrt(k*m)
print ('Cc =', Cc)

c = Cc
print ('c =', c)

Z  = c/Cc
print ('Z =', Z)

xstart = 0
xstop = 2
increment = 0.002
t = np.arange(xstart,xstop,increment)

xt= (xo+(xo_dot+(wn*xo))*t)*np.exp(-wn*t)
xt_dot = np.exp(-wn*t)*((xo_dot+wn*xo)-(xo+(xo_dot+wn*xo))*t)
xt_dot_dot = -wn*np.exp(-wn*t)*((xo_dot+(wn*xo))-(wn*(xo+(xo_dot+wn*xo)*t))+(xo+((xo_dot+wn*xo)*t)))

# Plotting

plt.figure(1)
plt.plot(t,xt)
plt.title("System Response")
plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.grid()
plt.show()

plt.figure(2)
plt.plot(t,xt_dot)
plt.title("System Response")
plt.xlabel("Time (s)")
plt.ylabel("Velocity (m/s)")
plt.grid()
plt.show()

plt.figure(3)
plt.plot(t,xt_dot_dot)
plt.title("System Response")
plt.xlabel("Time (s)")
plt.ylabel("Acceleration (m^2/s)")
plt.grid()
plt.show()