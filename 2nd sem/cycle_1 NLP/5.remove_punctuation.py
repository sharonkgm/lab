#Remove Punctuations from text data


import string


text="hii what's up!!?"
print("\nBefore removing punctuations, text is:",text)
for char in string.punctuation:
    text=text.replace(char,"")
print("\n\nAfter removing punctuations, text is:",text)