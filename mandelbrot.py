# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 14:42:22 2022

@author: 淡水
"""

import numpy as np
import matplotlib.pyplot as plt             # Import package numpy and matplotlib

n = int(input('Enter the n value: '))           # Required input
N_max = int(input('Enter the N_max value: '))
threshold = int(input('Enter the threshold value: '))

# The graph in the package is plot by the following value, 
# My Spyder seem to have some problem: It cannot deal with input method, I try it in jupyter.
# n = 1000
# N_max = 10
# threshold = 50

x = np.linspace(-2, 1, n)       # Generate the n value in [-2,1] for x
y = np.linspace(-1.5, 1.5, n)   # Generate the n value in [-1.5,1.5] for y
x, y = np.meshgrid(x, y)        # Construc the n x n matrix for generate c

c = x + 1j*y            # Generate c by x and y after using method meshgrid method in numpy.
# c grid has a size 10000 with a shape 100 x 100.

mask = np.zeros((n,n), dtype = bool)    # Generate mask array which filled with False
for i in range(n):
    for j in range(n):          # Calculate the z value for each complex value in c.
        z = 0                   
        for k in range(N_max):  # Calculation of z value
            z = z**2 + c[i,j]
            
        if abs(z) < threshold:  # Check the relation of z value and threshold
            mask[i,j] = True    # Mark the value True if z is less than the threshold.

plt.imshow(mask.T, extent = [-2, 1, -1.5, 1.5])
plt.gray()                      # Plot the graph 
plt.savefig('mandelbrot.png')   # Save the graph

