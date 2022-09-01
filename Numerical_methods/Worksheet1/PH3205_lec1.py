import math
import numpy as np
import matplotlib.pyplot as plt


def func(x): #function
    return 2 + 3*(x**2)

def d_f(x): #exact derivative of function
    return 6*x

def rel_error(a,b): #defined relative error
    return math.log(float(abs(a-b))/b)


def d_f2(x,h): #defined num derivative
    return float(func(x+h)-func(x))/h
    
def d_f3(x,h): # Central difference derivative definition
    return float(func(x+h)-func(x-h))/(2*h)

x = 2.3

h_range = np.linspace(10**(-6),10**(-1), 10**3 )

error = [abs(d_f(x) - d_f2(x,h))/d_f(x) for h in h_range]

fig, ax = plt.subplots(figsize=(20, 10))
ax.scatter(h_range,error ,s=2 ,alpha=0.70)

plt.legend(loc="upper left")

plt.xlabel('values of h')
plt.ylabel('error')


ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.60)

plt.show()

plt.show()

error_3 = [abs(d_f(x) - d_f3(x,h))/d_f(x) for h in h_range]
#print(error_3)

print(sum(error_3)/len(error), "The error for f'3 is almost zero. This is because of the limitation of the precision of the machine and language")

