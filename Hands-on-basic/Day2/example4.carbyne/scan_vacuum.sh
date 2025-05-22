#!/bin/sh

# loop over ecutwfc value
for cell_parameter in 20
#8 10 12 14 18 20 
do
    echo "Running for vacuum level = $cell_parameter ..."

    # self-consistent calculation
    cat > pw.carbyne.scf_vacuum$cell_parameter.in << EOF
   &CONTROL
    calculation='',  ! Specify the type of calculation
    prefix='carbyne',
    pseudo_dir='../pseudo/',
    outdir='./tmp'
    tprnfor = .true.
    tstress=.true.
   /
   &SYSTEM    
      ibrav =  0, 
      nat =  ,  !Specify the number of atom in the unit cell
      ntyp = ,  ! Specify the number of atomic type in the unit cell
      ecutwfc = 40, 
   /
   &ELECTRONS
   /
   ATOMIC_SPECIES
   C  12.011  C.pbe-n-kjpaw_psl.1.0.0.UPF
   ATOMIC_POSITIONS crystal
   C 0.00 0.00 0.00 
   K_POINTS automatic
   X X 30 0 0 0   ! Specify the number of k-points in the x nad y direction of the BZ (Hint: look at example2.graphene)
   CELL_PARAMETERS bohr
   $cell_parameter         0.00000       0.0000
   0.00000         $cell_parameter       0.0000
   0.00000         0.00000       3.36
EOF

   # run the pw.x calculation
   pw.x -in pw.carbyne.scf_vacuum$cell_parameter.in > pw.carbyne.scf_vacuum$cell_parameter.out
done
