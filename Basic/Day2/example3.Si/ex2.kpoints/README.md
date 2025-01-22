# PURPOSE OF THE EXERCISE:
## convergence test for k-points (K_POINTS)
---------------------------------------------------------

**Steps to perform:**

1. Inspect `scan_kgrid.sh` 

2. Run `scan_kgrid.sh` for the first time

3. Comment out the even spacing of the kgrid in `scan_kgrid.sh` and remove the comment from the odd spacing 

4. Rerun `scan_kgrid.sh` for the second time

5. Run `gather_data_even.sh` and `gather_data_odd.sh`

6. Plot the data with python:
    
    `python3 plot_etot_kgrid.py`
     



