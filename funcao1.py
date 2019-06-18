# -*- coding: utf-8 -*-
"""
Created on Tue May 14 07:56:24 2019

@author: 08475268951
"""

import numpy as np

def f(x):
    return x**2 - np.pi

def bisseccao(f,a,b,tolerancia):
    tolerancia = 1e-10
    if np.abs(f(a)) < tolerancia:
        return a
    elif np.abs(f(b)) < tolerancia:
        return b
    elif f(a)*f(b) > 0:
        return np.Inf
    else:
        x = (a+b)/2
        print("x = {}".format(x))
        print("f(x) = {}".format(f(x)))
        nbiter = 0
        while np.abs(f(x)) >  tolerancia:
            if f(x)*f(a) > 0:
                a = x
            else:
                b = x
            x = (a+b)/2  
            print("x = {}".format(x))
            print("f(x) = {}".format(f(x)))
            nbiter = nbiter + 1
        return x, nbiter
    
    
    
    
    
