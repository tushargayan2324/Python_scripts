import random
import numpy as np
import matplotlib.pyplot as plt

N = 10**4 #Number of steps

pi = np.pi

def x_f(n):
    x = 0
    for i in range(n):
        r = random.random()
        if r > 0.5:
            x += 1
        elif r < 0.5:
            x -= 1
        else:
            print("bruhh")
    return x

M = 10**4 #number of points

xf_array = np.zeros(M)

for i in range(M):
    xf_array[i] = x_f(N)

mean = float(sum(xf_array))/len(xf_array)

var = (sum( [ (x-mean)**2 for x in xf_array ] ) )/len(xf_array)

kwargs = dict(alpha=0.5, bins=100, density=True, stacked=True)

plt.hist(xf_array,**kwargs)
#plt.hist(y,**kwargs)

q = np.linspace(-10,10,M)
z = np.exp(-0.5*(q**2))/ (np.sqrt(2*pi))
#plt.plot(q,z)

plt.legend(['Mean is %f and Variance is %f' %( mean, np.sqrt(var) )])

plt.grid()
plt.show()
