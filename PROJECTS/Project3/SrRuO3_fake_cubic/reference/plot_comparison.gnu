set style data dots
set nokey
set xrange [0: 5.86222]
set yrange [  9.46665 : 15.05330]
set arrow from  0.80387,   9.46665 to  0.80387,  15.05330 nohead
set arrow from  1.94071,   9.46665 to  1.94071,  15.05330 nohead
set arrow from  3.33305,   9.46665 to  3.33305,  15.05330 nohead
set arrow from  4.72538,   9.46665 to  4.72538,  15.05330 nohead
set xtics ("G"  0.00000,"X"  0.80387,"R"  1.94071,"G"  3.33305,"R"  4.72538,"X"  5.86222)
 
 plot "sro_bands.dat.gnu" u ($1/2.9392* 5.88622232):2 w l
 replot "sro_band.dat" 
