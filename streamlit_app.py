import streamlit as st
from PIL import Image
import numpy as np

# Import your model code here
# from model import generate_digit_images

# Dummy version for demonstration
def generate_digit_images(number, num_images=5):
    # This should generate real images in your case
    # Dummy: generate 5 black images with text
    from PIL import ImageDraw
    images = []
    for i in range(num_images):
        img = Image.new('L', (128, 128), color=255)
        d = ImageDraw.Draw(img)
        d.text((40, 50), str(number), fill=0)
        images.append(img)
    return images


st.set_page_config(page_title="Handwritten Digit Generator", layout="centered")

st.title("🖋️ Handwritten Digit Generator")

number = st.text_input("Enter a single digit (0-9):", max_chars=1)

if st.button("Generate Handwritten Images"):
    if number.isdigit() and 0 <= int(number) <= 9:
        st.success(f"Generating handwritten images for: **{number}**")

        images = generate_digit_images(int(number), num_images=5)

        # Display images in a row
        cols = st.columns(5)
        for idx, img in enumerate(images):
            with cols[idx]:
                st.image(img, caption=f"Image {idx+1}", use_column_width=True)
    else:
        st.error("❗ Please enter a **single digit number** between 0 and 9.")
