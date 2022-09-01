import math
import numpy as np
import matplotlib.pyplot as plt

def func(x):
#    return  float(1)/(x**2 + (np.cos(x))**2 ) #np.exp(-(x**2))
    return np.exp(-x)*x**(-0.2)

def simp_int_1(x,h):
    return float(h*( func(x+h) + func(x-h) + 4*func(x) ) )/3

def simp_int(a,b,h):

    x = a+h
    S_func = 0

    while x+h < b:
        S_func += simp_int_1(x,h)
        x += 2*h
    return S_func


def simp_int_new(a,b,h):
    n = int(abs(float(b-a)/h))
    
    x = np.linspace(a,b,n)
    y = func(x) #np.exp(-(x**2))
    print(y)
    
    Simp_int = h*( y[0] + y[n-1] + 2*sum(y[:n-2:2]) + 4*sum(y[1:n-1:2]) )/3
    
    return Simp_int


print(simp_int_new(0.00001,1,0.00001))

h_range = np.linspace(10**-6,1,10**3)

h_range_log = np.linspace(-6,-0.1,6)

#print(h_range)

lit_value = 1.4936482656248540507989348722637060107089993736253  #Value of integral from other sources hopefully precise

#error = [ abs(lit_value - simp_int(-1,1,h))/lit_value for h in h_range]

#error_log = [ (abs(lit_value - simp_int_new(-1,1,10**(-h)))/lit_value) for h in h_range_log]


fig, ax = plt.subplots(figsize=(20, 10))

#ax.scatter(h_range,error ,s=2 ,alpha=0.70)
#ax.scatter(h_range_log,error_log ,s=2 ,alpha=0.70)


plt.legend(loc="upper left")

plt.xlabel('values of h')
plt.ylabel('error')

ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.60)

plt.show()

