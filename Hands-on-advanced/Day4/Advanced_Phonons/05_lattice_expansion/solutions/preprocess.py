#!/usr/bin/env python

# Generic imports
import shutil
from pathlib import Path

# Reference for conveniently representing a path in python:
#   docs.python.org/3/library/pathlib.html

# ASE
from ase.io import read

# Read input geometry, save the lattice constant and convert to phonopy atoms object
initial_atoms = read("geometry.in", format="aims")

scale_factors = [0.96, 0.98, 1.0, 1.02, 1.04]

print(f"Initial volume:           {initial_atoms.get_volume():.3f} \u212B^3")
for ii, factor in enumerate(scale_factors):
    unitcell = initial_atoms.copy()
    unitcell.set_cell(initial_atoms.cell * factor, scale_atoms=True)
    volume = unitcell.get_volume()
    # create working directory and store input files
    workdir = Path(f"qha_{volume:.3f}")
    workdir.mkdir(exist_ok=True)
    unitcell.write(str(workdir / "geometry.in"), format="aims", scaled=True)
    shutil.copy("phonopy.in", workdir)
    shutil.copy("aims.in", workdir)

    # prompt what we've done:
    print(f"Volume of sample {ii:4d}:    {unitcell.get_volume():.3f} \u212B^3")
    print(f"Input files written to:   {workdir}")
