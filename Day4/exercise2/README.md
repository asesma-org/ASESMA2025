exercise-2.a: Perform convergence tests of the total energy of Si using the 
              PBE0 functional and x_gamma_extrapolation = .true.
              Use q-point meshes 1x1x1, 2x2x2, 4x4x4, 8x8x8.

              mpirun -np 2 pw.x < Si.scf.in |tee Si.scf.out

exercise-2.b: Perform convergence tests of the total energy of Si (as above) 
              using the PBE0 functional and x_gamma_extrapolation = .false.

              In which case the convergence is faster?
