import numpy as np
import matplotlib.pyplot as plt


phi = np.loadtxt("COLVAR")
stride = np.array([i for i in range(0,phi.shape[0],20)])
print(np.std(phi[:,1]))
fig, axs = plt.subplots(1,2,figsize=(10,5))
axs[0].set_title(r"$\phi$")
axs[1].set_title(r"$\psi$")

axs[0].plot(phi[stride,0],np.rad2deg(phi[stride,1]),linestyle="none",marker="o",markersize=0.5)
axs[1].plot(phi[stride,0],np.rad2deg(phi[stride,2]),linestyle="none",marker="o",markersize=0.5)

axs[0].legend()
axs[0].set_xlabel("Time (ns)")
axs[1].set_xlabel("Time (ns)")
plt.show()
