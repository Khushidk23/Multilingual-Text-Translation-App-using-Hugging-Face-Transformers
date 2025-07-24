# 🌐 Multilingual Text Translation App using Hugging Face Transformers

This is a simple web-based multilingual text translation application built using [Gradio](https://gradio.app/) and [Hugging Face Transformers](https://huggingface.co/transformers/). It supports translation between multiple languages including English, Hindi, Kannada, French, German, and Spanish using **free and publicly available models** from Hugging Face.

✅ **No paid API key required — powered by Hugging Face’s free and open-source model APIs.**

---

## 🚀 Features

- Translate text between:
  - English ↔ Hindi
  - English ↔ Kannada
  - Hindi ↔ Kannada
  - English → French, German, Spanish
  - German → English
- Clean and interactive web UI built with Gradio
- No login or subscription required
- 100% free to run locally or on Hugging Face Spaces

---

## 🔑 Free API Used

This app uses **Hugging Face’s free Transformers pipeline** for translation.  
It does **not require any API key or authentication**.

- Runs locally using `transformers` library.
- Can be deployed to Hugging Face Spaces with free tiers.
- Ideal for students, learners, and open-source developers.

---

## 🧠 Models Used

| Language Pair         | Hugging Face Model |
|----------------------|--------------------|
| English → Hindi      | `Helsinki-NLP/opus-mt-en-hi` |
| Hindi → English      | `Helsinki-NLP/opus-mt-hi-en` |
| English → Kannada    | `ai4bharat/indic-trans-en-kn` |
| Kannada → English    | `ai4bharat/indic-trans-kn-en` |
| Kannada → Hindi      | `ai4bharat/indic-trans-kn-hi` |
| Hindi → Kannada      | `ai4bharat/indic-trans-hi-kn` |
| English → French     | `Helsinki-NLP/opus-mt-en-fr` |
| English → German     | `Helsinki-NLP/opus-mt-en-de` |
| English → Spanish    | `Helsinki-NLP/opus-mt-en-es` |
| German → English     | `Helsinki-NLP/opus-mt-de-en` |

---

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://huggingface.co/spaces/khushidk23/Multilingual-Text-Translation-App-using-Hugging-Face-Transformers
   cd Multilingual-Text-Translation-App-using-Hugging-Face-Transformers
