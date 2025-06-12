set terminal post eps enhanced solid color "Helvetica" 20
set output "phonon_dispersion.eps"
set xrange [0:4.280239]
set yrange [-200:650]
set arrow from 1,-200 to 1,650 nohead  lw 3
set arrow from 2,-200 to 2,650 nohead  lw 3
set arrow from 1.5,-200 to 1.5,650 nohead  lw 3
set arrow from 3.4142,-200 to 3.4142,600 nohead  lw 3
set ylabel "{/Symbol w} (cm^{-1})"
unset xtics
set label "{/Symbol G}" at -0.05,-240
set label "X" at 0.95,-240
set label "W" at 1.45,-240
set label "X" at 1.95,-240
set label "{/Symbol G}" at 3.37,-240
set label "L" at 4.1897,-240

plot "./freq.plot" u 1:2 w l lw 2 title 'q-grid: 2x2x2'

