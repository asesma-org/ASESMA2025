import matplotlib.pyplot as plt

# Set the plot style
plt.rcParams['font.size'] = 20
plt.rcParams['lines.markersize'] = 10

# Data points for plotting
x = []
y1 = []
y2 = []
y3 = []
y4 = []
y5 = []
y6 = []

# Read data from file
with open("data-g", "r") as file:
    next(file)
    for line in file:
        values = line.split()
        x.append(float(values[0]))
        y1.append(float(values[1]))
        y2.append(float(values[2]))
        y3.append(float(values[3]))
        y4.append(float(values[4]))
        y5.append(float(values[5]))
        y6.append(float(values[6]))

# Create the plot
plt.figure(figsize=(6, 6))
plt.plot(x, y1, 'o-', color='orange', linewidth=3, label='degauss-0.01')
plt.plot(x, y2, 'o-', color='blue', linewidth=3, label='degauss-0.03')
plt.plot(x, y3, 'o-', color='black', linewidth=3, label='degauss-0.05')
plt.plot(x, y4, 'o-', color='red', linewidth=3, label='degauss-0.07')
plt.plot(x, y5, 'o-', color='purple', linewidth=3, label='degauss-0.09')
plt.plot(x, y6, 'o-', color='green', linewidth=3, label='degauss-0.11')

# Set the plot labels
plt.xlabel('k-point mesh')
plt.ylabel('Energy (eV)')

# Set the legend position
plt.legend(loc='upper center')

# Save the plot to a file
plt.savefig('gauss.png', format='png', dpi=300, bbox_inches='tight')

# Display the plot
plt.show()
