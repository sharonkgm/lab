#Remove Stop Words FromText data


import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
stop_words = set(stopwords.words('english'))
with open(r"2nd sem\cycle_1 NLP\Alice.txt", 'r') as text_file:
    text = text_file.read()

#tokenize text into words
words = word_tokenize(text)
nonstop_words= []

for word in words:
    if word.lower() not in stop_words:
        nonstop_words.append(word)

filtered_text = ' '.join(nonstop_words)
print(filtered_text)