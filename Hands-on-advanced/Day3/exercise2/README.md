## Calculation of the electron energy loss spectra (EELS) of bulk silicon 
## using the turbo_eels.x code (Sternheimer algorithm)
------------------------------------------------------------------------

 1. Run the SCF ground-state calculation

        mpirun -n 2 pw.x < pw.si.scf.in |tee pw.si.scf.out

 2. Solve the Sternheimer equations

        mpirun -n 2 turbo_eels.x < turbo_eels.si.sternheimer.in |tee turbo_eels.si.sternheimer.out

    Note: this calculation is very slow. 

 3. Use the Python3 script `plot_spectrum.py` from the previous exercise
    and adapt it for this exercise to plot the spectrum.

        python3 plot_spectrum.py

    Visualize the spectrum using the generated file silicon_spectrum.pdf

 4. Perform a converge test of EELS with respect to the size of the k mesh:
    consider k meshes 4x4x4, 6x6x6, 8x8x8, 10x10x10.
    To do this, use the Sternheimer (or Lanczos) algorithm.
    Note that Sternheimer is much slower than Lanczos.

 5. Compute and plot the plasmon dispersion, i.e. compute EELS for
    |q| = 0.1, 0.3, 0.5, 0.7, 0.9, 1.1, 1.3 a.u. along the [100] direction.

