# DFT+DMFT project

Description of the content:

- `/Literature` folder containing literature 
- `SrVO3_example_setup` Strontium vanadate setup, a classical system to study with many body methods
- `SrRuO3_fake_cubic` simplified cubic structure of SrRuO3, a ferromagnetic metal, which is the n=infty limit of the ruddlesden popper series
- `example_single_band_notebook.ipynb` notebook containing tutorial from: `https://triqs.github.io/triqs/latest/userguide/python/tutorials/ModelDMFT/solutions/01s-IPT_and_DMFT.html` explaining one of the simplest impurity solvers

# Loading the docker container

To install the `solid_dmft` docker image on your pc run
```
docker pull cartaalberto/solid_dmft:3.3.x
```

Add this to the bashrc
```
alias triqs_qe="docker run -p 8888:8888 --rm -it --shm-size=4g -e USER_ID=`id -u` -e GROUP_ID=`id -g` -v /home:/home cartaalberto/solid_dmft:3.3.x bash"
```

To run a jupyter notebook inside your container
```
jupyter notebook --ip=0.0.0.0 --port=8888 --allow-root --no-browser
```


