# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:19:15 2020

@author: Lakshya Singhal
"""

import pandas as pd 
import numpy as np
import os

df = pd.DataFrame()

df['l1'] = 1

IMG_DIR = 'C:/Users/Lakshya Singhal/Downloads/EEG dataset-20200226T161610Z-001/EEG dataset/A'
tempDir = 'EEG dataset-20200226T161610Z-001/EEG dataset/A/'
for sig in os.listdir(IMG_DIR):
    sig1 = tempDir + str(sig)
    df = df.append({'l1':sig1},ignore_index=True)


df['label'] = 0

IMG_DIR = 'C:/Users/Lakshya Singhal/Downloads/EEG dataset-20200226T161610Z-001/EEG dataset/E'
tempDir = 'EEG dataset-20200226T161610Z-001/EEG dataset/E/'
dfb = pd.DataFrame(columns = ['l1'])

for sig in os.listdir(IMG_DIR):
    sig1 = tempDir + str(sig)
    dfb = dfb.append({'l1':sig1},ignore_index=True)

dfb['label'] = 1

df = df.append(dfb)

df.to_csv('file2.csv', header=True) 