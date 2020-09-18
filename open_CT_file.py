# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:21:26 2020

@author: SantiagoCaroZ
"""

import pydicom
import matplotlib.pyplot as plt
import numpy as np

filename="slices/series 002[CT-Crane SPC]/1.3.6.1.4.1.5962.99.1.2786334768.1849416866.1385765836848.6.0.dcm"

dataset=pydicom.dcmread(filename)
data=dataset.pixel_array
# Leer Datos
print("La imagen tiene {} x {} pixels".format(data.shape[0],data.shape[1]))
    
print("Nombre del paciente: ", dataset.PatientName)
print("Número de identificación: ", dataset.PatientID)

#Modificar datos
name=dataset[0x0010,0x0010]
name.value="Jhon Fredy"

dataset.PatientID="125487"


#Guarda nuevos datos
newfile="EJEMPLO1.dcm"
dataset.save_as(newfile)

dataset1=pydicom.dcmread(newfile)

   


