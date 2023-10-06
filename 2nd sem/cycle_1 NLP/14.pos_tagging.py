#Tag The Parts Of Speech (POS Tagging) in a Sentence

import nltk

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')


sentence = "Alice was beginning to get very tired of sitting by her sister on the bank."


words = nltk.word_tokenize(sentence)


pos_tags = nltk.pos_tag(words)

print(pos_tags)
