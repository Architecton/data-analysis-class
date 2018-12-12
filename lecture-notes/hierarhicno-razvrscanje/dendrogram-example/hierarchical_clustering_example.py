import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# Read data matrix from file.
data_mat = np.genfromtxt("data.txt", delimiter="   ")

# Encode hierarchical clustering in a linkage_matrix using the ward distance as comparison.
linkage_matrix = linkage(data_mat, 'ward')

# Create dendrogram.
dend = dendrogram(linkage_matrix, truncate_mode = 'none', orientation = 'left')

# Add title to dendrogram.
plt.title('Hierarchical Clustering Example')

# Show dendrogram.
plt.show()