#!/usr/bin/env python

# calculate vowel-extrinsic or -intrinsic Coefficient of Variation
# à la Lee, Potamianos, & Narayanan (1999)
# read input .csv with columns for acoustic measurements, speaker, and phone
# file output = CoV_data.csv
# Author: Meg Cychosz 2018
# UC Berkeley

import pandas as pd
import numpy as np

# within speaker coefficient of variation: vowel extrinsic 

 data = pd.read_csv("data.csv")
 CoV=[] # create empty list to store measurements

 speakers = data['speaker'].unique() # get speaker numbers
 subsets = {s: data[data['speaker'] == s] for s in speakers} # create dictionary
 for s in subsets:
 	F1 = subsets[s].loc[: , "F1"] # index each mini dataframe by speaker #
 	F1_CoV = (np.std(F1, ddof=1))/(np.mean(F1)) # be sure to specify sample stan.dev., not pop.
 	CoV.append(F1_CoV)

 data = data.assign(coef = np.repeat(CoV,data.speaker.value_counts(sort=True))) 
 data.to_csv('CoV_data.csv', encoding='utf-8') 
	
# --------------------------------------------------

# vowel-intrinsic option

#data = pd.read_csv("data.csv")
#CoV=[] # create empty list to store CoV measurements
#
#for v in data['phone'].unique():
#	phone = data.loc[data['phone'] == v] # create dfs by phone
#	speakers = phone['speaker'].unique() # get speaker numbers
#	subsets = {s: phone[phone['speaker'] == s] for s in speakers} # create dictionary
#	for s in subsets:
#		F1 = subsets[s].loc[: , "F1"] # index each mini dataframe by speaker #
#		F1_CoV = (np.std(F1, ddof=1))/(np.mean(F1)) # be sure to specify sample stan.dev., not pop.
#		CoV.append(F1_CoV)
#
#data['speaker_phone'] = data['phone'].map(str) + data['speaker'].map(str)
#data = data.assign(coef = np.repeat(CoV,data.speaker_phone.value_counts(sort=True))) 
#data.to_csv('CoV_data.csv', encoding='utf-8') 

