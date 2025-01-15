import matplotlib.pyplot as plt
import numpy as np

# Load data from file
data = np.loadtxt('data.dat', skiprows=1, delimiter=',')

# Set grid
plt.grid(True)

# Set y-axis format
plt.gca().yaxis.set_major_formatter('{: .3f}'.format)

# Set x-axis format
plt.gca().xaxis.set_major_formatter('{: .1f}'.format)

# Set labels
plt.ylabel('Total energy (Ry)', size =16)
plt.xlabel('Lattice parameter (Bohr)', size =16)

# Plot data
plt.plot(data[:, 0], data[:, 2], linestyle='-', linewidth=2, marker='o', markersize=10)
plt.savefig("alat_scan.png", dpi=300, bbox_inches='tight')

# Show the plot
plt.show()
