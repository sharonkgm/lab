# Generate N-Grams For a Given Sentence

import nltk
from nltk.util import ngrams
from nltk.tokenize import word_tokenize

sentence = "Alice was beginning to get very tired of sitting by her sister on the bank."

words = word_tokenize(sentence)

# Generate N-grams
n_grams = list(ngrams(words, 3))

# Print the N-grams(trigram)
for n_gram in n_grams:
    print(n_gram)
