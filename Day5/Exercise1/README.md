# PURPOSE OF THE EXERCISE:
## How to calculate the phonon frequencies of silicon at the Gamma point
------------------------------------------------------------------------

### Steps to perform:

1. Run the SCF ground-state calculation

        mpirun -np 4 pw.x < Si.scf.in > Si.scf.out             

2. Run the phonon calculation

        mpirun -np 4 ph.x < Si.ph.in > Si.ph.out

3. Impose the acoustic sum rule at the Gamma point

        mpirun -np 4 dynmat.x < Si.dynmat.in > Si.dynmat.out
