## exercise-4.a

Perform convergence tests of the band gap of Si using the SCAN functional 
with the SCAN-generated pseudopotential (Si.SCAN.UPF).
Consider the kinetic-energy curoff ecutwfc from 20 to 200 Ry (with a 10 Ry step).
What is the converged band gap value? 
What is the optimal cutoff (with the accuracy of the band gap of ~0.001 eV)?
 
   mpirun -n 2 pw.x < Si.scf.in |tee Si.scf.out

## exercise-4.b 

Calculate the band gap of Si using the SCAN functional with the PBE-generated
pseudopotentials (Si.pbe_PseudoDojo.UPF and Si_ONCV_PBE-1.2.upf) and using the 
optimized cutoff from the previous exercise. Compare these band gap values
with the one obtained in the previous exercise.

## exercise-4.c 

Calculate the band gap of Si using the rSCAN and r2SCAN functionals with the
PBE-generated pseudopotential Si_ONCV_PBE-1.2.upf. Compare the computed band
gap value with the one obtaned from SCAN and experiments. Which meta-GGA
functional gives the closest agreement with experiments for the band gap of Si?


=============================================================================================

BONUS exercises:

- Perform convergence tests of the magnetic moment of Fe using the SCAN functional
  with the PBE-generated pseudopotential (Fe_ONCV_PBE-1.2.upf). What is the converged
  value of the magnetic moment and what is the optimal cutoff?

- Compute the magnetic moment of Fe using the rSCAN and r2SCAN functionals with the
  PBE-generated pseudopotential (Fe_ONCV_PBE-1.2.upf). Which meta-GGA functional
  gives the the closest agreement with experiments for the magnetic moment of Fe?

  mpirun -n 2 pw.x < Fe.scf.in |tee Fe.scf.out
