
#!/bin/sh

rm -f c.etot_vs_vacuum
# loop over ecutwfc value
for cell_parameter in  X X X  ! Specify the range of cell_parameter

do
    echo "Grepping energy and stresses for vacuum = $cell_parameter bohr..."
    
    #save the total energy into the variable etot
    etot=$(grep "!" pw.carbyne.scf_vacuum$cell_parameter.out | tail -1 | awk '{print $5}')

    #save the pressure along the z axis into the varibale stress
    stress=$(grep "P= " pw.carbyne.scf_vacuum$cell_parameter.out | tail -1 | awk '{print $6}')

    printf "%10.10f   %10.10f     %10.10f\n"  $cell_parameter  $etot  $stress >> c.etot_vs_vacuum

done
