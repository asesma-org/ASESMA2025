PURPOSE OF THE EXERCISE:
How to calculate Band structure for Silicon

 Run the calculations in the following way:

  1. pw.x -in si.scf.in| tee si.scf.out  # unlike the previous ">" , the "tee" command print the output also on the terminal

  2. pw.x -in si.bands.in | tee si.bands.out

  3. bands.x -in bands.in | tee bands.out

  4. find the Fermi energy (Homo level) using "cat si.scf.out | grep "highest occupied level"

  5. gnuplot plot_bands.gp









