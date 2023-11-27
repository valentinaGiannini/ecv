# pip install -r requirements.txt
import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import numpy as np
# 
# import SimpleITK as sitk
import numpy as np

def file_selector(folder_path='C:Users/Valentina/Downloads/'):
    filenames = os.listdir(folder_path)
    selected_filename = st.selectbox('Select a file', filenames)
    return os.path.join(folder_path, selected_filename)
    
filename = file_selector()    
st.title('Calcoliamo ecv')

HT = st.number_input('Imposta valore Ematocrito')
risultato = 1- HT
# st.write(1-HT)
# st.write(f' {risultato}')

deltaBlood = st.number_input('Imposta deltablood')




#st.write(f' {filename}')
# input_path = st.file_uploader('Upload files')

basale_path = 'C:Users/Valentina/Downloads/COLLORAFI_LIDIA/basale.nii'
le_path = 'C:Users/Valentina/Downloads/COLLORAFI_LIDIA/LE.nii'



# # Read the .nii image c
# basale = sitk.ReadImage(basale_path)
# lee = sitk.ReadImage(le_path)
# ecv_array = (1-HT) * (sitk.GetArrayFromImage(lee) - sitk.GetArrayFromImage(basale))/deltaBlood
# ecv_array[ecv_array < 0.0] = 0.0
# ecv_array[ecv_array > 8.0] = 8.0
# ecv_array_int=np.round(ecv_array*10)

# ecv=sitk.GetImageFromArray(ecv_array_int)
# castFilter = sitk.CastImageFilter()
# castFilter.SetOutputPixelType(sitk.sitkInt16)

# # Convert floating type image (imgSmooth) to int type (imgFiltered)
# imgFiltered = castFilter.Execute(ecv)

# for i in range(imgFiltered.GetDepth()):
#     image_slice = imgFiltered[:, :, i]
#     sitk.WriteImage(image_slice, 'C:Users/Valentina/Downloads/COLLORAFI_LIDIA/dcm80/'+str(i)+'.dcm')
