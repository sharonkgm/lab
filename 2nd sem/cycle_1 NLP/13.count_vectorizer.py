#Convert Text Features using a count vectoriser

from sklearn.feature_extraction.text import CountVectorizer

corpus = [
    "This is the first document.",
    "This document is the second document.",
    "And this is the third one.",
    "Is this the first document?"
]

vectorizer = CountVectorizer()

X = vectorizer.fit_transform(corpus)

import pandas as pd

df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())

print(df)
