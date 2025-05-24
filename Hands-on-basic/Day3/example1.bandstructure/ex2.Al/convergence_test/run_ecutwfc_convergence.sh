#!/bin/sh

rm -f Al.scf.out Etot_vs_ecut.dat
touch Etot_vs_ecut.dat

for Ecut in 10 12 14 16 18 20 22 24 26 28 30; do

echo "running $Ecut ..."

# self-consistent calculation
cat > Al.scf.in << EOF
 &control
    prefix='Al'
    outdir='./tmp'
    pseudo_dir = '../../../pseudo',
 /
 &system    
    ibrav=  2, 
    celldm(1) =7.652, 
    nat=  1, 
    ntyp= 1,
    ecutwfc = $Ecut, 
    occupations='smearing', 
    smearing='marzari-vanderbilt', 
    degauss=0.01
 /
 &electrons
 /
ATOMIC_SPECIES
 Al  26.98 Al.pz-vbc.UPF
ATOMIC_POSITIONS alat
 Al 0.00 0.00 0.00 
K_POINTS automatic
  8 8 8 1 1 1 
EOF

pw.x -in Al.scf.in > Al.scf.out

grep  -e ! Al.scf.out | \
      awk -v ecut=$Ecut '{print ecut,$5}' >> Etot_vs_ecut.dat

done
