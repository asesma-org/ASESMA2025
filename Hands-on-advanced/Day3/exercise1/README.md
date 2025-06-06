## Calculation of the electron energy loss spectra (EELS) of bulk silicon 
## using the turbo_eels.x code (Lanczos algorithm)
------------------------------------------------------------------------

 1. Run the SCF ground-state calculation

        mpirun -n 2 pw.x < pw.si.scf.in |tee pw.si.scf.out

 2. Perform Lanczos recursions

        mpirun -n 2 turbo_eels.x < turbo_eels.si.lanczos.in |tee turbo_eels.si.lanczos.out

 3. Run the post-processing spectrum calculation

        mpirun -n 2 turbo_spectrum.x < turbo_spectrum.si.in |tee turbo_spectrum.si.out

 4. Plot the spectrum using Python3 and the script `plot_spectrum.py`. 

        python3 plot_spectrum.py
    
    Visualize the spectrum using the generated file silicon_spectrum.pdf

 5. Perform a converge test of EELS with respect to the number of 
    Lanczos iterations in two ways:
    - without extrapolation (extrapolation = 'no')  for 500, 1000, and 1500 iterations;
    - with    extrapolation (extrapolation = 'osc') for 500, 1000, and 1500 iterations.
    
    Note: For each new calculation, change the name of the input and output files 
          (e.g. turbo_eels.si.lanczos.500.in, turbo_eels.si.lanczos.500.out;
                turbo_spectrum.si.500.in,     turbo_spectrum.si.500.out)
    
    What conclusion can you make by comparing the results?
