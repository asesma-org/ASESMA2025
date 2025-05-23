#!/bin/sh

rm -f Al.scf.out Etot_vs_nk.dat
touch Etot_vs_nk.dat

#for nk in 6 8 10 12 14 16 18 20; do
for nk in 6 8 ; do

echo "running $nk ..."

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
    ecutwfc = 16, 
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
  $nk $nk $nk 1 1 1 
EOF

pw.x < Al.scf.in > Al.scf.out

grep  -e ! Al.scf.out | \
      awk -v nk=$nk '{print nk,$5}' >> Etot_vs_nk.dat

done
