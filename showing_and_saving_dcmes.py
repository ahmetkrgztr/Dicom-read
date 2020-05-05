# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 23:23:29 2019

@author: ahmet
"""


import os, glob
import numpy as np
import matplotlib.pyplot as plt
import pydicom
from rvseg import patient
import time

#patient number
patient_number = int(15)

#creating path
if patient_number < 10:
    folder_direc = 'C:\\Users\\ahmet\\Desktop\\cardiacmr\\Datasets\\TrainingSet\\patient0' + str(patient_number) + '\\P0' + str(patient_number) + 'dicom'
else:
    folder_direc = 'C:\\Users\\ahmet\\Desktop\\cardiacmr\\Datasets\\TrainingSet\\patient' + str(patient_number) + '\\P' + str(patient_number) + 'dicom'

#counting element number of folder for iteration number
list_of_folder = os.listdir(folder_direc) 
file_number = len(list_of_folder)

element_arrs = np.zeros((256,216,file_number,50))

for i in range(file_number-50):
    
    #creating path
    if patient_number < 10:
        if i < 10:
            file_direc = folder_direc + '\\P0' + str(patient_number) + '-000' + str(i) + '.dcm'
        elif i >= 10 and i < 100:
            file_direc = folder_direc + '\\P0' + str(patient_number) + '-00' + str(i) + '.dcm'
        else:
            file_direc = folder_direc + '\\P0' + str(patient_number) + '-0' + str(i) + '.dcm'
            
    elif patient_number >= 10:
        if i < 10:
            file_direc = folder_direc + '\\P' + str(patient_number) + '-000' + str(i) + '.dcm'
        elif i >= 10 and i < 100:
            file_direc = folder_direc + '\\P' + str(patient_number) + '-00' + str(i) + '.dcm'
        else:
            file_direc = folder_direc + '\\P' + str(patient_number) + '-0' + str(i) + '.dcm'
       
    #showing pictures and save them as array  
        
    ds = pydicom.dcmread(file_direc)
    plt.imshow(ds.pixel_array, cmap=plt.cm.bone)
    plt.show()
    
    arr=ds.pixel_array
    element_arrs[:,:,i,patient_number]=arr
    
    time.sleep(0)
    
    
    
    
    


        