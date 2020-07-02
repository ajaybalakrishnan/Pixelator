import streamlit as st
import cv2
from PIL import Image
import numpy as np
import io
from predict import predict


st.title("Super Resolution")
st.subheader("Low Resolution to High Resoulution image Converter")


st.markdown("Upload an low resolution image")


uploaded_file = st.file_uploader("Choose an low resolution image to be uploaded", type = ("jpg", "png", "jpeg"))
if uploaded_file is not None:
    st.image(uploaded_file,
            caption = "Uploaded Image")
    image = Image.open(uploaded_file)
    pred = predict(image)
    st.image(pred, caption = "Output Image")






