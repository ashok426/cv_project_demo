import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

# Load trained model
model = tf.keras.models.load_model("best_model.h5")

# Define class names
classes = ['Indian market', 'Onion', 'Potato', 'Tomato']  # Make sure order matches your training

# Set image size
IMG_SIZE = 224

st.title("Vegetable Image Classifier")
st.markdown("Upload an image of **Onion**, **Tomato**, **Potato**, or an **Indian Market Scene**.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Preprocess
    img = image.resize((IMG_SIZE, IMG_SIZE))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Predict
    prediction = model.predict(img_array)
    class_idx = np.argmax(prediction)
    class_label = classes[class_idx]

    st.subheader(f"Prediction: **{class_label}**")
