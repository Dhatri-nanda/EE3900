# -*- coding: utf-8 -*-
"""Untitled22.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1oXR_6K0MdwSOMp0b8-CNSrALqmlL4Z9a
"""

import numpy as np
from scipy import linalg as lg

A = np.array([[3, -2], [4, -2]])

values, vectors = lg.eig(A)
print(values)

Sum = values[0] + values[1]
print(Sum)

Prod = values[0]*values[1]
print(Prod)

#The quadratic equation if sum and product are given is A^2 - (sum)A + Prod