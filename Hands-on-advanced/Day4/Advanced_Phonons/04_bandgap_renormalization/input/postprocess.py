#!/usr/bin/env python

import re
import os
import shutil
from os import listdir
from os.path import isfile, join, isdir
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from ase.io import read, write


# Get bandgap function
def get_bandgap(filename="aims.out"):
    # Use regular expressions to match the following line and 
    # extract the bandgap value.
    # For example, "0.86904246" from 
    # "ESTIMATED overall HOMO-LUMO gap:      0.86904246 eV"
    re_pattern = r"ESTIMATED overall HOMO-LUMO gap:\s+([-\d.]+) eV"

    with open(filename) as file:
        for line in file:
            re_match = re.search(re_pattern, line)
            if re_match:
                return float(re_match.group(1))


folders = sorted([f for f in Path(".").glob("samples_*K") if f.is_dir()])
print(f"Processing samples in: {folders}")

# use regular expressions to find 
# what temperatures the samples correspond to
temp_re_pattern = r'samples_(\d+)K'
temp = [int(re.search(temp_re_pattern, folder.name).group(1)) for folder in folders]

gaps = []
gaps_std = []

for samples_dir in folders:

    print(f'Processing directory {samples_dir}')
    os.chdir(samples_dir)

    allfiles = [f for f in Path(".").glob("geometry.in.supercell.*") if f.is_file()]
    band_gaps_at_temperature = []

    for idx, file in enumerate(allfiles):
        os.chdir(f'sample_{idx+1}/aims/calculations/')
        band_gaps_at_temperature.append(get_bandgap(filename="aims.out"))

        os.chdir('../../../')

    gaps.append(np.average(band_gaps_at_temperature))
    gaps_std.append(np.std(band_gaps_at_temperature))

    os.chdir('../')

plt.errorbar(temp, gaps, yerr = gaps_std, fmt = 'o', color = 'black',
             ecolor = 'lightblue', elinewidth = 3, capsize=3)
plt.title('Band Gap vs Temperature', fontsize=16)
plt.xlabel('Temperature, K', fontsize=16)
plt.ylabel('Band Gap, eV', fontsize=16)
plt.grid()
plt.savefig('Band_gap_vs_Temperature.png', dpi=300)
