#Extract Entity from a text



# pip install spacy
# Load the spaCy model
# python -m spacy download en_core_web_sm

import spacy
nlp = spacy.load("en_core_web_sm")

text = open(r"2nd sem\cycle_1 NLP\Alice.txt").read()

# Process the text with spaCy NER
doc = nlp(text)

# Extract and print entities
for entity in doc.ents:
    print(f"Entity: {entity.text}, Label: {entity.label_}")