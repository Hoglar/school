# Program ballposisjon.py
import numpy as np
import matplotlib.pyplot as plt

# Leser t- og s-verdier inn i lister
data = np.loadtxt('ballslipp.txt')
t = data[:,0]
s = data[:, 1]

n = len(t)
v = np.zeros(n)

# Beregne fart

for i in range(1, n):
    v[i] = (s[i]-s[i-1])/(t[i]-t[i-1])

# Tegner fartsgrafen

plt.figure(1)
plt.plot(t, v)
plt.grid()
plt.title("Fart")

plt.xlabel("$t$ / s")
plt.ylabel("$v$ / m/s")




plt.show()



