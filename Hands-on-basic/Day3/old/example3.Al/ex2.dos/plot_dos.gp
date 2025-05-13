set terminal post eps enhanced solid color "Helvetica" 20 
set arrow from 0, graph 0 to 0, graph 1 nohead
set output "Al_DOS.eps" 
set xlabel "E - E_F (eV)" 
set ylabel "DOS (states/eV)"
Efermi = 8.4533 
plot "dos.dat" u ($1-Efermi):($2) w l lw 3 lt rgb "red"   title 'total DOS' 
