import os
from dotenv import load_dotenv
import pandas as pd
import torch
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from datasets import Dataset
from jiwer import cer, wer

load_dotenv()

def main():
    # Load the dataset
    test_df = pd.read_csv("Hindish-Training/hindi/test.csv")
    test_dataset = Dataset.from_pandas(test_df)

    # Load tokenizer and model
    model_checkpoint = "sk-community/HindishFormer"
    tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
    model = AutoModelForSeq2SeqLM.from_pretrained(model_checkpoint)

    # Set device
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # Evaluation
    def evaluate(examples):
        inputs = [ex for ex in examples["source"]]
        targets = [ex for ex in examples["target"]]

        # Tokenize inputs and generate predictions
        inputs = tokenizer(inputs, return_tensors="pt", padding=True, truncation=True, max_length=128).to(device)
        with torch.no_grad():
            outputs = model.generate(**inputs)
        predictions = tokenizer.batch_decode(outputs, skip_special_tokens=True)

        # Calculate metrics
        cer_score = cer(targets, predictions)
        wer_score = wer(targets, predictions)

        return {"cer": cer_score, "wer": wer_score, "predictions": predictions, "targets": targets}

    results = test_dataset.map(evaluate, batched=True, batch_size=16)

    # Print results
    for i in range(10):
        print(f"Example {i+1}:")
        print(f"  Input: {test_dataset[i]['translation']['en']}")
        print(f"  Target: {results[i]['targets']}")
        print(f"  Prediction: {results[i]['predictions']}")
        print("---")

    print(f"Overall CER: {results.column_names}")

if __name__ == "__main__":
    main()
