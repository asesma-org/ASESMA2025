import numpy as np
import matplotlib.pyplot as plt


phi = np.loadtxt("COLVAR")
print(np.std(phi[:,2]))
plt.plot(phi[:,0],np.rad2deg(phi[:,2]))

plt.ylabel(r"$\psi$")
plt.xlabel("Time (ns)")
plt.show()
