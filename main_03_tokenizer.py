from transformers import AutoTokenizer
import main_02_processing as pro


df = pro.df
model_name = "Helsinki-NLP/opus-mt-en-es"

tokenizer = AutoTokenizer.from_pretrained(model_name)

fragment_encoded = []
for i in range(df.shape[1]):
    batch = df.iloc[:, i].dropna().to_list()

    tokenized_text = tokenizer(
        batch, padding=True, truncation=True, return_tensors="pt")

    fragment_encoded.append(tokenized_text)

print("Tokenization Done!")
print(f"fragment_encoded: {len(fragment_encoded)}")