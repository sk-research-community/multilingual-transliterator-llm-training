
import pandas as pd
from datasets import load_dataset
from sklearn.model_selection import train_test_split

def main():
    # Load Hindi dataset
    hindi_dataset = load_dataset("sk-community/hindish-dataset-1.8M", split="train")

    # Load Bangla dataset
    bangla_dataset = load_dataset("sk-community/banglish-1.8M", split="train")

    # Process datasets
    processed_data = []

    # Process Hindi dataset
    for item in hindi_dataset:
        # English to Hindi
        processed_data.append({'source': '<to_htrs>' + item['en'], 'target': item['hi']})
        # Hindi to English
        processed_data.append({'source': '<to_hbtrs>' + item['hi'], 'target': item['en']})

    # Process Bangla dataset
    for item in bangla_dataset:
        # English to Bangla
        processed_data.append({'source': '<to_btrs>' + item['en'], 'target': item['bn']})
        # Bangla to English
        processed_data.append({'source': '<to_bbtrs>' + item['bn'], 'target': item['en']})

    # Create a DataFrame
    df = pd.DataFrame(processed_data)

    # Split the data into training and testing sets
    train_df, test_df = train_test_split(df, test_size=0.1, random_state=42)

    # Save to CSV
    train_df.to_csv("train.csv", index=False)
    test_df.to_csv("test.csv", index=False)

if __name__ == "__main__":
    main()
