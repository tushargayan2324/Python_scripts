import numpy as np
import matplotlib.pyplot as plt

def dxdt(x,v,t):
    return v

l = 0 #lambda

def dvdt(x,v,t,l):
    return -x -l*(x**3)


st_time = 0
end_time = 10
h = 0.001 # time step

N = int((end_time - st_time)/h)


x = np.zeros((N,1)) #position array
v = np.zeros((N,1)) #v array
h_v = np.zeros((N,1)) #half step v array
E_array = np.zeros((N,1))


t = np.linspace(st_time, end_time, N)


v[0] = 0 #initial velocity
x[0] = 1 # " position
#part a 
"""
def E(x,v,l):
    return v*v/2 + x*x/2 + l*(x**4)/4
E_array[0] = E(x[0],v[0],l)
"""
#print(dvdt(0,0,0))
l_array = np.linspace(0,3,3)

for l in l_array:
    for i in range(0,len(t)-1):
        h_v[i+1] = h_v[i] + h*dvdt(x[i],v[i],t[i],l)/2
        x[i+1] = x[i] + h*h_v[i+1]
        v[i+1] = h_v[i+1] + h*dvdt(x[i],v[i],t[i],l)/2
        #E_array[i+1] = E(x[i],v[i],l)
    plt.plot(x,v)

plt.xlabel("velocity")
plt.ylabel("displacement")
plt.title("lambda = %s and step size = %s"%(l_array,h))
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.60)
plt.show()

