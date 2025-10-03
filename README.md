# Multi-language Transliteration

This repository contains the code for training and evaluating a multi-language transliteration model.

## Code Description

- `prepare_dataset.py`: This script downloads and prepares the datasets for training.
- `train_multi_transliterator.py`: This script is used to train the transliteration model.
- `evaluate_multi_transliterator.py`: This script is used to evaluate the trained model.
- `bengali_transliterate.py`: This script contains functions for transliterating Bengali text.

## Dataset

The model is trained on a combination of the following datasets:

- **Hindi Dataset:** `sk-community/hindish-dataset-1.8M`
- **Bangla Dataset:** `sk-community/banglish-1.8M`

The following special tokens are used to specify the transliteration direction:

- `<to_htrs>`: English to Hindi
- `<to_hbtrs>`: Hindi to English
- `<to_btrs>`: English to Bangla
- `<to_bbtrs>`: Bangla to English

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sk-research-community/multi-transliteration.git
   ```
2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Create a `.env` file** and add your Hugging Face token:
   ```
   HF_TOKEN=your_token
   ```
4. **Prepare the dataset:**
   ```bash
   python prepare_dataset.py
   ```
5. **Train the model:**
   ```bash
   python train_multi_transliterator.py
   ```
6. **Evaluate the model:**
   ```bash
   python evaluate_multi_transliterator.py
   ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
