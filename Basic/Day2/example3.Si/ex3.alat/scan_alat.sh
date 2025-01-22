#!/bin/sh
# reminder: from now on, what follows the character # is a comment


# delete the si.etot_vs_ecut if it exists
rm -f si.etot_vs_alat

# loop over ecutwfc value
for alat in 9.7 9.8 9.9 10.0 10.1 10.2 10.3 10.4 10.5 10.6 10.7 10.8 
do
    echo "Running for lattice constant = $alat Bohr"

    # self-consistent calculation
    cat > pw.si.scf_alat$alat.in << EOF
 &CONTROL
    calculation='scf',
    prefix='silicon',
    pseudo_dir='../../pseudo/',
    outdir='./tmp'
 /
 &SYSTEM    
    ibrav =  2, 
    celldm(1) = $alat, 
    nat =  2, 
    ntyp = 1,
    ecutwfc = 36, 
 /
 &ELECTRONS
 /
ATOMIC_SPECIES
   Si  28.086  Si.pz-vbc.UPF
ATOMIC_POSITIONS
   Si 0.00 0.00 0.00 
   Si 0.25 0.25 0.25 
K_POINTS automatic
   6 6 6   1 1 1
EOF

    # run the pw.x calculation
    pw.x -i pw.si.scf_alat$alat.in > pw.si.scf_alat$alat.out
done
