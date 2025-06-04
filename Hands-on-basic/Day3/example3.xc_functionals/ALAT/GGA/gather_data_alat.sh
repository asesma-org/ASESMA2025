#!/bin/sh


# delete the si.etot_vs_kgrid if it exists
rm -f data.dat
rm -f Etot-vs-alat.dat

echo 'alat, vol, etot' > data.dat

# loop over ecutwfc value
for alat in 9.7 9.8 9.9 10.0 10.1 10.2 10.3 10.4 10.5 10.6 10.7 10.8
do
    echo "Grepping energy for alat = $alat ..."
    
    etot=$(grep ! pw.si.scf_alat$alat.out |  awk '{print $(NF-1)}')
    cell_volume=$(grep 'volume' pw.si.scf_alat$alat.out | awk '{print $4}')
    

    echo $alat, $cell_volume, $etot >> data.dat

    echo $alat, $etot >> Etot-vs-alat.dat

done
