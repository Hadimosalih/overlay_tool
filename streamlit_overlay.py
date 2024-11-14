import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt
import io

# App title
st.title("Interaktive Bildüberlagerung")

# File uploader
original_file = st.file_uploader("Lade das Originalbild hoch", type=["png", "jpg", "jpeg"])
segmented_file = st.file_uploader("Lade das segmentierte Bild hoch", type=["png", "jpg", "jpeg"])

# Transparenz-Schieberegler
alpha = st.slider("Transparenz der Überlagerung", min_value=0.0, max_value=1.0, value=0.5, step=0.05)

if original_file and segmented_file:
    # Load images
    original_image = Image.open(original_file).convert('L')
    segmented_image = Image.open(segmented_file).convert('L').resize(original_image.size, Image.NEAREST)

    # Create overlay
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(original_image, cmap='gray', alpha=1 - alpha)
    ax.imshow(segmented_image, cmap='viridis', alpha=alpha)
    ax.axis('off')

    # Render the plot in Streamlit
    st.pyplot(fig)
