import matplotlib.pyplot as plt
import numpy as np

# Load data from file
data = np.loadtxt('si.etot_vs_ecut')

# Calculate forward difference
ecut_diff = np.diff(data[:, 1]) / np.diff(data[:, 0])

# Create figure and subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Set grid
axs[0].grid(True)
axs[1].grid(True)

# Set y-axis format for the first subplot
axs[0].yaxis.set_major_formatter('{: .3f}'.format)

# Set labels for subplots
axs[0].set_ylabel('Total energy (Ry)', size =16)
axs[1].set_ylabel('Forward Difference (Ry)', size =16)
axs[1].set_xlabel('ecutwfc (Ry)', size =16)

# Plot total energy
axs[0].plot(data[:, 0], data[:, 1], linestyle='-', linewidth=2, marker='o', markersize=10)

# Plot forward difference
axs[1].plot(data[1:, 0], ecut_diff, linestyle='-', linewidth=2, marker='o', markersize=10)

# Show the plot
plt.tight_layout()
plt.savefig("en_vs_ecut.png", dpi=300, bbox_inches='tight')
plt.show()
