# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 20:20:23 2021

@author: vidhan
"""

import numpy as np

# Indexing numpy array
arr = np.random.randint(1,100,(4,4))
print(arr)
print(arr[2,2])

# Broadcasting a value 
arr[:2,:2] = 50
print(arr)

# Conditioning a numpy array
arr_new = arr > 49
print(arr_new)
print(arr[arr_new])
print(arr[arr_new].shape)