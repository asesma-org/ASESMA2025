################## EX 2.######################
metad from configuration A
compile input
gmx grompp -f vacuum.mdp -c confA.gro -p topol.top -o dialaA.metad.tpr -maxwarn 1


inspect the plumed input and let's discuss what we see

run metadynamics
gmx mdrun -s dialaA.metad.tpr -x dialaA.metad.xtc -plumed plumedmetad.dat


we now have a COLVAR file which contains the values of phi and psi as a function of time. as well as a HILLS file which contains the details of the deposited gaussians. We will use this file to obtain the free energies.


plumed sum_hills --hills HILLS #this command tells plumed to sum the gaussians in the HILLS file and provide the free energies. after this runs, there will be a file called fes.dat. Let us inspect it.
