import streamlit as st
import numpy as np
import cv2
from tensorflow.keras.models import load_model
from PIL import Image
from keras.models import Sequential, load_model
from keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout, InputLayer


age_classes = {
    0: "0-2", 
    1: "3-9", 
    2: "10-19", 
    3: "20-29", 
    4: "30-39", 
    5: "40-49", 
    6: "50-59", 
    7: "60-69", 
    8: "70-79", 
    9: "80-89", 
    10: "90+"
}

# Load the pre-trained model    
# Load the trained model
model = load_model("C:\\Users\\SHWETA BHOYAR\\OneDrive\\CAPM WEB APPLICATION\\age_detection_model.h5")



# Define age bins
bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Function to preprocess uploaded image
def preprocess_image(image):
    img = np.array(image)
    img = cv2.resize(img, (100, 100))  # Resize to match model input
    img_array = img.astype('float32') / 255.0  # Normalize
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    return img_array

# Function to get age range from predicted class
def get_age_range(pred_class, bins):
    if pred_class == 0:
        return f"0 - {bins[0]}"
    elif pred_class >= len(bins):
        return f"{bins[-1]}+"
    else:
        return f"{bins[pred_class - 1]} - {bins[pred_class]}"

# Streamlit app UI
st.title("🧑‍🔬 Age Detection from Image")
st.write("Upload an image and let the model predict the age range.")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)

    try:
        # Preprocess the image
        processed_img = preprocess_image(image)

        # Make prediction
        prediction = model.predict(processed_img)
        pred_class = np.argmax(prediction)
        age_range = get_age_range(pred_class, bins)
        pred_range = age_classes[pred_class]

        st.success(f"Predicted Age Class: {pred_class}")
        st.info(f"Predicted Age Range: {age_range}")

    except Exception as e:
        st.error(f"Error during prediction: {e}")
