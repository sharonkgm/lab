# Download any numerical dataset with more than 1000 features. Reduce the
# feature dimension with the help of PCA. 
# Do the following experiments
# a. Reduce the feature dimension to 300, 400, 500  
# b. Perform the machine learning with svm for the different dimensions
# mentioned in a.
# c. Find precision recall and F1 score of all the experiments said in b.
# d. Prepare a comparison table of c.


import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.svm import SVC
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split


# Load the dataset (replace 'your_dataset.csv' with the actual dataset filename)
data = pd.read_csv(r'2nd sem\cycle_3\dataset\1000_features.csv')

# Assuming the dataset has features in columns and a target column (if applicable)
X = data.iloc[:, :-1] 
y = data.iloc[:, -1] 

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

dimensions = [300, 400, 500]  # Dimensions to experiment with

results = []

for n_components in dimensions:
    # Create a PCA instance and specify the number of components
    pca = PCA(n_components=n_components)

    # Fit PCA to the scaled data and transform
    X_pca = pca.fit_transform(X_scaled)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X_pca, y, test_size=0.2, random_state=42)

    # Create and train an SVM classifier
    svm_classifier = SVC(kernel='linear')
    svm_classifier.fit(X_train, y_train)

    # Make predictions
    y_pred = svm_classifier.predict(X_test)

    # Calculate precision, recall, and F1 score
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    f1 = f1_score(y_test, y_pred, average='weighted')

    # Store results
    results.append([n_components, precision, recall, f1])

# Create a DataFrame to display results
results_data = pd.DataFrame(results, columns=['PCA Components', 'Precision', 'Recall', 'F1 Score'])
print(results_data)
