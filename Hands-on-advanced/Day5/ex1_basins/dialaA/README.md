################## EX 1.######################
dialaA
compile input
gmx grompp -f vacuum.mdp -p topol.top -o dialaA.tpr -c confA.gro -maxwarn 1

run md 
gmx mdrun -s dialaA.tpr -x dialaA.xtc

look at the plumed input and say what you see
compute cv into COLVAR using plumed driver

plumed driver --ixtc dialaA.xtc --plumed plumed.calccvs.dat
