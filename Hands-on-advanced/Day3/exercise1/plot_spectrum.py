import os
os.environ["MPLCONFIGDIR"] = "/tmp/mplconfig"
os.makedirs("/tmp/mplconfig", exist_ok=True)

import numpy as np
import matplotlib.pyplot as plt

# Load data: column 1 = energy, column 3 = -Im[1/ε]
data = np.loadtxt("silicon.plot_eps.dat")
energy = data[:, 0]
intensity = data[:, 2]

# Create plot
plt.figure(figsize=(8, 6))
plt.plot(energy, intensity, color="magenta", linewidth=2, label=r'$-\mathrm{Im}[1/\varepsilon]$')

# Set plot parameters
plt.xlim(0, 30)
plt.ylim(0, 3)
plt.xticks(np.arange(0, 31, 5))
plt.xlabel("E (eV)", fontsize=14)
plt.ylabel("Intensity (unitless)", fontsize=14)
plt.title("Silicon Energy Loss Spectrum", fontsize=16)
plt.legend()
plt.grid(True)

# Save as PDF
plt.savefig("silicon_spectrum.pdf", format="pdf")
print("Plot saved as silicon_spectrum.pdf")

