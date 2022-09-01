import numpy as np
import matplotlib.pyplot as plt
import random
import sys
#np.set_printoptions(threshold=sys.maxsize)

N = 10**3 #number of points

tf = 10 #final time
ti = 0

dt = (tf-ti)/float(N) #time step

m = 1.1 #mu
s = 1.4 #sigma

x_0 = 94.7 #random.random() #initial condition

t = np.linspace(ti,tf,N)

dW = np.sqrt(dt)*np.array([random.normalvariate(0,1) for i in range(N)])
W = np.cumsum(dW)

#x_em = np.array([ x_0*( 1 + m*dt + s*np.sum(dW[i-1:i]) ) for i in range(N)  ])


#print(x_em[:])

x_em = np.zeros(N)
x_em[0] = x_0

for i in range(1,N):
    dW_up = np.sum(dW[i-1:i])
    x_em[i] = x_em[i-1] + m*dt*x_em[i-1] + s*x_em[i-1]*dW_up


x_exact = x_0*np.exp(m*t-s**2*t*0.5 + s*W)
#print(x_exact)

plt.plot(t,x_em)
plt.plot(t,x_exact)
#plt.plot(t,f(t,x_0,m,s,b_t))
plt.grid()
plt.legend(["Euler Maryama method", "Exact function"])
plt.show()