import nltk
import os
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet


nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')
nltk.download('omw-1.4')

def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None

words_to_check = ["play", "run", "light", "work", "draw", "right", "game", "break"]
volume_files = ["vol-21.txt", "vol-22.txt", "vol-23.txt"]

os.makedirs("outputSBS", exist_ok=True)

for filename in volume_files:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()

    tokens = word_tokenize(text)
    tagged = pos_tag(tokens)

    results = []
    for word in words_to_check:
        pos = pos_tag([word])[0][1]
        wn_pos = get_wordnet_pos(pos)
        if wn_pos:
            synsets = wordnet.synsets(word, pos=wn_pos)
        else:
            synsets = wordnet.synsets(word)
        results.append(f"{word} ({pos}) - {len(synsets)} synsets")

    output_path = f"outputSBS/{filename.replace('.txt', '')}_wordnet.txt"
    with open(output_path, "w", encoding="utf-8") as out_file:
        for line in results:
            out_file.write(line + "\n")