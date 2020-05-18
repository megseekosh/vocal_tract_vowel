# vocal_tract_vowel
_under development_

Triple vowel formant tracker; compute vocal tract length from acoustic data; contains scripts and notebooks to replicate second dissertation chapter

## Triple formant tracker
Throughout these notebooks, the output from the cells has been cleared as it contains deanonymized participant information

## Data analysis

`1_cleanvowels_eo.Rmd` - select relevant lexical items and remove all formant measurements outside of 3 MADs from the median; not included in the public repo as it contains personal identifying information

`2_rename_participants.R` - map participant names to anonymied IDs; not included in the public repo as it contains personal identifying information

`3_vtl_results.Rmd` - generates results section of manuscript, including 1) calculation of vocal tract length/deltaF, 2) calculating vowel dispersion via coefficient of variation, 3) vowel normalization via Lobanov and DeltaF techniques, 4) modeling differences by normalization technique, 5) calculating formant ratios between supraglottal cavities, 6) modeling differences by supraglottal cavity formant ratios

- script to validate cavity ratio



