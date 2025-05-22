# PURPOSE OF THE EXERCISE:
## convergence test for cutoff energy (ecutwfc) via traditional Unix shell-script
--------------------------------------------------------------------------------

**Steps to perform:**

1. Open the structure with xcrysden to visualize it, using the script:

       xcrysden --script carbyne.xcrysden

2. Read the `scan_vacuum.sh` script and try to understand it.

3. Fill the part that are left empty

4. To run the example, execute:

       bash ./scan_vacuum.sh
       
5. To gather the data, execute:

       bash ./gather_data.sh
       
6. To plot the data, run:
	
       python ./plot_etot_ecut.py 

       or
       gnuplot ./plot.gp
