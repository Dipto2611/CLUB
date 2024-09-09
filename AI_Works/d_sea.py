# import seaborn as sns
# import matplotlib.pyplot as plt

# # Create a 3x3 matrix of random numbers
# data = np.random.rand(3, 3)

# # Create a heatmap using Seaborn
# sns.heatmap(data, annot=True)
# plt.title("Seaborn Heatmap")
# plt.show()

import numpy as np  # Make sure to import NumPy
import seaborn as sns
import matplotlib.pyplot as plt

# Create a 3x3 matrix of random numbers
data = np.random.rand(3, 3)

# Create a heatmap using Seaborn
sns.heatmap(data, annot=True)
plt.title("Seaborn Heatmap")
plt.show()
