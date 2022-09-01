import math
import numpy as np
import matplotlib.pyplot as plt

exact_int = float(7*math.exp(8)+1)/4

def func(x):
    return float((4*x + 4)*math.exp(4*x+4)) #By changing interval to [-1,1] and coodinate transformation


def g_quad_2(func):
    return func(1/(math.sqrt(3))) + func(-1/(math.sqrt(3)))

def g_quad_3(func):
    return 8*func(0)/9 + 5*(func(0.774597) + func(-0.774597))/9

def g_quad_4(func):
    return 0.652145*(func(0.339981) + func(-0.339981)) + 0.347855*(func(-0.861136)+func(0.861136))

def g_quad_5(func):
    return 0.568889*func(0) + 0.478629*(func(0.538469) + func(-0.538469)) + 0.236927*(func(0.90618) + func(-0.90618))



print(g_quad_2(func)-exact_int)

print(g_quad_3(func)-exact_int)

print(g_quad_4(func)-exact_int)

print(g_quad_5(func)-exact_int)

fig, ax = plt.subplots(figsize=(20, 10))

n = [2,3,4,5]

int_values = [ g_quad_2(func), g_quad_3(func), g_quad_4(func),g_quad_5(func)  ]

error = [ exact_int - i for i in int_values ]

ax.scatter(n,error ,s=40 ,alpha=0.70)


plt.legend(loc="upper left")

plt.xlabel('values of n')
plt.ylabel('error')

ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.60)

plt.show()

