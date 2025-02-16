#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 09:54:43 2023

@author: douglassilvestre
"""

import matplotlib.pyplot as plt
import numpy as np
import math

m      = 800;         # Mass (kg)
k      = 1.2*10**5;   # Spring Stiffness (N/m)
c      = 4*10**4;     # Damping Coefficient (N.s/m)
xo     = 1;           # Amplitude (m)
xo_dot = 0;           # Inicial Velocity (m/s)

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

# Plotting

plt.plot(t,xt)
plt.title("Step Response")
plt.xlabel("t")
plt.ylabel("xt")
plt.grid()
plt.show()