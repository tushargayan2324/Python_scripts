import random
import numpy as np
import matplotlib.pyplot as plt

N = 10**4 #Random number count

sig = 9
mu = 2

pi = np.pi

#p = np.linspace(0,1,)
#t = np.linspace(0,1,N)

p = np.array([random.random() for i in range(N)])
t = np.array([random.random() for i in range(N)])

x = sig*np.sqrt(-2*np.log(p))*np.cos(2*pi*t) + mu*np.ones(N)
y = sig*np.sqrt(-2*np.log(p))*np.sin(2*pi*t) + mu*np.ones(N)

q = np.linspace(-60,60,N)
z = np.exp(-0.5*(((q-mu)/sig)**2))/ (np.sqrt(2*pi*sig**2))

#print(x)

kwargs = dict(alpha=0.5, bins=100, density=True, stacked=True)

plt.hist(x,**kwargs)
plt.hist(y,**kwargs)
plt.plot(q,z)

plt.grid()
plt.show()
#plt.hist(y, bins=50)
