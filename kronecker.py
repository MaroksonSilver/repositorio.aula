# -*- coding: utf-8 -*-
#Este programa implementa o produto de Kronecker entre duas matrizes.
"""
Created on Tue Apr 23 07:52:34 2019

@author: 08475268951
"""
# to escrevendo essa msg pra nada mesmo

import numpy as np

A = np.asarray([[1,2,3],[4,5,6]])
B = np.asarray([[1,1,1,1],[1,1,1,1]])

(m,n) = A.shape
(p,q) = B.shape

AxB = np.zeros((m*p,n*q))

for i in range(m):
    for j in range(n):
        AxB[i*p:(i+1)*p, j*q:(j+1)*q] = A[i][j]*B
        

