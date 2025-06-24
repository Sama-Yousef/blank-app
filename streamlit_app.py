import streamlit as st
from PIL import Image
import numpy as np
from tensorflow.keras.layers import LeakyReLU


# Import your model code here
# from model import generate_digit_images
from tensorflow.keras.models import load_model
import tensorflow as tf

generator = load_model("CGAN_generator_model.h5", custom_objects={"LeakyReLU": LeakyReLU})



from PIL import Image
import numpy as np

def generate_digit_images(number, num_images=5, latent_dim=100):
    """
    Generate handwritten digit images using a pre-trained CGAN generator.
    
    Args:
        number (int): The digit to generate (0-9).
        num_images (int): Number of images to generate.
        latent_dim (int): Dimension of the generator's noise input.
        
    Returns:
        list of PIL.Image: Generated digit images.
    """
    # ✅ Generate random noise vectors
    noise = np.random.normal(0, 1, (num_images, latent_dim))

    # ✅ One-hot encode the digit labels → shape = (num_images, num_classes)
    labels = tf.keras.utils.to_categorical([number] * num_images, num_classes=10)

    # ✅ Generate images from the generator
    generated_images = generator.predict([noise, labels], verbose=0)

    # ✅ Rescale from [-1, 1] → [0, 255]
    generated_images = 0.5 * (generated_images + 1) * 255
    generated_images = generated_images.astype(np.uint8)

    # ✅ Convert to list of PIL.Image
    images = []
    for img_array in generated_images:
        img = Image.fromarray(img_array.squeeze(), mode='L')
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
                st.image(img, caption=f"Image {idx+1}", use_container_width=True)
    else:
        st.error("❗ Please enter a **single digit number** between 0 and 9.")
