 #Convert Text Data Into Lowercase

import PyPDF2
import nltk

file=open(r"2nd sem\cycle_1 NLP\Alice.txt").read()
# readFile=PyPDF2.PdfReader(file)
# text=readFile.pages[0].extract_text()
lower=file.lower()
print("\nBefore converting to lowercase text is:\n\n",file)
print("\nAfter converting to lowercase text is:\n\n",lower)
