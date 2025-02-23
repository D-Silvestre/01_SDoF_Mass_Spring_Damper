#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 26 17:04:19 2023

@author: douglassilvestre
"""

import matplotlib.pyplot as plt
import numpy as np
import math

# Mass (kg)
m  = 800;
# Spring Stiffness (N/m)
k  = 1.2*10**5;
# Damping Coefficient (N.s/m)
c  = 8*10**3;
# Amplitude (m)
xo = 0.1;
# Inicial Velocity (m/s)
xo_dot = 0;

wn = math.sqrt(k/m)
Cc = 2*math.sqrt(k*m)
Z  = c/Cc
wa = wn*math.sqrt(1-(Z**2))

xstart = 0
xstop = 1
increment = 0.002
t = np.arange(xstart,xstop,increment)

xt = (xo/math.sin(math.atan(wa*xo/(xo_dot+Z*wn*xo))))*np.exp(-Z*wn*t)*np.sin(wa*t+math.atan(wa*xo/(xo_dot+Z*wn*xo)))
xt_dot = ((xo/math.sin(math.atan(wa*xo/(xo_dot+Z*wn*xo))))*np.exp(-Z*wn*t))*((-Z*wn*np.sin(wa*t+math.atan(wa*xo/(xo_dot+Z*wn*xo))))+(wa*np.cos(wa*t+math.atan(wa*xo/(xo_dot+Z*wn*xo)))))
xt_dot_dot = ((xo/math.sin(math.atan(wa*xo/(xo_dot+Z*wn*xo))))*np.exp(-Z*wn*t))*(((-Z**2*wn**2*np.sin(wa*t+math.atan(wa*xo/(xo_dot+Z*wn*xo))))-(wa*Z*wn*np.cos(wa*t+math.atan(wa*xo/(xo_dot+Z*wn*xo)))))+((-Z*wn*wa*np.cos(wa*t+math.atan(wa*xo/(xo_dot+Z*wn*xo))))-(wa**2*np.sin(wa*t+math.atan(wa*xo/(xo_dot+Z*wn*xo))))))
                                                  
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
