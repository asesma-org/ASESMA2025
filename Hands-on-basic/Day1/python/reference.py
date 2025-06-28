#%%
import numpy as np

# Read the data from the file
data = np.loadtxt('Etot-vs-alat.dat', delimiter=',')

# Extract the alat and Etot columns
alat = data[:, 0]
Etot = data[:, 1]

# Print the arrays (optional)
print("alat:", alat)
print("Etot:", Etot)

import matplotlib.pyplot as plt

# Plot the data
plt.plot(alat, Etot, label="Si", marker='o')
plt.xlabel("Lattice constant [Angstrom]", size=14)
plt.ylabel("Etot [Ry]", size=14)
plt.legend()
plt.title("Silicon bulk energy")
plt.grid(True)
plt.savefig("Etot_vs_alat.png", bbox_inches='tight', dpi=300)
# plt.show()