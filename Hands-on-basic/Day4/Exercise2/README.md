# PURPOSE OF THE EXERCISE:
## How to calculate the phonon frequencies of the polar semiconductor AlAs at the Gamma point.
------------------------------------------------------------------------

### Steps to perform:

1. Run the SCF ground-state calculation

        mpirun -np 4 pw.x < AlAs.scf.in > AlAs.scf.out

2. Run the phonon calculation at Gamma

        mpirun -np 4 ph.x < AlAs.ph.in > AlAs.ph.out

3. Impose the acoustic sum rule at the Gamma point and add the non-analytic LO-TO splitting

        mpirun -np 4 dynmat.x < AlAs.dynmat.in > AlAs.dynmat.out
