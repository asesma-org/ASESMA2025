#%%
from triqs_dft_tools.converters import Wannier90Converter
Converter = Wannier90Converter(seedname='sro')
Converter.convert_dft_input()
# %%
