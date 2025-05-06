import spacy
import pandas as pd

# Load spaCy's medium English model
nlp = spacy.load("en_core_web_md")

# Read in your text file
with open("vol-10.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Process the text
doc = nlp(text)

# Pull all adjectives
adjectives = []
for token in doc:
    if token.pos_ == "ADJ":
        adjectives.append((token.text, token.sent.start_char))

# Save to TSV
df = pd.DataFrame(adjectives, columns=["adjective", "char_offset"])
df.to_csv("adjectives_vol10.tsv", sep="\t", index=False)