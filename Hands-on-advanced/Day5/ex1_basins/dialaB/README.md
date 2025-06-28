################## EX 1.######################
dialaB
compile input
gmx grompp -f vacuum.mdp -p topol.top -o dialaB.tpr -c confB.gro -maxwarn 1

run md 
gmx mdrun -s dialaB.tpr -x dialaB.xtc

look at the plumed input and say what you see
compute cv into COLVAR using plumed driver

plumed driver --ixtc dialaB.xtc --plumed plumed.calccvs.dat
