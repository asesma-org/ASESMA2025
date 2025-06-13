import numpy as np
import matplotlib.pyplot as plt

fes = np.loadtxt("fes.dat")

phi = np.rad2deg(fes[:,0])
psi = np.rad2deg(fes[:,1])
fes = fes[:,2]

phii = np.unique(phi)
psii = np.unique(psi)

phi_grid, psi_grid = np.meshgrid(phii,psii)
free_energy = fes.reshape(len(phii),len(psii))


contour = plt.contourf(phi_grid,psi_grid,free_energy,levels=50,cmap="viridis")
plt.colorbar(contour,label="Free Energy (kj/mol)")
plt.xlabel(r"$\phi$")
plt.ylabel(r"$\psi$")
plt.show()
