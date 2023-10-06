#Correct spelling mistakes of Given Words


#pip install pyspellchecker

from spellchecker import SpellChecker

spellcheck = SpellChecker()


words = ["programmming", "coding", "netvorking", "haaking"]

corrected_words = []

for word in words:
    corrected_word = spellcheck.correction(word)
    corrected_words.append(corrected_word)
    print(f"{word} -> {corrected_word}")

