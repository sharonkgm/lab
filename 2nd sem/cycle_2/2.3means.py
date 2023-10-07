# #Given the following data, which specify classifications for nine combinations of
# VAR1 and VAR2 predict a classification for a case where VAR1=0.906 and
# VAR2=0.606, using the result of k- means clustering with 3 means (i.e., 3
# centroids)

import numpy as np
from sklearn.cluster import KMeans

# Define your data and their corresponding classes
data = np.array([
    [1.713, 1.586, 0],
    [0.180, 1.786, 1],
    [0.353, 1.240, 1],
    [0.940, 1.566, 0],
    [1.486, 0.759, 1],
    [1.266, 1.106, 0],
    [1.540, 0.419, 1],
    [0.459, 1.799, 1],
    [0.773, 0.186, 1]
])

# Separate the features (VAR1 and VAR2) and class labels (CLASS)
X = data[:, :2]
y = data[:, 2]

# Initialize the K-Means model with 3 clusters
k = 3
kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)

# Fit the model to your data
kmeans.fit(X)

# New data point for prediction
new_case = np.array([0.906, 0.606])

# Predict the cluster for the new data point
new_case_cluster = kmeans.predict([new_case])

# Extract class labels for data points in the same cluster as the new data point
cluster_points = y[kmeans.labels_ == new_case_cluster[0]]

# Predicted class is the most frequent class in the cluster
predicted_class = int(np.argmax(np.bincount(cluster_points.astype(int))))


print("Predicted class:", predicted_class)

