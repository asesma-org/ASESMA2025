"""script to run all aims calculations in the directories created from preprocess.py"""
#!/usr/bin/env python

from ase.io import read
import os
import shutil
from pathlib import Path
import re
import numpy as np

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

# Process all samples
band_gaps_at_temperature = []
allfiles = [f for f in Path(".").glob("geometry.in.supercell.*") if f.is_file()]
for idx, file in enumerate(allfiles):

    # Run calculation for one sample
    atoms = read(f'{file}', format='aims')

    Path(f"sample_{idx+1}").mkdir(parents=True, exist_ok=True)
    os.chdir(f'sample_{idx+1}')

    atoms.write('geometry.in', format='aims')
    shutil.copy('../aims.in', './')
    os.system('vibes run singlepoint')

    band_gaps_at_temperature.append(get_bandgap(filename="aims/calculations/aims.out"))

    os.chdir('../')

# Final Output
print("Average band gap value is ", np.average(band_gaps_at_temperature), " eV")
    
