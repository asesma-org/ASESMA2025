# LATTICE EXPANSION

*Estimated total CPU time: 35 min*

> In the following exercises, computational settings including the reciprocal space grid (tag `k_grid`), the basis set, and supercell's size, have been chosen to allow for a rapid computation of the exercises in the limited time and within the CPU resources available during the tutorial session. Without loss of generality, these settings allow to demonstrate trends of the lattice dynamics of materials.

> :warning: **In the production calculation, all computational parameters should be converged.**


In this exercise, you will:

* Perform phonon calculations in supercells with different volumes.
* Learn how to use the harmonic vibrational free energy to 
determine the lattice expansion.

We are going to inspect how the thermal motion of the atoms at
finite temperatures can lead to an expansion (or even a contraction) of
the lattice. For an ideal harmonic system, which is fully determined by
the dynamical matrix $D_{IJ(\mathbf{q})}$ defined in
Tutorial III,
the Hamiltonian does not depend on the volume. This also implies
that the harmonic Hamiltonian is independent of the lattice parameters,
and as a consequence of this, the lattice expansion coefficient:

$$
\alpha(T) =  \frac{1}{a}\left(\frac{\partial a}{\partial T}\right)_{p}
$$ 

vanishes[^AshcroftMermin]. To assess the lattice
expansion, it is thus essential to account for **anharmonic** effects.
In this exercise, we will use the **quasi-harmonic** approximation for
this purpose [^Biernacki], [^Togo]: In the quasi-harmonic approximation,
the free energy of solid is given by the total DFT energy of the
electronic system and the vibrational free energy of the nuclei:

$$
F(T, V) = E_\text{DFT} (V) + F^\text{ha}(T, V)~.
$$

This means that our task it not to minimize the total energy with
respect to the volume by using the
Murnaghan equation of state. Instead, we minimize the free energy
$F(T,V)$ with respect to volume. This needs to be done for each
temperature of interest because of the temperature dependence of the
vibrational free energy term $F^\text{ha}(T, V)$. So what we need to do
is:

-   Compute the phononic properties for slightly expanded and reduced
    system sizes.

-   find the lattice constant minimizing the free energy $F(T, V)$ at a
    given temperature $T$ using the Murnaghan equation of state.

Our procedure will be as follows: First, we generate input files for
*Phonopy* calculations at different volume. We will use a Python script for this called `preprocess.py`. Once the script is executed:

```
python3 preprocess.py
```

it should create 5 working directories:

```
    qha_35.335
    qha_37.590
    qha_39.939
    qha_42.383
    qha_44.926
```

In each of those you will find three input files: `geometry.in` ,
`phonopy.in`, and `aims.in`. We now need to perform a
*Phonopy* calculation, the *Phonopy* postprocess, and the reference
*FHI-aims* calculation in each of the folders. To do that, get into
the respective directory and run

```
cd qha_35.335
vibes run    phonopy                               >> logfile
vibes output phonopy phonopy/trajectory.son --full >> logfile
vibes run    singlepoint                           >> logfile
cd ..
```

Once you have computed all the thermal property files in the respective
folders, we have a good dataset for vibrational free energy term $F^\text{ha}(T, V)$.

We start to perform the post-processing by extracting the total energies
from the aims calculations that are stored in the trajectory files
`qha*/aims/trajectory.son`. The script `postprocess.py`
will read the trajectories in, extract the `ase.Atoms` object
from there, read total energy and volume from it, and save them to a
file `energy-volume.dat`.

```
python3 postprocess.py
```

We can now use this information to plot a $E$ vs $V$ curve and fit it to
a Murnaghan equation of state. *Phonopy*  is shipped with a set of
scripts to facilitate certain tasks. We will use the script
`phonopy-qha` to perform the fitting[^1].

To fit the data, type:

```
phonopy-qha -b energy-volume.dat --eos murnaghan
```

This tells `phonopy-qha` to perform a Murnaghan fit on the data
contained in `energy-volume.dat`. The script will return the minimal
volume, energy, and bulk modulus:

```
phonopy-qha -b energy-volume.dat --eos murnaghan
# Murnaghan EOS
Volume: 39.6914408
Energy: -15748.2247602
Bulk modulus: 94.2257743
Parameters: -15748.2247602 0.5881108 4.6267231 39.6914408
```
If you run the script with the argument `-p` and `-s` and include the paths to the `thermal_properties.yaml`-files, it will also display and save several plots like of the energy vs. volume data points and the line obtained from fitting the equation of state. This allows us to perform the final step of the quasi-harmonic analysis!

Please create the directory `QHA` (`mkdir QHA`) and change to it (`cd QHA`). From within this directory, call:

```
phonopy-qha ../energy-volume.dat ../qha_*/phonopy/output/thermal_properties.yaml -p -s
```

This will create a bunch of files

```text
Cp-temperature.dat
Cp-temperature_polyfit.dat
Cv-volume.dat
bulk_modulus-temperature.dat
dsdv-temperature.dat
entropy-volume.dat
gibbs-temperature.dat
gruneisen-temperature.dat
helmholtz-volume.dat
thermal_expansion.dat
volume-temperature.dat
```

and a plot displaying several free energy vs. volume curves at different temperatures, as well as the
volume and lattice expansion coefficients vs. temperature.
Zoom into the plot displaying the $F$ vs. $V$ curves (`helmholtz-volume.dat`)
and take a look at the minimum of the uppermost curve marked in red. The
uppermost curve corresponds to 0 K temperature. What do you observe?
Can you explain why the 0 K volume changes slightly when you include the
vibrational free energy?

Another interesting feature is the negative lattice expansion of Silicon
below room temperature. Do you have an explanation for this? [^Kim]

[^1]: See <https://atztogo.github.io/phonopy/qha.html#phonopy-qha> for reference.
[^Biernacki]: [S. Biernacki and M. Scheffler, Phys. Rev. Lett. 63, 290 (1989).](https://doi.org/10.1103/PhysRevLett.63.290)
[^AshcroftMermin]: N. W. Ashcroft, N. D. Mermin, Solid State Physics, Saunders College Publishing, New York, (1976).
[^Kim]: [D. S. Kim, et al., Proc. Natl. Acad. Sci. U.S.A. 115, 1992 (2018).](https://doi.org/10.1073/pnas.1707745115)
[^Togo]: [A. Togo, L. Chaput, I. Tanaka, G. Hug, Phys. Rev. B, 81, 174301-1-6 (2010).](https://journals.aps.org/prb/abstract/10.1103/PhysRevB.81.174301)

