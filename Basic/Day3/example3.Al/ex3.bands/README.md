PURPOSE OF THE EXERCISE:
How to calculate Band structure for Aluminum

 Run the calculations in the following way:

  1. pw.x < al.scf.in | tee al.scf.in

  2. pw.x < al.bands.in | tee al.bands.in

  3. bands.x < bands.in | tee bands.out

  4. gnuplot plot.gp









