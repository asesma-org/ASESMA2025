PURPOSE OF THE EXERCISE:
How to calculate Band structure for Aluminum

 Run the calculations in the following way:

  1. pw.x < al.scf.in | tee al.scf.out

  2. pw.x < al.bands.in | tee al.bands.out

  3. bands.x < bands.in | tee bands.out

  4. find the Fermi energy using cat al.scf.out | grep "Fermi"

  5. gnuplot plot_bands.gp

Homework: Optimize the k-points and ecutwfc for Al. The folder `convergence_test` contains the necessary files.







