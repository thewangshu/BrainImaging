# *Fluency task* : This folder contains the following files :

1. *_fmri.nii_* : This is the 4D file using which the First level FEAT analysis was performed using 2 input variables, namely _word_generation.txt_ and _word_shadowing.txt_.
2. *_structural.nii_* : This file contains data from the structural space.
3. *_structural_brain_1.nii_* : This file was generated using the BET Tool of FSL for the purpose of coregistration.
4. *_mean_func.mat_* : The transformation matrix generated after coregistration.
5. *_mean_func.nii_* : Generated after performing coregistration of the Time-series mean 3D NIFTI image generated from the FEAT analysis
6. *_thresh_zstat1_out.nii_* : Generated after applying the tranformation matrix obtained from coregistration and pertains to the word generation task.
7. *_thresh_zstat2_out.nii_* : Generated after applying the tranformation matrix obtained from coregistration and pertains to the word suppression task.
8. **_thresh_zstat1.png_** : Screenshot showing activation during Word generation.
9. **_thresh_zstat2.png_** : Screenshot showing activation during Word shadowing.
