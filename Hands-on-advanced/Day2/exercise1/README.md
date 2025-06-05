# Run the calculations in the following way:

## exercise-1.a 

Calculation of the projected density of states (PDOS) of CoO from DFT (PBEsol)

  mpirun -n 2 pw.x < CoO.scf.in |tee CoO.scf.out

  mpirun -n 2 pw.x < CoO.nscf.in |tee CoO.nscf.out

  mpirun -n 2 projwfc.x < CoO.projwfc.in |tee CoO.projwfc.out

  python3 plot_pdos.py

  Visualize the file CoO_PDOS.pdf

## exercise-1.b
 
Calculation of the Hubbard U parameter for the Co-3d states.
Modify the CoO.scf.in file by adding the HUBBARD card (see slides).

  mpirun -n 2 pw.x < CoO.scf.in |tee CoO.scf.out

  mpirun -n 2 hp.x < CoO.hp.in |tee CoO.hp.out

## exercise-1.c

Calculation of the projected density of states (PDOS) of CoO from DFT+U.
To do this, please make the same steps as in exercise 1.a and use the Hubbard U
value that you determined in exercise 1.b. This requires modifying the 
files CoO.scf.in and CoO.nscf.in. Also, in the script plot_pdos.py use the 
Fermi energy that is printed at the end of the Co.scf.out file.
Then compare the PDOS from DFT and DFT+U. Which conclusions can you make?

