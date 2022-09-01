import numpy as np
import random as rd
import math
import matplotlib.pyplot as plt

pi = math.pi
e = math.e

n = 10**4 #number of points

def f(y):
    return 1/(y**2 + (np.cos(y))**2 )

def p(y,a):
    return a*np.exp(-y) 

def y(x,a):
    return -np.log(1-x/a)

def rng(N):
    return np.array( [ rd.random() for i in range(N)] )

g = 1/(1-(np.e)**-pi) #normalised value of a
M = y(rng(n), g ) #np.array([ y(rd.random(), a + j*h ) for i in range(N)])
N = f(M) /p(M, g )
mean = sum(N)/(len(N))
var = sum(N**2)/len(N) - mean**2
print("Mean, var, error(simpson integral - monte carlo): ",mean,var,(mean-1.5811879)," #The actual value of integral is found by normalising the p(y).")


I_range = np.zeros(n)

a = 1
b = 2
h = 0.001
t = int((b-a)/(h))


I_range = np.zeros(t)
a_range = np.linspace(a,b,t)

for j in range(0,t):
    M = y(rng(n), a+j*h ) #np.array([ y(rd.random(), a + j*h ) for i in range(N)])
    N = f(M) /p(M, a+j*h )
    mean = sum(N)/(len(N))
    var = sum(N**2)/len(N) - mean**2
    I_range[j] = var#((mean,var))

"""
#print(I_range)
j = 0
M = np.array([ y(rd.random(), a + j*h ) for i in range(N)])
N = f(M) /p(M, a+j*h )
mean = sum(N)/(len(N))
var = sum(N**2)/len(N) - mean**2
"""    

#1.5811879 integral value from Simpson integration
#print(mean,var)

plt.plot(a_range , I_range)


plt.legend(loc="upper left")
plt.xlabel('a')
plt.ylabel('I')
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.60)
plt.show()

"""The value of a must be 1/(1-e**-pi) for the integral to make sense as the integral of p(y)dy must be equal to 1 for integrand. This is in line with the result with the simpson's integration and error upto 3rd decimal place (for I checked upto the limits of my machine)"""