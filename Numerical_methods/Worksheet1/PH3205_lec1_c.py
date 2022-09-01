import math
import numpy as np
import matplotlib.pyplot as plt

def func(x): #function
    return math.exp(x)

def d_f(x): #exact derivative of function
    return math.exp(x)

def rel_error(a,b): #defined relative error
    return math.log(float(abs(a-b))/b)

def error(a,b):
    return float(abs(a-b))/b

def d2_f(x,h):
    return float(func(x+h)+func(x-h)-2*func(x))/(h**2)

x_range = np.linspace(1,10,10)
#h_range = np.linspace(10**(-6),10**(-1), 6 )

h_range = [10**(-i) for i in range(1,7)]

#print(h_range)

table = np.zeros((len(x_range), len(h_range)))

for i in range(len(x_range)):
    for j in range(len(h_range)):
        table[i][j] = rel_error(d2_f(x_range[i],h_range[j]), d_f(x_range[i]))


with np.printoptions(threshold=np.inf):
    print(table)
    

#error = [abs(d_f(x) - d_f2(x,h))/d_f(x) for h in h_range]

fig, ax = plt.subplots(figsize=(20, 10))

for i in range(len(x_range)):
    plt.plot(h_range,table[i], label = "%f" %x_range[i])

plt.legend(loc="upper left")

plt.xlabel('values of h')
plt.ylabel('relative error (log scale)')


ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.60)

plt.show()


#The dip in the graph occurs around x = 0.0001. Thus this is the optimal h
