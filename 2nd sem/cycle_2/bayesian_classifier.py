#) Construct a Bayesian classifier using Titanic survival prediction dataset.
#Calculate the accuracy, precision, and recall for the data set.

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score

# Load the Titanic dataset
df = pd.read_csv('2nd sem\cycle_2\dataset\Titanic_dataset.csv')

# Handle missing values (e.g., fill missing ages with the mean)
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Encode categorical features like 'Sex' and 'Embarked'
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])
df['Embarked'] = le.fit_transform(df['Embarked'])

# Split the dataset into features (X) and target labels (y)
X = df[['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']]
y = df['Survived']

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
