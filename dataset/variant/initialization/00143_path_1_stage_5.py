import numpy as np
import matplotlib.pyplot as plt

# Define the data
fantasy = np.array([20, 25, 30, 45, 65, 80, 95, 110, 130, 145, 160])
mystery = np.array([30, 35, 40, 45, 50, 55, 65, 70, 75, 85, 90])
science_fiction = np.array([15, 20, 28, 35, 45, 55, 70, 85, 100, 115, 130])
romance = np.array([25, 30, 35, 40, 45, 50, 60, 70, 80, 85, 95])
non_fiction = np.array([10, 15, 20, 25, 30, 40, 50, 55, 60, 65, 70])
thriller = np.array([12, 18, 25, 35, 48, 60, 75, 90, 105, 125, 140])
historical = np.array([5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 80])

genre_data = [fantasy, mystery, science_fiction, romance, non_fiction, thriller, historical]

labels = ['Fantasy', 'Mystery', 'Sci-Fi', 'Romance', 'Non-Fiction', 'Thriller', 'Historical']

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 9))

# Plot a horizontal box plot with a single color for all boxes
ax.boxplot(genre_data, vert=False, patch_artist=True, labels=labels,
           boxprops=dict(facecolor='lightblue'))

ax.set_xlabel('Sales')

plt.tight_layout()
plt.show()