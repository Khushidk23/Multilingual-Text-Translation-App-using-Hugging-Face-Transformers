# 🌐 Multilingual Translator App

This is a simple web-based multilingual text translation application built using [Gradio](https://gradio.app/) and [Hugging Face Transformers](https://huggingface.co/transformers/). It allows users to translate text between multiple languages including English, Hindi, Kannada, French, German, and Spanish using **free models and APIs from Hugging Face**.

✅ **No paid API key required — powered by free Hugging Face models and pipelines!**

---

## 🚀 Features

- Translate text between:
  - English ↔ Hindi
  - English ↔ Kannada
  - Hindi ↔ Kannada
  - English → French, German, Spanish
  - German → English
- Clean and simple user interface using Gradio
- No login, no paid plans — uses free Hugging Face resources
- Suitable for learning, academic projects, and demos

---

## 🔑 Free API Used

This app uses **Hugging Face's free model inference pipeline** via the `transformers` library.

- No paid API key is needed.
- No API usage limits unless deployed on restricted infrastructure.
- All models run locally (or in a Hugging Face Space) using open-source pretrained models.

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
   git clone https://huggingface.co/spaces/khushidk23/translator-app
   cd translator-app
