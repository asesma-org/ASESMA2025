GNUPLOT
Below some indications on how to build a gnuplot script

As a result of the above calcuations we got a file "dos.dat", to plot the file, excute:
gnuplot
gnuplot> p 'dos.dat' u 1:2 w l lw 3

Set the correct Fermi energy: The Fermi energy in the 1st line of 'dos.dat' file.

By subtracting the Fermi energy (Efermi = 6.724) from the x-axis value, we can get a ”plot with the Fermilevel as zero”.

Replot the DOS,i.e., excute:
gnuplot
gnuplot> p ’dos.dat’ u ($1-Efermi):2 w l lw 3
gnuplot> set arrow from 0, graph 0 to 0, graph 1 nohead
gnuplot> p ’dos.dat’ u ($1-Efermi):2

