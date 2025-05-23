import matplotlib.pyplot as plt
import numpy as np

# Load data from file
data = np.loadtxt('')  #Specify the file where the energy versus vacuum are stored

cell_parameter = data[:, 0] # Size of the cell: vacuum space along x-y (bohr)
Etot = data[:, 1]  # Total energy (Ry)
Ptot = data[:, 2]  # Total pressure (kbar)

## Calculate the energy difference
e_diff = # Fill this part (Hint: look at example3.Si/ex1.exutwfc/plot_etot_ecut.py)
p_diff = #


#  Create figure and subplots
fig, axs = plt.subplots(4, 1, figsize=(16, 12), sharex=True)

# Set grid
axs[0].grid(True)
axs[1].grid(True)
axs[2].grid(True)
axs[3].grid(True)

# Set y-axis format for the first subplot
axs[0].yaxis.set_major_formatter('{: .3f}'.format)

# Set labels for subplots
axs[0].set_ylabel('Total energy (Ry)', size =16)
axs[1].set_ylabel('E difference (Ry)', size =16)
axs[2].set_ylabel('Total pressure (kbar)', size =16)
axs[3].set_ylabel('P difference (kbar)', size =16)
axs[3].set_xlabel('vacuum along the lateral directions (Bohr)', size =16)

# Plot total energy
axs[0].plot(cell_parameter, Etot, color = "green", linestyle='-', linewidth=2, marker='o', markersize=10)

# Plot energy difference
axs[1].plot(cell_parameter, e_diff, color = "green", linestyle='-', linewidth=2, marker='o', markersize=10)

# Plot pressure
axs[2].plot(cell_parameter, Ptot, color = "red", linestyle='-', linewidth=2, marker='o', markersize=10)

# Plot pressure difference
axs[3].plot(cell_parameter, p_diff, color = "red", linestyle='-', linewidth=2, marker='o', markersize=10)

# Show the plot
plt.tight_layout()
plt.savefig("en_p_vs_vacuum_diff.png", dpi=300, bbox_inches='tight')
plt.show()
