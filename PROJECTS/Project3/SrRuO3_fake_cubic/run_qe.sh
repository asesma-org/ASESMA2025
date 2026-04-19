
# run the scf calculation
mpirun -n 4 pw.x -i sro.scf.in | tee vo.scf.out


# OPTIONAL: run the DFT bandstructure calculation
mpirun -n 4 pw.x -i sro.bnd.in | tee sro.bnd.out
mpirun -n 4 bands.x -i sro.bands.in | tee sro.bands.out


# run the nscf calculation
mpirun -n 4 pw.x -i sro.nscf.in | tee sro.nscf.out

# Wannierize

## pre-process wannier90
wannier90.x -pp sro
## run interface wannier90-quantum espresso
mpirun -n 4 pw2wannier90.x -i sro.pw2wan.in | tee sro.pw2wan.out
## run wannier90
wannier90.x sro

# Interface with TRIQS, this will create the sro.h5 archive to start the calculation
python3 ./convert_wannier.py
