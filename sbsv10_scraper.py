import spacy
import os


nlp = spacy.load("en_core_web_md")


with open("vol-10.txt", "r", encoding="utf-8") as file:
    text = file.read()


doc = nlp(text)


adjectives = [token.text for token in doc if token.pos_ == "ADJ"]


output_dir = "output"
os.makedirs(output_dir, exist_ok=True)


output_path = os.path.join(output_dir, "vol10_adjectives.tsv")
with open("output/vol10_adjectives.tsv", "w", encoding="utf-8") as f:
    f.write("Word\tPartOfSpeech\n")
    for token in doc:
        if token.pos_ == "ADJ":
            f.write(f"{token.text}\t{token.pos_}\n")