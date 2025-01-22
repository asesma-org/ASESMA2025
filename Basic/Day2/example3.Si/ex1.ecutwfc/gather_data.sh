
#!/bin/sh
# reminder: from now on, what follows the character # is a comment


# delete the si.etot_vs_ecut if it exists
rm -f si.etot_vs_ecut

# loop over ecutwfc value
for ecut in 12 16 20 24 28 32 36
do
    echo "Grepping energy for ecutwfc = $ecut ..."
    
    grep -e 'kinetic-energy cutoff' -e ! pw.si.scf_ecut$ecut.out | \
        awk '/kinetic-energy/ {ecut=$(NF-1)}
             /!/              {print ecut, $(NF-1)}' >> si.etot_vs_ecut

done
