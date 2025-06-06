import matplotlib.pyplot as plt
import numpy as np

# Load data from file
data_even = np.loadtxt('si.etot_vs_kgrid_even')
data_odd = np.loadtxt('si.etot_vs_kgrid_odd')

x_even = data_even[:,0]  # The first column of the file : k-points
y_even = data_even[:,1]  # The second column of the file: total energy (Ry)
x_odd = data_odd[:,0]  # The first column of the file : k-points
y_odd = data_odd[:,1]  # The second column of the file: total energy (Ry)

# Calculate the energy difference
#(we reference to the last energy value, the one with the higher k-point)
even_diff = y_even-y_even[-1]  
odd_diff = y_odd - y_odd[-1]

# Create figure and subplots
fig, axs = plt.subplots(2, 1, figsize=(8, 6), sharex=True)

# Set grid
axs[0].grid(True)
axs[1].grid(True)

# Set y-axis format for the first subplot
axs[0].yaxis.set_major_formatter('{: .3f}'.format)

# Set labels for subplots
axs[0].set_ylabel('Total energy (Ry)', size =16)
axs[1].set_ylabel('Energy Difference (Ry)', size =16)
axs[1].set_xlabel('Kgrid', size=16)

# Plot total energy
axs[0].plot(x_even, y_even, linestyle='-', linewidth=2, marker='o', markersize=10,label='even kgrid')
axs[0].plot(x_odd, y_odd, linestyle='-', linewidth=2, marker='x', markersize=10,label='odd kgrid')

# Plot difference
axs[1].plot(x_even, even_diff, linestyle='-', color = "purple", linewidth=2, marker='o', markersize=10,label='even kgrid')
axs[1].plot(x_odd, odd_diff, linestyle='-', color= "red", linewidth=2, marker='x', markersize=10,label='odd kgrid')

# Show the plot
plt.tight_layout()
plt.legend()
plt.savefig("en_vs_kgrid.png", dpi=300, bbox_inches='tight')
plt.show()
