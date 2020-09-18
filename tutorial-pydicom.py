# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:21:26 2020

@author: SantiagoCaroZ
"""

import pydicom
import matplotlib.pyplot as plt
import numpy as np
import glob

 

    
def open_file(file=None):    
    if file==None:    
        filename=pydicom.data.get_testdata_file("CT_small.dcm")
    else:
        filename=file
      
    dataset=pydicom.dcmread(filename)
    return dataset

def save_dataset(dataset):
    doc=[]
    name=str(dataset.PatientName)
    
    for fname in glob.glob("*.txt", recursive=False):
        doc.append(fname)
    
    if (len(doc)==0):
        docfile=open("dataset.txt","x")
    else:
        name="dataset"+str(len(doc))+".txt"
        docfile=open(name,"x")
    docfile.write(str(dataset))
    
    
    

def info_img(dataset):
    pixel_array=dataset.pixel_array
    print("La imagen tiene {} x {} voxels".format(pixel_array.shape[0],pixel_array.shape[1]))
    
    print("Nombre del paciente: ", dataset.PatientName)
    print("Número de identificación: ", dataset.PatientID)
    print(dataset.StudyDate)
    

def graf_img(dataset):    
    plt.figure()
    plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
    #plt.savefig("Dicom1.png", dpi=200)
    plt.show()
    
    
dataset=open_file("slices/series 002[CT-Crane SPC]/1.3.6.1.4.1.5962.99.1.2786334768.1849416866.1385765836848.6.0.dcm")
info_img(dataset)
graf_img(dataset)
save_dataset(dataset)
   