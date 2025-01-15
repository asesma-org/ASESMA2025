#!/bin/sh

# remove old outputs and create new files
rm -f data-mv k_file out.al.* etot.*
touch data-mv k_file


FIL=""
dg_list="0.01 0.03 0.05 0.07 0.09 0.11" 
k_list="6 8 10 12 14 16"


for degauss in $dg_list; do
    touch etot.${degauss}

    for nk in $k_list; do 
        cat > input.pw <<EOF
&control
    calculation = 'scf',
    prefix = 'al',
    pseudo_dir = '../../../../pseudo',
    outdir = './tmp'
/
&system
    ibrav = 2, 
    celldm(1) = 7.461, 
    nat = 1, 
    ntyp = 1,
    nbnd = 10
    ecutwfc = 16,
    occupations='smearing'
    smearing='marzari-vanderbilt'
    degauss=$degauss
/
&electrons
    mixing_beta = 0.7
/
ATOMIC_SPECIES
Al 26.98 Al.pz-vbc.UPF
ATOMIC_POSITIONS (alat)
Al 0.0 0.0 0.0
K_POINTS (automatic)
$nk $nk $nk 1 1 1

EOF

        pw.x -inp input.pw | tee out.al.${degauss}.${nk}.gauss

        etot=$(grep -e ! out.al.${degauss}.${nk}.gauss | awk '{print $5}')
        echo $etot >> etot.${degauss}
    done

    FIL=$FIL"etot."${degauss}" "
done

echo "#nk" "degauss" $dg_list >> data-mv
echo "$k_list" | tr ' ' '\n' >> k_file
paste -d" " k_file $FIL >> data-mv
rm etot.*
