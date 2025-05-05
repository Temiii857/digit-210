import nltk
import nltk.corpus

nltk.download('book')
from nltk.book import *
from urllib import request

nltk.download('gutenberg')
nltk.download('punkt')

emma_words = gutenberg.words('austen-emma.txt')
bible_words = gutenberg.words('bible-kjv.txt')
def lexical_diversity(text):
    return len(set(text)) / len(text)

print("Lexical diversity of Emma:", round(lexical_diversity(emma_words), 4))
print("Lexical diversity of Bible:", round(lexical_diversity(bible_words), 4))

fdist_emma = FreqDist(emma_words)
fdist_bible = FreqDist(bible_words)

print("\nMost common words in Emma:", fdist_emma.most_common(10))
print("\nMost common words in Bible:", fdist_bible.most_common(10))


emma_text = nltk.Text(emma_words)
bible_text = nltk.Text(bible_words)

print("\nWords similar to 'love' in Emma:")
emma_text.similar('love')

print("\nWords similar to 'love' in Bible:")
bible_text.similar('love')