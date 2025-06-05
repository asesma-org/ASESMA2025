#!/bin/csh  
# The previous line indicates that this is a C-shell file
# -------------------------------------------------------
# Program to run deMon in the present working directory.
# To use: Create an input file with the name xxx.inp where
# xxx can be anything.  Execute with 
# /home/mcasida/ENGINEERING/workbook/examples/run.csh xxx 
# The job runs interactively in foreground.
# -------------------------------------------------------
set xxx = $1
echo "Input file "$xxx.inp
set PWD = `pwd`
echo "The present working directory is "$PWD
set deMon_root = /home/mcasida/ENGINEERING/workbook/deMon2kv6p3 # location of deMon files
echo "Using directories and excecutables from "$deMon_root
#
# copy essential files to the present working directory
#
cp $deMon_root/BASIS $PWD # copy the BASIS file to the run directory
cp $deMon_root/AUXIS $PWD # copy the AUXIS file to the run directory
cp $deMon_root/binary $PWD/deMon.x # copy the executable to the run directory
cp $xxx.inp deMon.inp
echo $xxx.rst
if ( -f $xxx.rst ) then
  cp $xxx.rst deMon.rst
else
  echo No restart file
endif
#
# run deMon
#
./deMon.x 
#
# clean up
\rm BASIS
\rm AUXIS
mv deMon.out $xxx.out
mv deMon.rst $xxx.rst
\rm deMon.*
# -------------
# End of file
# -------------
