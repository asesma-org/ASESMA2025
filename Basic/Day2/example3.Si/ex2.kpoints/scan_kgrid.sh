#!/bin/sh
# reminder: from now on, what follows the character # is a comment


# delete the si.etot_vs_ecut if it exists
rm -f si.etot_vs_ecut

# loop over ecutwfc value
for kres in 2 4 6 8    # even values
#for kres in 3 5 7 9   # odd values
do
    echo "Running for kgrid = $kres $kres $kres  ..."

    # self-consistent calculation
    cat > pw.si.scf_k$kres.in << EOF
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
   $kres $kres $kres   1 1 1
EOF

    # run the pw.x calculation
    pw.x -i pw.si.scf_k$kres.in > pw.si.scf_k$kres.out
done
