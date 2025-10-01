# Hindish Transliteration

This repository contains the code for training and evaluating a Hindish to Devanagari transliteration model.

## Code Description

- `train_hindish_transliterator.py`: This script is used to train the transliteration model.
- `evaluate_hindish_transliterator.py`: This script is used to evaluate the trained model.
- `bengali_transliterate.py`: This script contains functions for transliterating Bengali text.

## Dataset

The model was trained on a combination of the following datasets:

- **IITB English-Hindi Corpus:** https://huggingface.co/datasets/cfilt/iitb-english-hindi
- **Dakshina Dataset:** https://github.com/google-research-datasets/dakshina
- **Synthetic Data:** Generated using Gemini 2.0 Flash and Gemini 2.0 Flash-lite.
- **Romanized Bangla Para Wise Split:** https://huggingface.co/datasets/sk-community/romanized_bangla_para_wise_split

The total dataset size is 1.8 million rows.

## Model

The final model is available on Hugging Face: https://huggingface.co/sk-community/HindishFormer-worked

## Evaluation

The model was evaluated on the following metrics:

- **CER (Character Error Rate):** 0.09
- **WER (Word Error Rate):** 0.13
- **chrF:** 88.39

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/hindish-transliteration.git
   ```
2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a `.env` file** and add your Hugging Face token:
   ```
   HF_TOKEN=your_token
   ```
4. **Train the model:**
   ```bash
   python train_hindish_transliterator.py
   ```
5. **Evaluate the model:**
   ```bash
   python evaluate_hindish_transliterator.py
   ```