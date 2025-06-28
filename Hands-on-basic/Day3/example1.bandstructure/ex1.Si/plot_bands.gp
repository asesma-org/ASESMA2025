set terminal post eps enhanced solid color  "Helvetica" 20  
set output "Si_bands.eps" 
set arrow from 0, graph 0 to 0, graph 1 nohead

# set the highest occupied state energy to correct value
EFermi=6.06
# ... and uncomment the following line
set xzeroaxis lt -1


set grid xtics lt -1 lw 1
set format y "%5.1f"
set format x ""
set ylabel "Energy (Ry)"
set xlabel "Wavevector"
set label "Efermi" at 2.8,0.50
!set key center
set xtics ("W" 0.0000, "{/Symbol G}" 1.1180, "X" 2.1180, "W" 2.6180, "L" 3.3251,"{/Symbol G}" 4.1912)

plot [0:4.1912][-12:10] 'bands.dat.gnu' u 1:($2-EFermi) notitle  w lines lw 3 lc "black"
