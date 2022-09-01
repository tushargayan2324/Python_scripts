import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

pi = np.pi

def deriv(y, t): #define the derivative in coupled form
    #print(y)
    M = np.zeros(len(y))
    for i in range(len(y)-1):
        M[i] = ( y[i+1] + y[i-1] )/(2)
    return M

def p_0(x):
    s = 0.000001 #taking sigma very small
    c = 1/np.sqrt(2*pi*s)
    return c*np.exp(-(x**2)/(2*s))


st_time = -2
end_time = 2
h = 0.01 #step size
N = int((end_time - st_time)/h)

y0 = p_0(np.linspace(-2,2,N))
print(y0)
#for i in range(N):
#    y0[i] = p_0(i-N/2)


t = np.linspace(st_time, end_time, N) 

def sol(y0,t):
    space = np.zeros((N,len(y0)))
    space[0] = y0
    for n in range(N-1):
        space[n+1] = deriv(space[n],t)
    return space

sol = sol(y0, t)

#print(sol)

fig = plt.figure()
#print(sol[:,0])

x_range = np.linspace(-2,2,N)

plt.plot(x_range,sol[0,:])
plt.plot(x_range,sol[50,:])
plt.plot(x_range,sol[100,:])
plt.plot(x_range,sol[300,:])


#ax.plot( sol, 'b', label=r'$\theta(t)$')
plt.legend(loc='best')
#ax.xlabel('t')
plt.grid()
plt.show()



