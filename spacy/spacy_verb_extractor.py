import spacy
from bs4 import BeautifulSoup


nlp = spacy.load("en_core_web_sm")


with open("vol-4.xml", "r", encoding="utf-8") as file:
    xml_data = file.read()


soup = BeautifulSoup(xml_data, "xml")
say_elements = soup.find_all("say")
say_texts = " ".join([s.get_text() for s in say_elements])


doc = nlp(say_texts)


verbs = [token.text for token in doc if token.pos_ == "VERB"]

with open("verbFreq.txt", "w", encoding="utf-8") as out_file:
    for verb in verbs:
        out_file.write(verb + "\n")