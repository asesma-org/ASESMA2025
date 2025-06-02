# PURPOSE OF THE EXERCISE:
## How to calculate the phonon dispersion of the polar semiconductor AlAs
------------------------------------------------------------------------

### Steps to perform:

N.B. Open all the input files and try to understand them. Then, fill the parts that are left empty before running them.

1. Run the SCF ground-state calculation

        mpirun -np 4 pw.x < AlAs.scf.in > AlAs.scf.out

2. Run the phonon calculation on a uniform grid of q-points

        mpirun -np 4 ph.x < AlAs.ph.in > AlAs.ph.out

3. Fourier transform the Interatomic Force Constants from a uniform grid of q-points to real space: C(q) => C(R)

        mpirun -np 4 q2r.x < AlAs.q2r.in > AlAs.q2r.out

4. Calculate frequencies omega(q') at generic q' points using Interatomic Force Constants C(R)

        mpirun -np 4 matdyn.x < AlAs.matdyn.in > AlAs.matdyn.out

5. Plot the phonon dispersion 

        plotband.x < plotband.AlAs.in > plotband.AlAs.out
        gnuplot plot_dispersion.gp
