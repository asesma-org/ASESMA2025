#!/bin/sh


# delete the si.etot_vs_kgrid if it exists
rm -f si.etot_vs_kgrid_odd

# loop over ecutwfc value
for kres in 3 5 7 9
do
    echo "Grepping energy for kgrid = $kres $kres $kres ..."
    
    grep -e 'kgrid cutoff' -e ! pw.si.scf_k$kres.out | \
        #awk -v kres=$kres '/ / {kgrid=$kres}
        awk -v kres=$kres ' /!/ {print kres, $(NF-1)}' >> si.etot_vs_kgrid_odd

done
