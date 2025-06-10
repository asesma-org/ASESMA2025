#!/bin/bash -l

#SBATCH -J phonopy|lise
#SBATCH -o log/phonopy.%j
#SBATCH -e log/phonopy.%j
#SBATCH -D ./
#SBATCH --mail-type=all
#SBATCH --mail-user=knoop@fhi-berlin.mpg.de
#SBATCH --nodes=20
#SBATCH --ntasks-per-node=96
#SBATCH --ntasks-per-core=1
#SBATCH -t 1:0:00
#SBATCH --partition=standard96


vibes run phonopy phonopy.in
