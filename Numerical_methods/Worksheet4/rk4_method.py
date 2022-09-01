import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

def deriv(y, t, a, b, c): #define the derivative in coupled form
    return np.array( [ a*(y[1]-y[0]) , y[0]*(b-y[2])-y[1] , y[0]*y[1] - c*y[2] ] )

y0 = np.array( [ 0, 1, 0 ] )

st_time = 0
end_time = 100
h = 0.01 #step size
r = (end_time - st_time)/h

t = np.linspace(st_time, end_time, r) 

a = 10
c = 8.0/3
b = 28


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

sol = rungekutta4(deriv, y0, t, args=(a, b, c))

#print(sol)

fig = plt.figure()
#ax = plt.axes(projection='3d')
#print(sol[:,0])
#ax.plot3D(sol[:,0], sol[:,1], sol[:,2], 'gray')

plt.plot(t,sol[:,0])

#ax.plot( sol, 'b', label=r'$\theta(t)$')
#ax.legend(loc='best')
#ax.xlabel('t')
#ax.grid()
plt.grid()
plt.show()



