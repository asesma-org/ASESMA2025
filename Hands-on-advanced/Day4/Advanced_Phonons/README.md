# ASESMA2025

This repository contains materials for the advanced phonon tutorial at the ASESMA2025 workshop.
It is based on the electronic structure theory code [FHI-aims](https://fhi-aims.org/) and the 
lattice dynamics Python package [FHI-vibes](https://vibes-developers.gitlab.io/vibes/).

It was kindly prepared by Matteo Rinaldi, Elena Gelžinytė, Christoph Dähn, and Christian Carbogno 
on the basis of existing tutorials available at the [FHI-aims](https://fhi-aims.org/) and the 
[FHI-vibes](https://vibes-developers.gitlab.io/vibes/) webpage. To explore the discussed topics
in more depth, please refer to these tutorials that were prepared and improved by several people
over the last decade. In particular, honorable mentions go out to Shuo Zhao, Florian Knoop, and 
Thomas A.R. Purcell as well as to Matthias Scheffler for continuous and long-standing support.


# ACTIVATION OF THE FHI-AIMS AND FHI-VIBES SOFTWARE PACKAGE
All necessary software should be preinstalled. To make sure that your docker image can find it, please edit  */home/triqs/.bashrc*
**before** starting the Docker image.
Scroll to the end of the file and uncomment the following lines:

      export PYTHONPATH=/home/triqs/FHI_local/FHI_vibes_build/:$PYTHONPATH
      export PATH=/home/triqs/FHI_local/FHI_vibes_build/bin:$PATH

Then, you can start the Docker as usual by calling *asesma_qe*. 

**Please do not forget to comment out / remove this two lines at the end of the tutorial!**

