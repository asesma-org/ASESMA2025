# Run the calculations in the following way:

## exercise-1.a 

Calculation of the projected density of states (PDOS) of CoO from DFT (PBEsol)

  pw.x < CoO.scf.in |tee CoO.scf.out

  pw.x < CoO.nscf.in |tee CoO.nscf.out

  projwfc.x < CoO.projwfc.in |tee CoO.projwfc.out

  gnuplot plot_pdos.gp

  evince CoO_PDOS.eps

## exercise-1.b
 
Calculation of the Hubbard U parameter for the Co-3d states.
Modify the CoO.scf.in file by adding the HUBBARD card (see slides).

  pw.x < CoO.scf.in |tee CoO.scf.out

  hp.x < CoO.hp.in |tee CoO.hp.out

## exercise-1.c

Calculation of the projected density of states (PDOS) of CoO from DFT+U.
To do this, please make the same steps in Exercise 1.a and use the Hubbard U
value that you determined in Exercise 1.b. This requires modifying the 
files CoO.scf.in and CoO.nscf.in. Also, in the script plot_pdos.gp use the 
Fermi energy that is printed at the end of the Co.nscf.out file.
Then compare the PDOS from DFT and DFT+U. Which conclusions can you make?
