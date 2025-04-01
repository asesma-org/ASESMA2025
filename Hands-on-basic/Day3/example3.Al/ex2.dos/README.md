PURPOSE OF THE EXERCISE:
How to calculate Density of State for Aluminum and how to project it onto the atomic orbitals

1. scf file (al.scf.in)
To run the file, execute:
pw.x < al.scf.in | tee al.scf.out

2. nscf file (al.nscf.in)
To run the file, execute:
pw.x < al.nscf.in | tee al.nscf.out

3. dos file (al.dos.in)
To run the file, execute:
dos.x < al.dos.in | tee al.dos.out

4. plot using gnuplot
Execute:
gnuplot plot_dos.gp

5. Atomic projected dos file (al.pdos.in)
To run the file, execute:
projwfc.x < al.pdos.in | tee al.pdos.out

6. plot using gnuplot
Execute:
gnuplot plot_pdos.gp

To visualize the result, use a pdf reader to open `al_DOS.eps` and `al_pdos.eps`
