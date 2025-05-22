#!/bin/sh


# delete the si.etot_vs_kgrid if it exists
rm -f si.etot_vs_kgrid

# loop over ecutwfc value
for kres in 2 4 6 8   # even values
#for kres in 3 5 7 9  # odd values
do
    echo "Grepping energy for kgrid = $kres $kres $kres ..."
    
    grep -e 'kinetic-energy cutoff' -e ! pw.si.scf_k$kres.out | \
        #awk -v kres=$kres '/ / {kgrid=$kres}
       
	# here we save the Etot for each k-points grid and save to file: si.etot_vs_kgrid_*
        # comment and uncomment the correct line accordingly
       
       	awk -v kres=$kres ' /!/ {print kres, $(NF-1)}' >> si.etot_vs_kgrid_even
        #awk -v kres=$kres ' /!/ {print kres, $(NF-1)}' >> si.etot_vs_kgrid_odd

done
