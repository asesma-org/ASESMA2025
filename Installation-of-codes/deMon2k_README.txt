+----------------------------------+
| File: deMon2k_README.txt         |
| Last updated: 18 May 2025 by MEC |
+----------------------------------+

deMon2k is a Gaussian-type orbitals (GTOs) based DFT code for molecules
which uses auxiliary function expansions to reduce 4-center electron 
repulsion integrals (ERIs) to 3-center electron repulsion inegrals, hence
achieving a theoretical scaling of O(N**3) rather than O(N**4) with the 
number of atoms N in the molecule.  In practice, additional techniques make 
scaling significantly better than O(N**2).

deMon2k is part of the codes of the European Theoretical Spectroscopy
Facility (ETSF)
https://www.etsf.eu/resources/software/codes

However the official web page for deMon2k is 
http://www.demon-software.com/public_html/index.html

There is a freely downloadable executable version of deMon2k which should
run on any Linux machine
http://www.demon-software.com/public_html/download.html#binary
This is there for potential users to be able to download and try deMon2k
and it is fine for pedagogical purposes as well. In particular, a 
tutorial was developed that uses this freely downloadable executable
for teaching practical aspects of density-functional theory (DFT) as
a series of mini projects designed to encourage the student to engage
in actual research with the code.  The tutorial may be found at
http://www.demon-software.com/public_html/tutorials.html
It includes an appendix describing the installation of Ubuntu
on a Mac Notebook followed by installation of deMon2k.  A description
of first experiences using the tutorial as a teaching tool have been
described in the article 

[OPEC23] Nabila B. Oozeer, Abraham Ponra, Anne Justine Etindele, and 
Mark Earl Casida, Pure Appl. Chem. 95, 213 (2023). 
https://doi.org/10.1515/pac-2022-1109, 
preprint: https://arxiv.org/abs/2211.16027
"A New Freely-Downloadable Hands-on Density-Functional Theory Workbook 
Using a Freely-Downloadable Version of deMon2k"

Should the user wish to have the FORTRAN code so that they may modify the
program, then the code is available to academic users for free provided
they sign a nonproliferation agreement
http://www.demon-software.com/public_html/download.html
The nonproliferation agreement says that you will not share the FORTRAN
code with anyone outside your research group.  It allows us to keep track
of how many copies have been distributed and to whom.

Non-academic users (i.e., companies) are asked to pay a nominal fee for 
access to the code.  In the past, this fee has been enough to pay at least
part of the salary of a postdoc or to defray some of the costs of the annual 
deMon developers meeting.

+-------------+
| End-of-File |
+-------------+

