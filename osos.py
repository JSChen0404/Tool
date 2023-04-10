# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 22:11:17 2023

@author: Ryan
"""

from os.path import join
import os 
import pandas as pd

def retrieve_filepath(folder_path, outcsv_path, datatype=None):
    fullpathlist = []
    namelist = []
    for root, dirs, files in os.walk(folder_path): 
        for f in files:
            fullpath = join(root, f)
            if datatype is not None and not(fullpath.lower().endswith(datatype.lower())):
                continue
            fullpathlist.append(fullpath)
            namelist.append(f)
            
    outdata = pd.DataFrame(list(zip(fullpathlist, namelist)), columns = ['FilePath', 'FileName'])
    outdata.to_csv(outcsv_path, index=False, encoding='utf_8_sig')  
    
retrieve_filepath(r'E:\Data\Data - Dicom\json',r'C:\Users\user\Downloads\filepath.csv','dcm')