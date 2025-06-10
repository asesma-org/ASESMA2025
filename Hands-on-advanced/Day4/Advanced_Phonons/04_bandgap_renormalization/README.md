# Zero-Point Motion and Bandgap Renormalization

As you know, the total energy of a set of
harmonically coupled quantum oscillators is given by 

$$
\begin{align}
	E = \sum_s \hbar \omega_s \left[ n(\omega_s, T) + \frac{1}{2} \right].
\end{align}
$$

in which the occupation numbers are give by the *Bose-Einstein distribution* function, since phonons are bosons. In turn, this means that the nuclei are never fully at rest, but always move, even at 0K.
 
In an experiment, which is typically performed on a time scale that is orders of magnitude larger than the period of the typical vibration in a solid, we thus also do not measure the properties of _static_ nculei, but the thermodynamic average of the _moving_ nuclei, even at 0K. 

To investigate this aspect, we can use the sampling techniques introduced in the previous exercise. Note that also the effect of *zero point motion* at vanishing temperature is accounted for: Since the
amplitude is determined by a consideration rooted in quantum mechanics, it *does not vanish* when the temperature goes to zero, whereas it would go to zero in the classical case. 

In order to investigate the influence of atomic motion on the band gap, we proceed in the following way: First we need to generate an ensemble of supercells, as in the previous exercise. Then we compute
the bandgap of each sample, collect the band gaps
and form the "thermodynamic average".


## Create Samples

Our samples are created from force constants (harmonic) computed with *Phonopy*, which were already obtained before, during phonon spectrum calculations. This is exactly what we did in the previous exercise, but we will now look at more temperatures and at the band gap

So, please enter the directory of the new exercise

```
cd 04_bandgap_renormalization/input
```

and copy the results of the seconds exercise (for the 8 atom supercell) into the current directory.

```
cp -r ../../02_phonons/input/sc_0008 .
```

Type:

```
cd sc_0008
vibes output phonopy phonopy/trajectory.son --full
```

and check that you have a reasonable band structure. As done in the previous exercise, we now need to remap the force constant file using

```
cd phonopy/output
vibes utils fc remap FORCE_CONSTANTS
```

Again, we copy the necessary files to the root `input` directory and change back into that directory with.

```
cp geometry.in.* FORCE_CONSTANTS* ../../../
cd ../../..
```

Now, it is time to generate representative samples, as done in the previous exercise:

```
vibes utils create-samples geometry.in.supercell -fc FORCE_CONSTANTS_remapped -T 000 -n 10 --quantum  
```

Note that we target a temperature of 0K, generate 10 samples (representative configurations), and use a *quantum* (Bose-Einstein) statistics (flag `--quantum`).


## Compute Band Gaps for Samples structures


We now want to compute the electronic band gap of silicon at different temperatures for the 10 samples we have created (Larger number of samples should be used to achieve convergence in production calculations).

```
mkdir samples_000K
mv geometry.in.supercell.0000K.* samples_000K
```

Once all the samples are generated for each temperature from the range of interest, we can start our calculations in an automated fashion. For this purpose, copy the `aims.in` file and the `run.py` script from the `input` root into your `samples_000K` directory:

```
 cp aims.in samples_000K/
 cp run.py  samples_000K/
```

You can now start your calculations using:
```
 cd samples_000K/
 python3 run.py
```

and will get an output like

```text
❯ python3 run.py
(base) 
[vibes.run]    run singlepoint calculations with settings from aims.in
[calculator]   Update aims k_grid with kpt density of 2 to [4, 4, 4]
[...]
[vibes]        Compute structure 1 of 1: finished.
[vibes]        Close the socket
[vibes]        done.
Average band gap value is  0.544051539  eV
```
Remember, the band gap of Si for **static** nuclei is 0.612 eV. What happened?

Try re-running the same workflow for 300K, 600K, and 900K in directories `samples_300K`, `samples_600K`, and `samples_900K`. You can also find pre-computed folders in the solution folders. You can postprocess all folders together using the script `postprocess.py` that is provided in the `input` root directory. Just run

```
python3 postprocess.py
```

The script helps you with
extracting the band gaps and plot temperature dependence of the band gap, saved as `Band_gap_vs_Temperature.png`.
Which trends do you observe? 

Note that the `solution` folder also features an additional folder called `more_samples_temperatures`. Here, more samples per temperature and more temperatures are explored. What trends do you observe?


<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    TeX: { equationNumbers: { autoNumber: "AMS" } }
  });
</script>
