import random
import numpy as np
import matplotlib.pyplot as plt

N = 10**4 #Random number count

Dict_num = {}

pi = np.pi

#p = np.linspace(0,1,)
#t = np.linspace(0,1,N)

p = np.array([random.random() for i in range(N)])
t = np.array([random.random() for i in range(N)])

x = np.sqrt(-2*np.log(p))*np.cos(2*pi*t)
y = np.sqrt(-2*np.log(p))*np.sin(2*pi*t)

q = np.linspace(-10,10,N)
z = np.exp(-0.5*(q**2))/ (np.sqrt(2*pi))

#print(x)

kwargs = dict(alpha=0.5, bins=100, density=True, stacked=True)

plt.hist(x,**kwargs)
plt.hist(y,**kwargs)
plt.plot(q,z)

plt.grid()
plt.show()
#plt.hist(y, bins=50)
