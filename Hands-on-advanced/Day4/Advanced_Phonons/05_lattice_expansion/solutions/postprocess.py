#!/usr/bin/python

# Generic imports
from pathlib import Path
from vibes.trajectory import reader

trajectories = sorted(Path().glob("qha*/aims/trajectory.son"))

all_atoms = []
for trajectory in trajectories:
    traj = reader(trajectory)
    atoms = traj[-1]
    all_atoms.append(atoms)

# write volume, energy to file
with open("energy-volume.dat", "w") as f:
    for atoms in all_atoms:
        vol = atoms.get_volume()
        e_tot = atoms.get_total_energy()

        f.write(f"{vol:20.10f} {e_tot:20.10e}\n")
