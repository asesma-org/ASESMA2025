Perform a variable-cell optimization: 

mpirun -np 2 pw.x < graphite.vc-relax.in |tee graphite.vc-relax.out

Study different cases:
 1. input_dft = 'vdw-DF'     @PBE pseudo (non-local)       C.pbe-rrkjus.UPF
 2. input_dft = 'vdw-DF2'    @PBE pseudo (non-local)       C.pbe-rrkjus.UPF
 3. input_dft = 'rVV10'      @PBE pseudo (non-local)       C.pbe-rrkjus.UPF
 4. vdw_corr  = 'DFT-D'      @PBE pseudo (semi-empirical)  C.pbe-rrkjus.UPF
 5. vdw_corr  = 'DFT-D3'     @PBE pseudo (semi-empirical)  C.pbe-rrkjus.UPF
 6. Normal PBE calculation   @PBE pseudo                   C.pbe-rrkjus.UPF
 7. Normal LDA calculation   @LDA pseudo                   C.pz-rrkjus.UPF

Use XCrySDen to determine the optimized inter-layer distance.  
Compare the optimized inter-layer distances with the experimental value of 3.336 A. 
Which VdW functional gives the most accurate inter-layer distance in graphite?

