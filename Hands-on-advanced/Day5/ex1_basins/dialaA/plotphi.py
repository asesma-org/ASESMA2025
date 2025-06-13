import numpy as np
import matplotlib.pyplot as plt


phi = np.loadtxt("COLVAR")
print(np.std(phi[:,1]))
plt.plot(phi[:,0],np.rad2deg(phi[:,1]))

plt.ylabel(r"$\phi$")
plt.xlabel("Time (ns)")
plt.show()
