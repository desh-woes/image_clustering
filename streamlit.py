from turtle import width
import streamlit as st
from PIL import Image
import os

st.write(
    """
    # Google Images Clustering
    A Machine Learning App that clusters product images according to either the similarity of the images or the similarity of the texts that describe the images.
    """
)

directory = 'C:\\Users\\Joyce\\Documents\\Clustering images\\Output\\'
clusters = []
images = []

i = 1
for folder in os.listdir(directory):
    clusters.append(folder)
    st.header('Cluster ' + str(i))
    for filename in os.listdir(directory+folder):
        images.append(filename)
        image = Image.open(directory+folder+'\\'+filename)
        st.image(image, caption=filename, width=500)
    i+=1