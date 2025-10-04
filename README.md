# Multi-language Transliteration

This repository contains the code for training and evaluating a multi-language transliteration model.

## Code Description

- `prepare_dataset.py`: This script downloads and prepares the datasets for training.
- `train_multi_transliterator.py`: This script is used to train the transliteration model.
- `evaluate_multi_transliterator.py`: This script is used to evaluate the trained model.
- `rule_based_bengali_transliterate.py`: This script contains functions for transliterating Bengali text.

## Dataset

The model is trained on a combination of the following datasets:

- **Hindi Dataset:** `sk-community/romanized_hindi`
- **Bangla Dataset:** `sk-community/romanized_bangla`

### Bangla Dataset

We used the bangla dataset "wikimedia/wikipedia", "20231101.bn" to convert to romanized form. 

- link: https://huggingface.co/datasets/wikimedia/wikipedia/viewer/20231101.bn

Total number of rows: 143069

We seperated each para from all rows. So total number of rows for our dataset was: **975215**

To transliterate we used a heuristic method. The script rule_based_bengali_transliterate.py was used to convert all rows to romanized form.


### Hindi Dataset

We used hindi dataset from 3 different sources. 

1. **Dakshina Dataset** : We directly used dakshina romanized hindi dataset of 10,000 rows.
- Dataset hf file: `sk-community/romanized_hindi/dakshina_data/dakshina_hi_romanized.csv`
- Source link: https://github.com/google-research-datasets/dakshina
- Total number of rows: 10,000

2. **Synthetically generated** : We synthetically generated **150k** rows of hindi text and its romanized.

- Dataset hf file: `sk-community/romanized-hindi/synthetic_data.csv`
- Model used: `gemini-2.0-flash` and `gemini-2.0-flash-lite`
- Total number of rows: 150,000


3. **Converted using opensource scripts** :
We transliterated `cfilt/iitb-english-hindi` dataset using indic-trans-v2.


- Source link: https://huggingface.co/datasets/cfilt/iitb-english-hindi/
- Total number of row: 1.66 million
- Model source link:	https://github.com/libindic/indic-trans

## How to Use

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sk-research-community/multi-transliteration-llm-training.git
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

## Model

The final model is available on Hugging Face: 
- Romanized Hindi Transliterator: https://huggingface.co/sk-community/
- Romanized Bangla Transliterator: https://huggingface.co/sk-community/
- Multilingual Transliterator: https://huggingface.co/sk-community/

## Special Tokens

The following special tokens are used to specify the transliteration direction:

For multi-transliterator Model: 

- `<to_htrs>`: Hindi to English
- `<to_hbtrs>`: English to Hindi
- `<to_btrs>`: Bangla to English
- `<to_bbtrs>`: English to Bangla


For romanized hindi Model: 

- `<to_trs>`: Hindi to Roman
- `<to_btrs>`: Roman to Hindi

For romanized bangla Model: 

- `<to_trs>`: Bangla to Roman
- `<to_btrs>`: Roman to Bangla


## Evaluation

The model was evaluated on the following metrics:

- **CER (Character Error Rate):** 0.09
- **WER (Word Error Rate):** 0.13
- **chrF:** 88.39

## Citation

*Will be added later*

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
