import spacy
import os

# Load the spaCy medium English model
nlp = spacy.load("en_core_web_md")

# Read the SBS volume text
with open("vol-10.txt", "r", encoding="utf-8") as file:
    text = file.read()

# Process the text
doc = nlp(text)

# Extract adjectives
adjectives = [token.text for token in doc if token.pos_ == "ADJ"]

# Create output directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Save to TSV file
output_path = os.path.join(output_dir, "vol10_adjectives.tsv")
with open(output_path, "w", encoding="utf-8") as file:
    for adj in adjectives:
        file.write(f"{adj}\n")