import numpy as np
import matplotlib.pyplot as plt
import random
import sys
#np.set_printoptions(threshold=sys.maxsize)

N = 10**3 #number of points

tf = 20 #final time
ti = 0

dt = (tf-ti)/float(N) #time step

k1 = 1.9 #k1
k2 = 1.4 #k2

x_0 = 0 #random.random() #initial condition

t = np.linspace(ti,tf,N)


#x_em = np.array([ x_0*( 1 + m*dt*i + s*np.sum(dW[:i:4]) ) for i in range(N)  ])
#print(x_em[:])

x_em = np.zeros(N)
x_em[0] = x_0

x_tent = np.zeros(N)


n = 1000 #number of "realisations"
for j in range(n):
    dW = np.sqrt(dt)*np.array([random.normalvariate(0,1) for i in range(N)])
    W = np.cumsum(dW)
    for i in range(1,N):
        dW_up = np.sum(dW[range((i-1),i)])
        x_em[i] = x_em[i-1] + k1*dt - k2*dt*x_em[i-1] + (np.sqrt(k1+k2*x_em[i-1]))*dW_up
    x_tent += x_em

x_tent = x_tent/n

x_exact = (float(k1)/k2)*( 1-np.exp(-k2*t) )
#print(x_exact)

plt.plot(t,x_tent)
plt.plot(t,x_exact)
#plt.plot(t,f(t,x_0,m,s,b_t))
plt.grid()
plt.legend(["Euler Maryama method", "Exact function"])
plt.show()