#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 09:54:43 2023

@author: douglassilvestre
"""

import matplotlib.pyplot as plt
import numpy as np
import math

# Mass (kg)
m      = 800;
# Spring Stiffness (N/m)
k      = 1.2*10**5;
# Damping Coefficient (N.s/m)
c      = 4*10**4;
# Amplitude (m)
xo     = 1;
# Inicial Velocity (m/s)
xo_dot = 0;

wn = math.sqrt(k/m)
Cc = 2*math.sqrt(k*m)
Z  = c/Cc

A = xo*wn*(((Z+math.sqrt(Z**2-1))+xo_dot)/(2*wn*math.sqrt(Z**2-1)))
B = -xo*wn*(((Z-math.sqrt(Z**2-1))-xo_dot)/(2*wn*math.sqrt(Z**2-1)))

xstart = 0
xstop = 1
increment = 0.002
t = np.arange(xstart,xstop,increment)

xt = (A*np.exp((-Z+math.sqrt(Z**2-1))*wn*t))+(B*np.exp((-Z-math.sqrt(Z**2-1))*wn*t))
xt_dot = (A*wn*(np.exp((-Z+math.sqrt(Z**2-1))*wn*t))*(-Z+math.sqrt(Z**2-1)))+(B*wn*(np.exp((-Z-math.sqrt(Z**2-1))*wn*t))*(-Z-math.sqrt(Z**2-1)))
xt_dot_dot = (A*np.sqrt(wn)*(np.exp((-Z+math.sqrt(Z**2-1))*wn*t))*(-Z+math.sqrt(Z**2-1))*(-Z+math.sqrt(Z**2-1)))+(B*np.sqrt(wn)*(np.exp((-Z-math.sqrt(Z**2-1))*wn*t))*(-Z-math.sqrt(Z**2-1))*(-Z-math.sqrt(Z**2-1)))

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
