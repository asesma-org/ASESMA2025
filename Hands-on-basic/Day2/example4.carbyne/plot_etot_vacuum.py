import matplotlib.pyplot as plt
import numpy as np

# Load data from file
data = np.loadtxt('c.etot_vs_vacuum')
cell_parameter = data[:, 0] # Size of the cell: vacuum space along x-y (bohr)
Etot = data[:, 1]  # Total energy (Ry)
Ptot = data[:, 2]  #Total pressure (kbar)

#  Create figure and subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Set grid
axs[0].grid(True)
axs[1].grid(True)

# Set y-axis format for the first subplot
axs[0].yaxis.set_major_formatter('{: .3f}'.format)

# Set labels for subplots
axs[0].set_ylabel('Total energy (Ry)', size =16)
axs[1].set_ylabel('Total stress (kbar)', size =16)
axs[1].set_xlabel('vacuum along the lateral directions (Bohr)', size =16)

# Plot total energy
axs[0].plot(cell_parameter, Etot, color = "green", linestyle='-', linewidth=2, marker='o', markersize=10)

# Plot forward difference
axs[1].plot(cell_parameter, Ptot, color = "red", linestyle='-', linewidth=2, marker='o', markersize=10)

# Show the plot
plt.tight_layout()
plt.savefig("en_vs_vacuum.png", dpi=300, bbox_inches='tight')
plt.show()
