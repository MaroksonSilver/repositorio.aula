# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:02:09 2019

@author: 08475268951
"""
# este programa calcula o fatorial de qualquer numero natural
def fatorial(n):
    if n == 0 or n ==1:
        return 1
    else:
        while n != 1:
                N = n*(n-1)
        n = n-1
        return N
            
        