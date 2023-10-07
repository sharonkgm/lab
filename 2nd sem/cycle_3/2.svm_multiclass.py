# Download any multi class numerical dataset from UCI repostiory and do the classification with 
# a. SVM with majority voting

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.ensemble import VotingClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


# Load the downloaded dataset and preprocess it
# Replace 'your_dataset.csv' with the actual dataset filename
data = pd.read_csv(r'2nd sem\cycle_3\dataset\iris.csv')

# Assuming the target column is named 'target' and the features are in other columns
X = data.iloc[:, :-1] 
y = data.iloc[:, -1] 

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# SVM classifiers with different kernels
svm_model_1 = SVC(kernel='linear')
svm_model_2 = SVC(kernel='rbf')
svm_model_3 = SVC(kernel='poly')

# Create the Voting Classifier with SVM models
voting_model = VotingClassifier(estimators=[('svm1', svm_model_1), ('svm2', svm_model_2), ('svm3', svm_model_3)],
                                voting='hard')

# Fit the Voting Classifier on the training data
voting_model.fit(X_train, y_train)

# Predict the labels for the test data
y_pred = voting_model.predict(X_test)

# Calculate the accuracy of the majority voting classifier
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print("Accuracy:", accuracy)