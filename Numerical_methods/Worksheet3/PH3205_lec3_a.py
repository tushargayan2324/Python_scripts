import numpy as np
import matplotlib.pyplot as plt

l = 2 # lambda
w = 4 #omega

def f(x,v,t): # f := dy/dt
    return v

def df(x,v,t): # df/dt = d2y/dt2
    return -2*l*w*v - x*(w**2)

h=0.001 # timesteps
time_range = 10.0 #seconds

N = int(time_range/h)

t = np.linspace(0, time_range, N+1)
#print(t)
x = np.zeros((N+1,1)) #x range
v = np.zeros((N+1,1)) #v range

x[0] = 1 #Initial x value
v[0] = 0 #Initial v value


for i in range(0,len(t)-1):
    k1=h*f(x[i],v[i],t[i])
    v1=h*df(x[i],v[i],t[i])
    k2=h*f(x[i]+k1/2,v[i]+v1/2,t[i]+h/2)
    v2=h*df(x[i]+k1/2,v[i]+v1/2,t[i]+h/2)
    k3=h*f(x[i]+k2/2,v[i]+v2/2,t[i]+h/2)
    v3=h*df(x[i]+k2/2,v[i]+v2/2,t[i]+h/2)
    k4=h*f(x[i]+k3,v[i]+v3,t[i]+h)
    v4=h*df(x[i]+k3,v[i]+v3,t[i]+h)
    x[i+1]=x[i] + (k1+2*k2+2*k3+k4)/6
    v[i+1]=v[i] + (v1+2*v2+2*v3+v4)/6


plt.plot(t,x)
plt.xlabel("time")
plt.ylabel("displacement")
plt.title("lambda = %s"%l)
plt.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.60)
plt.show()
