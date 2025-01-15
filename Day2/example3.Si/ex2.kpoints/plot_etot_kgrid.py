import matplotlib.pyplot as plt
import numpy as np

# Load data from file
data_even = np.loadtxt('si.etot_vs_kgrid_even')
data_odd = np.loadtxt('si.etot_vs_kgrid_odd')

# Calculate forward difference
even_diff = np.diff(data_even[:, 1]) / np.diff(data_even[:, 0])
odd_diff = np.diff(data_odd[:, 1]) / np.diff(data_odd[:, 0])

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
axs[1].set_xlabel('Kgrid', size=16)

# Plot total energy
axs[0].plot(data_even[:, 0], data_even[:, 1], linestyle='-', linewidth=2, marker='o', markersize=10,label='even kgrid')
axs[0].plot(data_odd[:, 0], data_odd[:, 1], linestyle='-', linewidth=2, marker='x', markersize=10,label='odd kgrid')

# Plot forward difference
axs[1].plot(data_even[1:, 0], even_diff, linestyle='-', linewidth=2, marker='o', markersize=10,label='even kgrid')
axs[1].plot(data_odd[1:, 0], odd_diff, linestyle='-', linewidth=2, marker='x', markersize=10,label='odd kgrid')

# Show the plot
plt.tight_layout()
plt.legend()
plt.show()
