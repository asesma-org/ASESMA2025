#!/bin/sh
# reminder: from now on, what follows the character # is a comment


# delete the si.etot_vs_ecut if it exists
rm -f si.etot_vs_ecut

# loop over ecutwfc value
for ecut in 12 16 20 24 28 32 36
do
    echo "Running for ecutwfc = $ecut ..."

    # self-consistent calculation
    cat > pw.si.scf_ecut$ecut.in << EOF
 &CONTROL
    calculation='scf',
    prefix='silicon',
    pseudo_dir='../../pseudo/',
    outdir='./tmp'
 /
 &SYSTEM    
    ibrav =  2, 
    celldm(1) = 10.2, 
    nat =  2, 
    ntyp = 1,
    ecutwfc = $ecut, 
 /
 &ELECTRONS
 /
ATOMIC_SPECIES
   Si  28.086  Si.pz-vbc.UPF
ATOMIC_POSITIONS
   Si 0.00 0.00 0.00 
   Si 0.25 0.25 0.25 
K_POINTS automatic
   4 4 4   1 1 1
EOF

    # run the pw.x calculation
    pw.x -i pw.si.scf_ecut$ecut.in > pw.si.scf_ecut$ecut.out
done
