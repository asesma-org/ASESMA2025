import os
os.environ["MPLCONFIGDIR"] = "/tmp/mplconfig"
os.makedirs("/tmp/mplconfig", exist_ok=True)

import matplotlib.pyplot as plt
import numpy as np

# Load data
data1 = np.loadtxt("CoO.pdos_atm#1(Co1)_wfc#3(d)")
data2 = np.loadtxt("CoO.pdos_atm#2(Co2)_wfc#3(d)")
data3 = np.loadtxt("CoO.pdos_atm#3(O)_wfc#2(p)")

# Energy offset
E_F = 15.79

# Plot
plt.figure(figsize=(8, 6))
plt.plot(data1[:,0] - E_F, data1[:,1], label='Co-3d (majority spin)', color='red', linewidth=2)
plt.plot(data2[:,0] - E_F, data2[:,1], label='Co-3d (minority spin)', color='green', linewidth=2)
plt.plot(data3[:,0] - E_F, data3[:,1], label='O-2p', color='blue', linewidth=2)

plt.axvline(0, color='black', linestyle='--', linewidth=1)
plt.xlabel("E - E_F (eV)")
plt.ylabel("PDOS (states/eV/atom)")
plt.xlim([-10, 8])
plt.ylim([0, 6.5])
plt.xticks(np.arange(-10, 9, 2))
plt.yticks(np.arange(0, 7, 1))
plt.legend()
plt.tight_layout()
plt.savefig("CoO_PDOS.pdf")

