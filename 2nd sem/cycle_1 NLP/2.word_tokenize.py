# Read Text from an File and Print them as Tokens(Use Alice Text passage)


import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize

data = open(r"2nd sem\cycle_1 NLP\Alice.txt").read()
print(data)
words = word_tokenize(data)
print(words)