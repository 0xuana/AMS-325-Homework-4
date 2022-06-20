# -*- coding: utf-8 -*-
"""
Created on Sun Jun 19 16:25:21 2022

@author: 淡水
"""

import numpy as np
import matplotlib.pyplot as plt  

def markov_chain(n, N):
    P = np.array([])
    
    for i in range(n):          # Construct the P matrix by random method
        p = np.random.dirichlet(np.ones(n), size = 1)   # Construct an array which have a sum 1
        p = np.matrix(p)        # Change it into matrix data type. It is easier to combine
        if P.size == 0:         # Check if P is empty, if empty first
            P = p
        else:                   # Not empty: combine the matrix
            P = np.concatenate((P,p))
    
    # for i in range(5):              # Check if every row of the matrix sum to 1.0
    #     print(np.sum(P[i]))
    
    p = P[0]                    # Re-get 'p' vector as the required
    for i in range(N):          # dot the matrix (without np.dot)
        p = p * P
        
    # np.linalg.matrix_power(P, N)    # Calculate by matrix_power
    
    eigen = np.linalg.eig(P.T)  # Get the eigenvalue and  right eigenvectors
                                # First line is eigenvalue, Second line is eigenvectors
    p_stationary = eigen[1]     # Get the eigenvector
    
    p = P[0]
    y = []                      # Initial the list to save the difference data
    x = np.arange(N)            # Construct the x value
    
    for i in range(N):
        
        p = p * P
        y.append(np.linalg.norm(p - p_stationary))
    

    plt.plot(x, y)
    plt.xlabel('Steps')                 # x label "Steps"
    plt.ylabel('$p - p_{stationary}$')  # y label "Difference"
    plt.savefig('markov_chain.png')     # Save the plot

markov_chain(5, 50)
markov_chain(3, 50)







