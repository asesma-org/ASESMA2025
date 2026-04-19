set style data dots
set nokey
set xrange [0: 4.21578]
set yrange [ 13.31852 : 17.57115]
set arrow from  0.55544,  13.31852 to  0.55544,  17.57115 nohead
set arrow from  1.11882,  13.31852 to  1.11882,  17.57115 nohead
set arrow from  1.90996,  13.31852 to  1.90996,  17.57115 nohead
set arrow from  2.30582,  13.31852 to  2.30582,  17.57115 nohead
set arrow from  2.86125,  13.31852 to  2.86125,  17.57115 nohead
set arrow from  3.42464,  13.31852 to  3.42464,  17.57115 nohead
set xtics ("G"  0.00000,"X"  0.55544,"M"  1.11882,"G"  1.90996,"Z"  2.30582,"R"  2.86125,"A"  3.42464,"Z"  4.21578)
plot "lto_bands_dft.dat.gnu" u ($1/3.7415*4.21578):2 w l
replot "lto_band.dat" w l



