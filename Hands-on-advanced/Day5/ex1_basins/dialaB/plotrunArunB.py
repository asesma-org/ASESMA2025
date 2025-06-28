import numpy as np
import matplotlib.pyplot as plt


phi_psiB = np.loadtxt("COLVAR")
phi_psiA = np.loadtxt("../dialaA/COLVAR")
plt.scatter(np.rad2deg(phi_psiA[:,1]),np.rad2deg(phi_psiA[:,2]),label="run A")
plt.scatter(np.rad2deg(phi_psiB[:,1]),np.rad2deg(phi_psiB[:,2]),label="run B")
plt.legend()
plt.xlabel(r"$\phi$")
plt.ylabel(r"$\psi$")
plt.show()
