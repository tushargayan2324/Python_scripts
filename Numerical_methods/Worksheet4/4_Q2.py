import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

pi = np.pi

def deriv(y, t): #define the derivative in coupled form
    #print(y)
    M = np.zeros(len(y))
    for i in range(len(y)-1):
        M[i] = ( y[i+1] + y[i-1] - 2*y[i] )/(2*h)
    return M

def p_0(x):
    s = 0.000001 #taking sigma very small
    c = 1/np.sqrt(2*pi*s)
    return c*np.exp(-(x**2)/(2*s))


st_x = -2
end_x = 2
h = 0.01 #step size
N = int((end_x - st_x)/h)

y0 = p_0(np.linspace(st_x,end_x,N))


#for i in range(N):
#    y0[i] = p_0(i-N/2)

st_time = 0
end_time = 10
step_time = 0.01
N1 = int((end_time-st_time)/step_time)

t = np.linspace(st_time, end_time, N1) 



def rungekutta4(f, y0, t, args=()):
    N = len(t)
    y = np.zeros((N, len(y0)))
    y[0] = y0
    for i in range(N - 1):
        h = t[i+1] - t[i]
        k1 = f(y[i], t[i], *args)
        k2 = f(y[i] + k1 * h / 2., t[i] + h / 2., *args)
        k3 = f(y[i] + k2 * h / 2., t[i] + h / 2., *args)
        k4 = f(y[i] + k3 * h, t[i] + h, *args)
        y[i+1] = y[i] + (h / 6.) * (k1 + 2*k2 + 2*k3 + k4)
    return y

sol = rungekutta4(deriv, y0, t, args=())

#print(sol)

fig = plt.figure()
#print(sol[:,0])
#plt.plot(sol[:,0], sol[:,300], sol[:,700],sol[:,900], 'gray')

x_range = np.linspace(-2,2,N)

plt.plot(x_range,sol[0,:])
plt.plot(x_range,sol[200,:])
plt.plot(x_range,sol[500,:])
plt.plot(x_range,sol[700,:])


#ax.plot( sol, 'b', label=r'$\theta(t)$')
plt.legend(loc='best')
#ax.xlabel('t')
plt.grid()
plt.show()



