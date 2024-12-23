# -*- coding: utf-8 -*-
"""Numpy array.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WW6O5d5CiizC2qR69Hztfg1G6YyKthAl

Create a NumPy array with 5 elements initialized with zeros.
"""

import numpy as np

array_zeros = np.zeros(5)
print("Question 1:", array_zeros)

"""Create a NumPy array with 3 rows and 4 columns initialized with ones."""

array_ones = np.ones((3, 4))
print("Question 2:\n", array_ones)

"""Create a 1D NumPy array containing numbers from 1 to 10."""

array_1_to_10 = np.arange(1, 11)
print("Question 3:", array_1_to_10)

"""4.Create a 2D NumPy array with dimensions 3x3 containing numbers from 1 to 9."""

array_3x3 = np.arange(1, 10).reshape(3, 3)
print("Question 4:\n", array_3x3)

"""Question 5
Create a 3D NumPy array with dimensions 2x3x4 containing random integers between 0 and 9.
"""

array_random_3d = np.random.randint(0, 10, (2, 3, 4))
print("Question 5:\n", array_random_3d)

"""Question 6
Create a NumPy array from a list containing elements [1, 2, 3, 4, 5].
"""

array_from_list = np.array([1, 2, 3, 4, 5])
print("Question 6:", array_from_list)

"""Question 7
Convert a tuple (6, 7, 8, 9, 10) into a NumPy array.
"""

tuple_to_array = np.array((6, 7, 8, 9, 10))
print("Question 7:", tuple_to_array)

"""Question 8
Create a NumPy array with shape (4, 2) containing numbers from 0 to 7.
"""

array_4x2 = np.arange(0, 8).reshape(4, 2)
print("Question 8:\n", array_4x2)

"""Question 9
Create a 3D NumPy array with shape (2, 3, 4) initialized with zeros.
"""

array_zeros_3d = np.zeros((2, 3, 4))
print("Question 9:\n", array_zeros_3d)

"""Question 10
Create a 2D NumPy array with shape (3, 3) containing random floating-point numbers between 0 and 1.
"""

array_random_float = np.random.rand(3, 3)
print("Question 10:\n", array_random_float)

"""Question 11
Create a NumPy array with shape (5,) containing numbers from 10 to 50, incrementing by 5.
"""

array_incrementing = np.arange(10, 55, 5)
print("Question 11:", array_incrementing)

"""Question 12
Create a NumPy array with shape (2, 5) containing numbers from -2 to 7.
"""

array_neg2_to7 = np.arange(-2, 8).reshape(2, 5)
print("Question 12:\n", array_neg2_to7)

"""Question 13
Create a 1D NumPy array with shape (10,) containing numbers from 100 to 109, and change its data type to float.
"""

array_100_to_109 = np.arange(100, 110, dtype=float)
print("Question 13:", array_100_to_109)

"""Question 14
Create a 2D NumPy array with shape (3, 4) initialized with ones, and then change its data type to int.
"""

array_ones_int = np.ones((3, 4), dtype=float).astype(int)
print("Question 14:\n", array_ones_int)

"""Question 15
Create a 3D NumPy array with shape (2, 2, 3) initialized with specified numbers.
"""

array_specified_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Question 15:\n", array_specified_3d)