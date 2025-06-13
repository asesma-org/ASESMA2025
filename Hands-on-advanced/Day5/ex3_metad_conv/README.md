################## EX 3######################
we now know the free energies as a function of two collective variables phi and psi
it is important for these to be converged so one way to do this is to check the fes per some nstride deposited gaussians 
run the following command to do this

plumed sum_hills --hills HILLS --stride 500 --mintozero
