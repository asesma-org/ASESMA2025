import matplotlib.pyplot as plt
import numpy as np

# Define the folder names and corresponding file names
folder_names = ['gaussian', 'marzari-vanderbilt', 'methfessel-paxton']
file_names = ['data-g', 'data-mv', 'data-mp']

# Initialize a list to store the extracted data for each method
method_data = []

# Iterate over the folder and file names
for folder, file in zip(folder_names, file_names):
    # Construct the file path
    file_path = f'{folder}/{file}'

    # Read the file and extract the data from the third line
    with open(file_path, 'r') as f:
        lines = f.readlines()
        data_line = lines[2].strip().split()
        method_data.append([float(value) for value in data_line[1:]])

# Convert the method data into a NumPy array
method_data = np.array(method_data)
plt.figure(figsize=(6, 6))

# Plot the data for each method
methods = ['Gaussian', 'Marzari-Vanderbilt', 'Methfessel-Paxton']
x_values = [0.01, 0.03, 0.05, 0.07, 0.09, 0.11]

for i, method in enumerate(methods):
    plt.plot(x_values, method_data[i], '-o',label=method, linewidth=3)

# Add labels and title to the plot
plt.xlabel('Degauss')
plt.ylabel('Energy')
plt.title('Energy vs Degauss for Different Methods')

# Add a legend
plt.legend()

# Set the figure size to 6x6 inches


# Save the figure as a PNG file
plt.savefig('smearing_comp.png', dpi=300, bbox_inches='tight')

plt.show()
