# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

def horner(x):
    a = np.array([1, -18, 144, -672, 2016,-4032, 5376, -4608, 2304, -512],dtype=np.float)
    n = len(x)
    p = np.ones(n)*a[0]
    for i in range(1, 10):
        p = x*p + a[i]
    return p

def poly(x):
    return (x-2)**9


x = np.linspace(1.92, 2.08, num=8000)

y0 = horner(x)
y1 = poly(x)

fig0 = plt.figure()
fig1 = plt.figure()

axes0 = fig0.gca()
axes1 = fig1.gca()

axes0.plot(x, y0)
axes1.plot(x, y1)

plt.show()

