# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

def horner(x):
    a = np.array([1, -18, 144, -672, 2016,-4032, 5376, -4608, 2304, -512],dtype=np.float)
    p = a[0]
    for i in range(1, 10):
        p = x*p + a[i]
    return p

def poly(x):
    return (x-2)**9

def bisect(fun, xlow, xhigh, tol=1e-8):
    """
    计算函数零点的二分算法
    
    Parameter
    ---------
    fun : 函数对象， fun(x)
    [xlow, xhigh] : 包含零点的区间
    tol : 阈值
    
    Return
    ------
    root : 零点
    """
    
    plow = fun(xlow)
    phigh = fun(xhigh)
    while xhigh - xlow > 2*tol:
        xmid = (xlow + xhigh)/2
        pmid = fun(xmid)
        if plow*pmid < 0:
            xhigh = xmid
            phigh = pmid
        elif pmid*phigh < 0:
            xlow = xmid
            plow = pmid
        else:
            xhigh = xmid
            xlow = xmid
            
    root = (xhigh + xlow)/2
    return root

x = np.linspace(1.92, 2.08, num=8000)

y0 = horner(x)
y1 = poly(x)

fig0 = plt.figure()
fig1 = plt.figure()

axes0 = fig0.gca()
axes1 = fig1.gca()

axes0.plot(x, y0)
axes1.plot(x, y1)

r0 = bisect(poly, 1.92, 2.10, tol=1e-10)
r1 = bisect(horner, 1.92, 2.10, tol=1e-10)

print("r0: ", np.abs(r0 - 2.0))
print("r1: ", np.abs(r1 - 2.0))

plt.show()

