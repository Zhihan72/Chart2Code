import matplotlib.pyplot as plt
import numpy as np

# Transpose the matrix to align with the horizontal bar chart's requirements
influence_matrix = np.array([
    [7, 5, 3, 4, 6],
    [6, 8, 2, 5, 7],
    [4, 7, 5, 3, 6],
    [3, 4, 9, 8, 5],
    [5, 6, 4, 7, 8],
    [6, 5, 7, 3, 9],
    [8, 3, 6, 9, 4],
])

# Calculate the mean of each row to represent in the bar chart
mean_values = influence_matrix.mean(axis=1)
categories = [f'Category {i+1}' for i in range(influence_matrix.shape[0])]

fig, ax = plt.subplots(figsize=(10, 8))

# Plot the horizontal bar chart 
ax.barh(categories, mean_values,)

ax.set_xlabel('Mean Influence')
ax.set_ylabel('Categories')
ax.set_title('Mean Influence per Category')

plt.tight_layout()
plt.show()