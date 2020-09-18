# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 16:37:31 2020

@author: Carlos Jose Munoz
Asociación con Echo SCP
"""

from pynetdicom import AE, debug_logger #importa la clase 

debug_logger()

ae = AE()#se cra una instancia AE
ae.add_requested_context('1.2.840.10008.1.1')#se crea una solicitud de asociación con un contexto de presentación
assoc = ae.associate('localhost', 11112)#inicio de la negociación de asociación con la IP en el puerto dado
if assoc.is_established:
    status=assoc.send_c_echo() #solicitar el uso de su servicio de verificación
    print('Association established with Echo SCP!')
    assoc.release()
else:
     # Association rejected, aborted or never connected
     print('Failed to associate')