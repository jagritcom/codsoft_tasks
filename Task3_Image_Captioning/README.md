# Task 3 — Image Captioning

## Objective
Combine computer vision and natural language processing to generate captions for images.

## Model
This implementation uses the pretrained `Salesforce/blip-image-captioning-base` model through Hugging Face Transformers. BLIP performs visual-language understanding and generates a caption from the uploaded image.

## Run
```bash
pip install -r ../requirements.txt
streamlit run app.py
```

## Notes
- Internet access is required the first time the model is downloaded.
- Model loading and caption generation can take longer on CPU.
- Upload a JPG, JPEG, PNG, or WEBP image.
