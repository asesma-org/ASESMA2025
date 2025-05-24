# PURPOSE OF THE EXERCISE:
## search of A-lattice parameter (celldm(1)) 
----------------------------------------------------------

**Steps to perform:**

1. Run `scan_alat.sh` 

2. Run `gather_data_alat.sh`

3. python `plot_alat.py`

4. python `fit_volume.py`

5. Run `ev.x` and follow the interactive command:

        ```
        Lattice parameter or Volume are in (au, Ang) > au
        Enter type of bravais lattice (fcc, bcc, sc, noncubic) > fcc
        Enter type of equation of state :
        1=birch1, 2=birch2, 3=keane, 4=murnaghan > 4
        Input file > Etot-vs-alat.dat
        Output file > ev.murnaghan.out
        ```
