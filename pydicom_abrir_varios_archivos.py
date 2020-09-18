# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:21:26 2020

@author: SantiagoCaroZ
"""

import pydicom
import matplotlib.pyplot as plt
import numpy as np
import glob

def run():
    """ Corre el programa completamente"""
    cont=0
    files=open_several_files()
   
    for i in files:
        cont+=1
        try:#se usa el try para evitar que muestre error cuando se trata de leer un archivo que no es .dcm
            dataset=open_file(i) # Lee todos los archivos .dcm
        except:
            pass
            
        if hasattr(dataset, "PixelData"): # si por alguna razón el archivo no tiene el atributo "PixelData" no lo deja graficar
            graf_img(dataset)
            print ("grafica {}".format(cont))
    return files
    
    
    
def open_several_files(carpeta=None):
    """-A esta funcion cuando no se le ingresa argumento, retorna el nombre de los archivos que se encuentren en las subcarpetas del carpeta en que se encuentre este codigo
    -Cuando se le ingresa una letra entre "A" y "H", retorna el nombre de los archivos de una de las carpetas especificas artroresonacia de Santiago Caro
    -Cuando se ingresa una direccion retorna el nombre de los archivos los archivos de las subcarpetas de esa direccion 
    """
    
    files = []
    if (carpeta==None): #Determina cual de las opciones va abrir
        direct="slices/**/*"
    else:
        direct=carpeta
    
    # Toma todos los archivos .dcm o con la misma extension y los agrega a la lista File
    for fname in glob.glob(direct, recursive=False): 
        #print("loading: {}".format(fname))
        files.append(fname)
    return files
    
def open_file(file=None):
    """
    Lee el archivo .dcm y retorna toda la informacion que contiene como un dataset
    """    
    if file==None:    
        filename=pydicom.data.get_testdata_file("CT_small.dcm")
    else:
        filename=file
      
    dataset=pydicom.dcmread(filename)
    return dataset
    

    
def info_img(dataset):
    
    pixel_array=dataset.pixel_array
    print("La imagen tiene {} x {} voxels".format(pixel_array.shape[0],pixel_array.shape[1]))
    
    print("Nombre del paciente: ", dataset.PatientName)
    print("Número de identificación: ", dataset.PatientID)
    

def graf_img(dataset):    
    
    """ Grafica la imagen que forma el array de pixeles dentro del archivo .dcm"""
    plt.imshow(dataset.pixel_array, cmap=plt.cm.bone)
    plt.show()

if __name__=="__main__":
    data=run()
    
