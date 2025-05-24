# PURPOSE OF THE EXERCISE:
## convergence test for vacuum in the x-y plane via traditional Unix shell-script
--------------------------------------------------------------------------------

**Steps to perform:**

1. Open the structure with xcrysden to visualize it, using the script:

       xcrysden --script carbyne.xcrysden

2. Read the `scan_vacuum.sh` script and try to understand it.

3. Fill the part that are left empty

4. To run the example, execute:

       bash ./scan_vacuum.sh
       
5. To gather the data, open the script and fill the missing part. Then, execute:

       bash ./gather_data.sh
       
6. To plot the data, run:
	
       python ./plot_etot_vacuum.py 

       or

       gnuplot ./plot.gp

7. Plot the difference in energy and pressure, filling the missing part of 'plot_etot_diff_vacuum.py'.
   (Hint: look at example3.Si/ex1 and example3.Si/ex2). Then, plot:

       python ./plot_etot_diff_vacuum.py