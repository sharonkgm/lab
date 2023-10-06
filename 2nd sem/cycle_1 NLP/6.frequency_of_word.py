#Print The frequency of words in a document


import nltk
nltk.download()
import PyPDF2
from nltk.tokenize import word_tokenize

file=open(r"2nd sem\cycle_1 NLP\Alice.txt").read()
# readFile=PyPDF2.PdfReader(file)
# text=readFile.pages[0].extract_text()
token=word_tokenize(file)

frequency={}
for i in token:
    frequency[i]=token.count(i)

print(frequency)






