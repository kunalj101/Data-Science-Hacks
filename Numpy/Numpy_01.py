# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np

#Definition of numpy array
my_list = [1,2,3]
nested_list = [[1,2,3],[3,4,5],[5,6,7]]
array = np.array(my_list)
np_array = np.array(nested_list)
print(array)
print(np_array)

#Sequential array definition
print(np.arange(0,-10,-1))
print(np.linspace(0,-10,21))

#Random array generation
print(np.random.randn(3,3))
print(np.random.rand(3,3))
print(np.random.randint(1,10,(3,3)))
np.random.seed(42)
print(np.random.rand(4))
np.random.seed(40)
print(np.random.rand(4))
np.random.seed(42)
print(np.random.rand(4))
test = np.random.randint(0,26,10)
print(test)

#Shaping of array
print(test.argmax())
print(np_array.shape)
dtype_arr = np.random.rand(4)
print(dtype_arr.dtype)