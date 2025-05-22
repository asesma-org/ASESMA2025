# PURPOSE OF THE EXERCISE:
## How to calculate and plot density-of-states (DOS) and band structure (spaghetti) of a graphene sheet.
--------------------------------------------------------------------

**Steps to perform:**

1. `pw.x` SCF calculation as to calculate Kohn-Sham states

       pw.x < pw.graphene.scf.in > pw.graphene.scf.out


### How to make a DOS plot

2. `pw.x` non-SCF calculation with a denser k-mesh (for a better DOS plot):

       pw.x < pw.graphene.nscf.in > pw.graphene.nscf.out


3. `dos.x` calculation to make a DOS datafile:

       dos.x < dos.graphene.in > dos.graphene.out

    (the resulting DOS datafile is written to a `graphene.dos` file)


4. plot the DOS with gnuplot:

       gnuplot dos.gp


### Setting the correct Fermi energy in gnuplot files

To indicate the Fermi energy in DOS and spaghetti plots, let's enter the
correct value of Fermi energy in the two gnuplot files. 

8. First find the fermi enery in `pw.graphene.nscf.out` file, e.g.,

       grep Fermi pw.graphene.nscf.out
       
   this command prints the following line:
   
       the Fermi energy is     0.8967 ev

9. Edit the `dos.gp` file and insert the above
   value of Fermi energy and uncomment the `set yzeroaxis lt -1` line,
   i.e., the top part of this files look like:
   
       # set Fermi energy to correct value
       Efermi=0.9204
       # ... and uncomment the following line
       set yzeroaxis lt -1
       
10. Replot the DOS:

        gnuplot dos.gp
