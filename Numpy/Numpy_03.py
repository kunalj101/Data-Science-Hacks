# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 20:41:04 2021

@author: vidhan
"""

import numpy as np

arr = np.arange(1,26).reshape(5,5)

# Operations on numpy
print(arr)
arr1 = arr*10
#print(arr1) 

# Notice the replaced undefined values as NAN and INF
#print(arr1/(arr-1))

nanarr = arr-1
#print(nanarr/nanarr)

# Mathematical operation on numpy array

#print(np.sin(arr))
#print(np.log(arr))

# Statistical operations on numpy array
print(arr.sum())
print(arr.mean())
print(arr.var())
print(arr.std())

# Operations along axis,i.e, rows or columns in 2D
print(arr.mean(axis=0)) # Across the rows but not along,i.e, column wise
print(arr.mean(axis=1)) # Across the column but not along,i.e, row wise 

