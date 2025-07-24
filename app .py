import gradio as gr
from transformers import pipeline


LANGUAGE_MODELS = {
    "English to Hindi": ("translation_en_to_hi", "Helsinki-NLP/opus-mt-en-hi"),
    "Hindi to English": ("translation_hi_to_en", "Helsinki-NLP/opus-mt-hi-en"),
    "English to Kannada": ("translation", "ai4bharat/indic-trans-en-kn"),
    "Kannada to English": ("translation", "ai4bharat/indic-trans-kn-en"),
    "Kannada to Hindi": ("translation", "ai4bharat/indic-trans-kn-hi"),
    "Hindi to Kannada": ("translation", "ai4bharat/indic-trans-hi-kn"),
    "English to French": ("translation_en_to_fr", "Helsinki-NLP/opus-mt-en-fr"),
    "English to German": ("translation_en_to_de", "Helsinki-NLP/opus-mt-en-de"),
    "English to Spanish": ("translation_en_to_es", "Helsinki-NLP/opus-mt-en-es"),
    "German to English":("translation_de_to_en","Helsinki-NLP/opus-mt-de-en"),

}

def translate_text(text, language_pair):
    task, model_name = LANGUAGE_MODELS[language_pair]
    translator = pipeline(task, model=model_name)
    output = translator(text, max_length=512)
    return output[0]['translation_text']

gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(lines=4, label="Enter Text"),
        gr.Dropdown(choices=list(LANGUAGE_MODELS.keys()), label="Select Language Pair")
    ],
    outputs=gr.Textbox(lines=4, label="Translated Text"),
    title="Multilingual Translator 🇬🇧 🇮🇳",
    description="Supports English, Hindi, and Kannada translation using Hugging Face models."
).launch()
