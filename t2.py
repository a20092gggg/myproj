# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 20:58:34 2019

@author: t.g.c
"""

import numpy as np
import matplotlib.pyplot as plt

x1 = np.arange(0,360)
y1 = np.sin(x1 * np.pi / 180.0)
y2 = np.cos(x1 * np.pi / 180.0)


y1 = np.array(y1)
y2 = np.array(y2)
y3 = -x1 +2 
ff = np.convolve(y1,y2)
#plt.plot(ff)
#plt.plot(x1,y1)
#plt.plot(x1,y2)


def con(a1,a2):
    a1 = np.array(a1)
    a2 = np.array(a2)
    if len(a1) >= len(a2):
        a11 = np.pad(a1,((0,len(a1))),'constant')
        a22 = np.pad(a2,((0,len(a1))),'constant')
        yy = []
        for i in range(len(a1)*2):       
            j = 0
            y=None
            y=[]
            while j != i:
                y += [a11[j]*a22[i-j]]
                j += 1
            else:
                y += [a11[j]*a22[i-j]]
                j+=1
            yy += [sum(y)]
    else:
        a11 = np.pad(a1,((0,len(a2))),'constant')
        a22 = np.pad(a2,((0,len(a2))),'constant')
        yy = []
        for i in range(len(a1)*2):       
            j = 0
            y=None
            y=[]
            while j != i:
                y += [a11[j]*a22[i-j]]
                j += 1
            else:
                y += [a11[j]*a22[i-j]]
                j+=1
            yy += [sum(y)]
    plt.plot(yy)
    return yy 




        



    

    



