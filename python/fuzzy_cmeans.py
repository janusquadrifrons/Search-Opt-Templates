# fuzzy c_means

import numpy as np
import matplotlib.pyplot as plt
from skfuzzy import cmeans

# Generate test data
np.random.seed(42)
data = np.random.randn(100, 2)

# Define the number of clusters
c = 3

# Define the fuzziness parameter
m = 2

# Cluster the data
centers, u, u0, d, jm, p, fpc = cmeans(data.T, c, m, error=0.005, maxiter=1000)

# Plot the data
plt.scatter(data[:,0], data[:,1], c=np.argmax(u, axis=0))
plt.show()

