import numpy as np
import matplotlib.pyplot as plt


phi_psiA = np.loadtxt("COLVAR")
phi_psiB = np.loadtxt("../dialaB/COLVAR")
#print(np.std(phi_psiA[:,1]))
#print(np.std(phi_psiB[:,2]))

fig, axs = plt.subplots(1,2,figsize=(10,5))
axs[0].plot(phi_psiA[:,0]/1000,phi_psiA[:,1],label="run A")
axs[0].plot(phi_psiB[:,0]/1000,phi_psiB[:,1],label="run B")

axs[1].plot(phi_psiA[:,0]/1000,phi_psiA[:,2],label="run A")
axs[1].plot(phi_psiB[:,0]/1000,phi_psiB[:,2],label="run B")


#axs[1].plot(phi_psi[:,0],phi_psi[:,2])
#axs[1].plot(phi_psi[:,1],phi_psi[:,2],marker='o',linestyle='none')
axs[0].legend()
axs[1].legend()

axs[0].set_ylabel(r"$\phi$")
axs[1].set_ylabel(r"$\psi$")
axs[0].set_xlabel("Time (ns)")
axs[1].set_xlabel("Time (ns)")
plt.show()
