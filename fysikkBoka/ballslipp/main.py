# Program ballposisjon.py
import numpy as np
import matplotlib.pyplot as plt

# Leser t- og s-verdier inn i lister
data = np.loadtxt('ballslipp.txt')
t = data[:,0]
s = data[:, 1]

# Tegner posisjonsgrafen

plt.figure(1)
plt.plot(t, s)
plt.grid()
plt.title("Posisjon")

plt.xlabel("$t$ / s")
plt.ylabel("$s$ / m")




plt.show()



