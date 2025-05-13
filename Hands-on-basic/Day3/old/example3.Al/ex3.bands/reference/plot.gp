# set Fermi energy to correct value
Efermi=6.2390
# ... and uncomment the following line
#set xzeroaxis lt -1

set grid xtics lt -1 lw 1
set format y "%5.1f"
set format x ""
set ylabel "Energy (Ry)"
unset xlabel
set label "EFermi" at 2.8,0.50
!set key center
set xtics ("L" 0.0000, "{/Symbol G}" 0.8660, "X" 1.8660, "U" 2.2196,"{/Symbol G}" 3.2802)

plot [0:3.2802][:35] 'bands.dat.gnu' u 1:($2-Efermi) notitle  with lines lw 3 
pause -1
