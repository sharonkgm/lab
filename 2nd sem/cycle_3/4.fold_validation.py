#Download any numerical dataset from UCI repository and do the classification
# process with SVM as said below
# a. 10 fold validation
# b. with dataset 80:20, 70:30 and 60:40
# c. prepare a comparison table of F1 score for a and b

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import f1_score
from sklearn.datasets import load_wine

# Load the dataset (replace 'your_dataset.csv' with the actual dataset filename)
data = load_wine()
X, y = data.data, data.target
# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create an SVM classifier
svm_classifier = SVC(kernel='linear')

# a. 10-fold cross-validation
cv_scores = cross_val_score(svm_classifier, X_scaled, y, cv=10, scoring='f1_macro')

# b. Train-test splits (80:20, 70:30, 60:40)
splits = [0.2, 0.3, 0.4]
f1_scores = []

for split in splits:
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=split, random_state=42)
    svm_classifier.fit(X_train, y_train)
    y_pred = svm_classifier.predict(X_test)
    f1 = f1_score(y_test, y_pred, average='macro')
    f1_scores.append(f1)

# c. Prepare a comparison table of F1 scores for a and b
comparison_table = pd.DataFrame({
    'Validation Method': ['10-fold CV'] + [f'{int(100 * (1 - split))}:{int(100 * split)}' for split in splits],
    'F1 Score': [cv_scores.mean()] + f1_scores
})

print(comparison_table)
