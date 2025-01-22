# PURPOSE OF THE EXERCISE:
## Convergence pw.x calculations of a simple bulk system (Silicon bulk)
-----------------------------------------------------------------------

Exercise consists of several examples, the first two being the
convergence tests for the cutoff energy (`ecutwfc`) and k-points.

Convergence tests are typically performed by making a series of
calculations with aid of shell-scripts, e.g., see
the shell-script: `ex1.ecutwfc/scan_ecut.sh`

In this tutorial we are going to use shell scripts to perform a series of calculations

**Logic of examples:** convergence tests for Si bulk consist of the
following steps: 
1. converge the basis-set 
2. converge the k-points 
3. with converged basis-set and k-points calculate lattice-parameter
   of Si bulk
4. with converged basis-set, k-points, and lattice parameter, 
   fit the bulk modulus of si.

**Description of examples:**

* `ex1.ecutwfc/` -- convergence tests for cutoff energy

* `ex2.kpoints/` --  convergence tests for k-points (`K_POINTS`)

* `ex3.alat/` -- search of lattice parameter of Si bulk and fitting bulk modulus
                 (**alat** = *a* lattice parameter)



