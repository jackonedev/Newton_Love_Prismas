from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
import sys
import main_02_processing as pro
from tqdm import tqdm
import threading


## path output
path_out = pro.path_out


##  control variables
fragment_to_translate = 0
number_of_paragraphs = 10


## Load data
df = pro.df
model_name = "Helsinki-NLP/opus-mt-en-es"


## Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if device == "cpu":
    print("torch.cuda is not available, exiting...")
    sys.exit(0)


##  Tokenizer and model initialization
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)


## Function that execute the model
translated = {}
def translate(input_ids, posicion):
    with torch.no_grad():
        trans = model.generate(**input_ids)
        translated[posicion] = trans


## Thread execution
if number_of_paragraphs == 0:
    number_of_paragraphs = df.shape[0]
batch = df.iloc[:number_of_paragraphs, fragment_to_translate].dropna().to_list()
threads = []
print("Tokenization...")
for i in tqdm(range(len(batch))):
    tokenized_text = tokenizer(
        batch[i], padding=True, truncation=True, return_tensors="pt")
    t = threading.Thread(target=translate, args=(tokenized_text, i))
    t.start()
    threads.append(t)

print("Translating...")
for t in tqdm(threads):
    t.join()


## Decode
translates = []
print("Decoding...")
for i in tqdm(range(len(translated))):
    trans = tokenizer.decode(translated[i][0], skip_special_tokens=True)
    translates.append(trans)


## show results
print("Saving results...")

## save results
save_path = f"{path_out}/translated_fragment_{fragment_to_translate+1}.txt"
with open(save_path, "w") as f:
    f.write("\n\n".join(translates))
    
print(f"Translated succesfully saved in {save_path}")

