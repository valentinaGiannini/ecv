import streamlit as st
import pandas as pd
import numpy as np
!pip install SimpleITK 
import SimpleITK as sitk
import numpy as np

st.title('Calcoliamo ecv')



basale_path = 'C:Users/Valentina/Downloads/COLLORAFI_LIDIA/basale.nii'
le_path = 'C:Users/Valentina/Downloads/COLLORAFI_LIDIA/LE.nii'


# Read the .nii image c
basale = sitk.ReadImage(basale_path)
lee = sitk.ReadImage(le_path)
ecv_array = 0.6 * (sitk.GetArrayFromImage(lee) - sitk.GetArrayFromImage(basale))/198.0
ecv_array[ecv_array < 0.0] = 0.0
ecv_array[ecv_array > 8.0] = 8.0
ecv_array_int=np.round(ecv_array*10)

ecv=sitk.GetImageFromArray(ecv_array_int)
castFilter = sitk.CastImageFilter()
castFilter.SetOutputPixelType(sitk.sitkInt16)

# Convert floating type image (imgSmooth) to int type (imgFiltered)
imgFiltered = castFilter.Execute(ecv)

for i in range(imgFiltered.GetDepth()):
    image_slice = imgFiltered[:, :, i]
    sitk.WriteImage(image_slice, 'C:Users/Valentina/Downloads/COLLORAFI_LIDIA/dcm80/'+str(i)+'.dcm')
