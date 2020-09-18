# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:42:03 2020

@author: SantiagoCaroZ
"""


import datetime

import pydicom
from pydicom.dataset import Dataset, FileDataset, FileMetaDataset

# Create some temporary filenames


filename_big_endian = "actividad.dcm"


# Populate required values for file meta information
file_meta = FileMetaDataset()
file_meta.MediaStorageSOPClassUID = '1.2.840.10008.5.1.4.1.1.2'
file_meta.MediaStorageSOPInstanceUID = "1.2.3"
file_meta.ImplementationClassUID = "1.2.3.4"


# Create the FileDataset instance (initially no data elements, but file_meta
# supplied)
ds = FileDataset(filename_big_endian, {},
                 file_meta=file_meta, preamble=b"\0" * 128)

# Add the data elements -- not trying to set all required here. Check DICOM
# standard
ds.PatientName = "Charli Muñoz"
ds.PatientID = "055088"
ds.BodyPartExamined="Face"
ds.PatientSex="M"
ds.PatientBirthDate="00/00/00"
ds.PatientAge="22"
# Set creation date/time
dt = datetime.datetime.now()
ds.ContentDate = dt.strftime('%Y%m%d')
timeStr = dt.strftime('%H%M%S.%f')  # long format with micro seconds
ds.ContentTime = timeStr

# 

# Write as a different transfer syntax XXX shouldn't need this but pydicom
# 0.9.5 bug not recognizing transfer syntax
ds.file_meta.TransferSyntaxUID = pydicom.uid.ExplicitVRBigEndian
ds.is_little_endian = False
ds.is_implicit_VR = False

print("Writing test file as Big Endian Explicit VR", filename_big_endian)
ds.save_as(filename_big_endian)

