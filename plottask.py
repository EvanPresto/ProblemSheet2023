#Author : Evan Preston-Kelly
# Task 08 

import matplotlib.pyplot as plt
import numpy as np
# import matplotlib and nump 

x = np.random.normal(5,2,1000)

# set x equal to to generate 1000 random numbers with a median of 5 and a standard deviation of 2

def h(x):
    x = x**3
    return x

# Create a function h(x) = x**3


plt.plot(h(x))
# plot the function of x 
plt.xlabel('h(x)= x**3')
plt.title('Task 08')
plt.show()