# vocal_tract_vowel

Triple vowel formant tracker that measures formants using three different systems and computes the median of them. Additional scripts to visualize and identify outliers and mis-tracked formants. Also contains all scripts and notebooks to replicate results from Chapter 2 of dissertation.  


## What's what in this repo

* [Notebooks to track formants and compute vocal tract length](#acoustic-measurements)
* [Scripts used to analyze vowel variability and generate results](#data-analysis)


## Dependencies

The following Python dependencies are required to run the scripts in this repo: `pandas`, `fnmatch`, `phonlab`, `audiolabel`, (both available [here](https://github.com/rsprouse)), `numpy`, `seaborn`, `matplotlib`, and `numpy`, in addition to other generic libraries that are pretty standard with any Python installation. Additional R libraries are needed and are listed in the R scripts/notebooks. 


## Acoustic measurements
Throughout these notebooks, the output from the cells has been cleared as it contains deanonymized participant information

`1_triple_formant_tracker.ipynb` - track formants in three ways: 1) Inverse Filter Control Formant (Watanabe, 2001), 2) ESPS covariance, and 3) ESPS autocorrelation. Requires a .wav file for each speaker. Then, each tracker generates a directory containing the files with various acoustic measurements for each speaker (f0, formants, etc.). LPC order of 10 specificed for the children and 12 for the adults.

`2_get_median_formant.ipynb` - compute the median measurement of each formant from the three trackers at 25%, 50%, and 75% of the vowel. Generates the file `med_formants.csv` which can be used in `3_check_for_outliers.ipnyb`, `get_vt_length.ipnyb`, and to generate the manuscript results

`2_get_median_formant_lpc8.ipynb` - same as above, but attempting to track formants using an LPC filter order of 8 for children aged 4-6 years; this performed markedly worse than an LPC order of 10 (lots of mistracked F2) so LPC order of 10 was used for all children

`3_check_for_outliers.ipynb` - histograms that visualize overlap in formant distribution by age group and individual speaker to identify mis-tracked formants 

`get_vt_length.ipynb` - compute child and adult vocal track length and DeltaF ratio using F1-F3 (for children) and F1-F4 (for adults); this script is sewn into the R script `3_vtl_results.Rmd` that generates the results section


## Data analysis

`1_cleanvowels_eo.Rmd` - select relevant lexical items and removes all formant measurements outside of 3 MADs from the median; not included in the public repo as it contains personal identifying information; generates the file `cleaned_vowels_eo.csv` which is used to run `2_rename_participants.R`

`2_rename_participants.R` - map participant names to anonymied IDs; not included in the public repo as it contains personal identifying information; generates the file `cleaned_vowels_eo.anonymized.csv` which is used to run `3_vtl_results.Rmd`

`3_vtl_results.Rmd` - generates results section of manuscript, including 1) calculation of vocal tract length/deltaF, 2) calculating vowel dispersion via coefficient of variation, 3) vowel normalization via Lobanov and DeltaF techniques, 4) modeling differences by normalization technique, 5) calculating formant ratios between supraglottal cavities, 6) modeling differences by supraglottal cavity formant ratios

`validate_ratio.Rmd` - script to validate the method for computing supraglottal cavity sizes using formant measurements (F1:F2 and F2:F3 ratios) 

`speaker_metadata_anonymized.csv` - dataframe containing speaker metadata


## Other scripts in this repo

`calculate_CoV.py` - short script to compute the coefficient of variation of formant measurements; vowel-extrinsic and intrinsic options

## Citations

Watanabe, A. (2001). Formant estimation method using inverse-filter control. _IEEE Transactions on Speech and Audio Processing_, 9(_4_), 317-326.



