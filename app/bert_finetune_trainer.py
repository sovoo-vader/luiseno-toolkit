# BERTFineTuneTrainer – Train BERT on Luiseño-English Parallel Corpus

from transformers import BertTokenizerFast, BertForSequenceClassification, Trainer, TrainingArguments
from datasets import Dataset
import torch

# Example dataset for illustration only
data = {
    "text": [
        "noona míyax teméq",
        "túpanax yawúsh",
        "míyax túpanax"
    ],
    "label": [0, 1, 0]  # e.g., label could be narrative category or translation ID
}

def load_dataset():
    return Dataset.from_dict(data)

def train_model():
    tokenizer = BertTokenizerFast.from_pretrained("bert-base-uncased")

    def tokenize_function(examples):
        return tokenizer(examples["text"], padding="max_length", truncation=True)

    dataset = load_dataset()
    tokenized_dataset = dataset.map(tokenize_function, batched=True)

    model = BertForSequenceClassification.from_pretrained("bert-base-uncased", num_labels=2)

    training_args = TrainingArguments(
        output_dir="./results",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=8,
        num_train_epochs=3,
        weight_decay=0.01
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        eval_dataset=tokenized_dataset
    )

    trainer.train()
    print("✅ Fine-tuning complete.")

if __name__ == '__main__':
    train_model()
