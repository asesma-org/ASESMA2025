set terminal post eps enhanced solid color "Helvetica" 20 
set arrow from 0, graph 0 to 0, graph 1 nohead
set output "Al_pdos.eps" 
set xlabel "E - E_F (eV)" 
set ylabel "pdos (states/eV)"
Efermi = 8.4533 
plot "pdos.dat.pdos_atm#1(Al)_wfc#1(s)" u ($1-Efermi):($2) w l lw 3 lt rgb "orange"    title '1s',\
     "pdos.dat.pdos_atm#1(Al)_wfc#2(p)" u ($1-Efermi):($2) w l lw 3 lt rgb "blue"  title '2p',\
     "pdos.dat.pdos_tot"                u ($1-Efermi):($2) w l lw 3 lt rgb "gray"   title 'total Pdos'  
