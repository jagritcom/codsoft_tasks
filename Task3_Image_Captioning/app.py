import streamlit as st
from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration

st.set_page_config(page_title="AI Image Captioning", page_icon="🖼️")
st.title("🖼️ AI Image Captioning")
st.caption("Upload an image and generate a natural-language caption with a pretrained BLIP model.")

@st.cache_resource(show_spinner="Loading the image-captioning model (first run may take a few minutes)...")
def load_model():
    model_name = "Salesforce/blip-image-captioning-base"
    processor = BlipProcessor.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(model_name)
    model.eval()
    return processor, model

uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png", "webp"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)

    if st.button("✨ Generate caption", type="primary"):
        try:
            processor, model = load_model()
            inputs = processor(images=image, return_tensors="pt")
            with torch.no_grad():
                output = model.generate(**inputs, max_new_tokens=40)
            caption = processor.decode(output[0], skip_special_tokens=True)
            st.subheader("Generated caption")
            st.success(caption)
        except Exception as exc:
            st.error("The model could not generate a caption. Check your internet connection and installed dependencies, then try again.")
            st.caption(f"Technical details: {exc}")
else:
    st.info("Upload an image to begin.")

with st.expander("How it works"):
    st.write("BLIP is a pretrained vision-language model. It processes the image, represents its visual content, and generates a text sequence describing the scene.")
