import math
import numpy as np
import matplotlib.pyplot as plt


def simp_int_new(a,b,h):
    n = int(float(abs(b-a))/h)
    x = np.linspace(a, b, n)
    y = np.exp(-(x**2))
    S_func = h*(y[0] + 2*sum(y[:n-2:2]) + 4*sum(y[1:n-1:2]) + y[n-1])/3
    return S_func

#print(simp_int_new(-1,1,0.0000001))

h_range = np.linspace(10**-6,1,10**6)

h_range_log = np.log10(h_range)

lit_value = 1.4936482656248540507989348722637060107089993736253  #Value of integral from other sources hopefully precise

#error_log = [ math.log10(abs(lit_value - simp_int_new(-1,1,10**(-h) ) )/lit_value) for h in h_range_log]

#error_log = np.log10( [abs(lit_value - simp_int_new(-1,1,10**(-h_range_log))) ] )

error = [abs(lit_value - simp_int_new(-1,1,h)) for h in h_range ]

error_log = np.log10(error)

fig, ax = plt.subplots(figsize=(20, 10))

#ax.scatter(h_range,error ,s=2 ,alpha=0.70)
#plt.plot(h_range,error)
plt.plot(h_range_log,error_log)


plt.legend(loc="upper left")

plt.xlabel('values of h (logscale)')
plt.ylabel('error (logscale)')

ax.grid(color='grey', linestyle='-', linewidth=0.25, alpha=0.60)

plt.show()

