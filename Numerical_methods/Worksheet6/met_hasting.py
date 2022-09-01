import numpy as np
import random as rd
import math
import matplotlib.pyplot as plt

def rd_state(x,delta):
    return x + rd.uniform(-delta,delta)

m = 0 #mu for the gaussian function
s = 1 #sigma for the gaussian function

def p(x):
  return np.exp(-0.5*( (x-m)/s )**2)

"""
def met_has(x_0,n):     #scrap code
    #return min([1, (p(y))/ p(x)])
    x = x_0
    for j in range(n):
        y = rd_state(x)
        acc_array = np.zeros([len(x)])
        for i in range(len(x)):
            p = rd.random()
            acc_array[i] = min( [ 1 , ( p(y[i]) ) / p(x[i]) ] )
            if p <= acc_array[i]:
                x[i] = y[i]
    return acc_array
"""

def met_has(x_0,n):
  x = np.zeros(n)
  x[0] = x_0
  for j in range(n-1):
    y = rd_state(x[j],0.5)
    acceptance_prob = min( [1, p(y)/p(x[j]) ] )
    u = rd.random()
    if acceptance_prob >= u:
      x[j+1] = y
    elif acceptance_prob < u:
      x[j+1] = x[j]
  return x  
    

#x_0 = rd.random() #choosing random initial state. You can put custom intial state as well, doesnt matter
"""
def met_has(x_0,n):
    x = x_0
    for i in range(n):    #scrap code 
        y = rd_state(x)
        Accep(x,y)
    return """

#print(met_has(x_0,10**3))

#M = met_has(np.array([rd.random() for i in range(10**3)]), 10**3)

M = met_has(rd.random(), 10**4)

kwargs = dict(alpha=0.5, bins=100, density=True, stacked=True)

plt.hist(M,**kwargs)
plt.grid()
plt.show()