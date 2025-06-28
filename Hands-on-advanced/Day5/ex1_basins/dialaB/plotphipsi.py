import numpy as np
import matplotlib.pyplot as plt


phi = np.loadtxt("COLVAR")
print(np.std(phi[:,1]))
fig, axs = plt.subplots(1,2,figsize=(10,5))
axs[0].plot(phi[:,0],np.rad2deg(phi[:,1]),label=r"$\phi$")
axs[0].plot(phi[:,0],np.rad2deg(phi[:,2]),label=r"$\psi$")
axs[1].scatter(np.rad2deg(phi[:,1]),np.rad2deg(phi[:,2]))

axs[0].legend()
axs[0].set_xlabel("Time (ns)")
axs[1].set_xlabel(r"$\phi$")
axs[1].set_ylabel(r"$\psi$")
plt.show()
