import pickle
import torch
import sys
from tqdm import tqdm
from transformers import AutoModelForSeq2SeqLM
import main_03_tokenizer as tok


model_name = tok.model_name
fragment_encoded = tok.fragment_encoded
tokenizer = tok.tokenizer

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
if device == "cpu":
    print("torch.cuda is not available, exiting...")
    sys.exit(0)
print('running on', device)

model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

with torch.no_grad():
    fragment_decoded = []
    for tokenized_text in tqdm(fragment_encoded):
        translation = model.generate(**tokenized_text)
        fragment_decoded.append(translation)


fragments = []
for translation in fragment_decoded:
    fragment = []
    for i in tqdm(range(len(translation))):
        fragment.append(tokenizer.decode(
            translation[i], skip_special_tokens=True))
    fragments.append(fragment)

with open("data/output/fragment_decoded.pickle", "wb") as f:
    pickle.dump(fragments, f)


print("Done!")
