# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 00:26:25 2020

@author: SantiagoCaroZ
"""
import pydicom

dataset=pydicom.dcmread("actividad.dcm")
dataset.PatientAge="22"
dataset[0x0010,0x0010].value="Santiago Caro Zapata"
dataset[0x0010,0x0020].value="1035440607"



dataset.save_as("respuesta.dcm")