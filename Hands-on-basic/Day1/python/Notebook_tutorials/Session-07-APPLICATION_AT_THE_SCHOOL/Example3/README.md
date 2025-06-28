Here we shall look at how to run QE simulations using python and plot the band structure.

To run the **scf** simulation,

`$ python3 run_qe.py Si.scf.in` 

Once the **scf** calculation is complete, we can run the **bands** calculation as follows,

`$ python3 run_bands.py bands.in`

To plot the **band structure**, we run,

`$ python3 plot_bs.py`

