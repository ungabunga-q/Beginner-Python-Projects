"""
K-Means Clustering Demo
----------------------
Clusters random data points and plots the result.

Steps for Beginners:
1. Import numpy, matplotlib, and sklearn.cluster.KMeans.
2. Generate random data points.
3. Fit KMeans to the data.
4. Plot the clusters and centroids.
"""

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# 2. Generate random data
X = np.random.rand(50, 2)

# 3. Fit KMeans
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)
labels = kmeans.labels_
centers = kmeans.cluster_centers_

# 4. Plot
plt.scatter(X[:,0], X[:,1], c=labels, cmap='viridis')
plt.scatter(centers[:,0], centers[:,1], c='red', marker='x', s=100, label='Centroids')
plt.title('K-Means Clustering')
plt.legend()
plt.show()
