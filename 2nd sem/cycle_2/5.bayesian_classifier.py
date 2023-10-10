#) Construct a Bayesian classifier using Titanic survival prediction dataset.
#Calculate the accuracy, precision, and recall for the data set.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the Titanic dataset
data = pd.read_csv('2nd sem\cycle_2\dataset\Titanic_dataset.csv')

# Prepare the dataset
data = data[['Survived', 'Pclass', 'Sex', 'Age', 'SibSp', 'Parch']]
data = data.dropna()

data['Sex'] = data['Sex'].map({'female': 0, 'male': 1})

# Split the dataset into features (X) and target labels (y)
X = data.drop('Survived', axis=1)
y = data['Survived']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the Bayesian classifier
bayesian_classifier = GaussianNB()
bayesian_classifier.fit(X_train, y_train)

# Make predictions on the test data
y_pred = bayesian_classifier.predict(X_test)

# Calculate accuracy, precision, and recall
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)

print(f"Accuracy: {accuracy * 100:.2f}%")
print(f"Precision: {precision * 100:.2f}%")
print(f"Recall: {recall * 100:.2f}%")
