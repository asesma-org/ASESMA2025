set style data dots
set nokey
set xrange [0: 4.18914]
set yrange [ 10.42863 : 14.84211]
set arrow from  1.40992,  10.42863 to  1.40992,  14.84211 nohead
set arrow from  2.22393,  10.42863 to  2.22393,  14.84211 nohead
set arrow from  3.03795,  10.42863 to  3.03795,  14.84211 nohead
set xtics ("R"  0.00000,"G"  1.40992,"X"  2.22393,"M"  3.03795,"G"  4.18914)
 plot "svo_band.dat"
