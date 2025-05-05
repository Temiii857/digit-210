import requests
from bs4 import BeautifulSoup
import os

url = "https://onepiece.fandom.com/wiki/SBS_Volume_20"

response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

paragraphs = soup.find_all("p")

qa_pairs = []
current_question = None

for para in paragraphs:
    text = para.get_text().strip()
    if text.startswith("D:"):
        current_question = text[2:].strip()
    elif text.startswith("O:") and current_question:
        answer = text[2:].strip()
        qa_pairs.append((current_question, answer))
        current_question = None

output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "sbs_volume_20_qa.txt")
with open(output_path, "w", encoding="utf-8") as file:
    for i, (q, a) in enumerate(qa_pairs, 1):
        file.write(f"Q{i}: {q}\nA{i}: {a}\n\n")

print(f"Scraping complete. Saved {len(qa_pairs)} Q&A pairs to {output_path}")