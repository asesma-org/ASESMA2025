PURPOSE OF THE EXERCISE:
How to calculate Density of State for Silicon and how to project it onto the atomic orbitals

1. scf file (si.scf.in)
To run the file, execute:
pw.x < si.scf.in | tee si.scf.out

2. nscf file (si.nscf.in)
To run the file, execute:
pw.x < si.nscf.in | tee si.nscf.out

3. dos file (si.dos.in)
To run the file, execute:
dos.x < si.dos.in | tee si.dos.out

4. plot using gnuplot
Execute:
gnuplot plot_dos.gp

5. Atomic projected dos file (si.pdos.in)
To run the file, execute:
projwfc.x < si.pdos.in | tee si.pdos.out

6. plot using gnuplot
Execute:
gnuplot plot_pdos.gp

To visualize the result, use a pdf reader to open `Si_DOS.eps` and `Si_pdos.eps`
