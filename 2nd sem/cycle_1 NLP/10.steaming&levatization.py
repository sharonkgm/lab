#Perform steaming and levetization on Text

import nltk
from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('wordnet')

text = open(r"2nd sem\cycle_1 NLP\Alice.txt").read()

words = word_tokenize(text)

stemmer = PorterStemmer()
lemmatizer = WordNetLemmatizer()

stemmed_words = [stemmer.stem(word) for word in words]
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

print("Original Text:", text)
print("\nStemmed Text:", ' '.join(stemmed_words))
print("\nLemmatized Text:", ' '.join(lemmatized_words))

