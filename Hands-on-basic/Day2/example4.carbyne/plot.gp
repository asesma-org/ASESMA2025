set grid

set multiplot
set origin 0,0.5
set size 1,0.5
set lmargin 13
set ylabel "Total energy (Ry)"
unset xlabel

plot 'c.etot_vs_vacuum' w linespoints lw 2 pt 4 ps 1.2

set origin 0,0
set size 1,0.5
set lmargin 13
set ylabel "Total stress (kbar)"
set xlabel "vacuum along the lateral directions (Bohr)"

plot 'c.etot_vs_vacuum' u 1:3 w linespoints lw 2 pt 4 ps 1.2
pause -1

