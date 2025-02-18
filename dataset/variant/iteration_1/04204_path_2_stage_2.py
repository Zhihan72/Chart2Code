import matplotlib.pyplot as plt
import numpy as np

# Data for Vitamin C content in mg per 100 grams for each fruit type
oranges = [53.2, 50.5, 52.4, 55.0, 54.3, 51.7, 52.8, 49.9, 54.1, 53.0]
strawberries = [58.8, 59.4, 60.1, 57.5, 59.6, 58.0, 60.3, 61.2, 57.9, 59.8]
kiwis = [92.7, 93.0, 89.6, 95.4, 94.2, 91.1, 92.6, 90.8, 93.3, 92.0]
lemons = [77.0, 76.4, 78.2, 75.8, 77.7, 78.9, 76.1, 77.4, 75.6, 77.9]
pineapples = [47.8, 48.2, 47.0, 49.3, 46.6, 47.4, 48.7, 47.5, 48.0, 48.8]

# Combine the data into a single list for the boxplot
data = [oranges, strawberries, kiwis, lemons, pineapples]
fruit_labels = ['Oranges', 'Strawberries', 'Kiwis', 'Lemons', 'Pineapples']

# Create the plot
fig, ax = plt.subplots(figsize=(10, 8))

# Create the box plot without stylistic elements
ax.boxplot(data, vert=True, patch_artist=True, labels=fruit_labels, notch=True,
           boxprops=dict(facecolor='#c6dbef', color='none'),
           whiskerprops=dict(color='#084594'),
           capprops=dict(color='#084594'),
           medianprops=dict(color='#ef3b2c'),
           flierprops=dict(marker='o', color='#ef3b2c', alpha=0.5))

# Set the labels without grid
ax.set_xlabel("Types of Fruits", fontsize=12)
ax.set_ylabel("Vitamin C Content (mg)", fontsize=12)

# Remove border and spines
for spine in ax.spines.values():
    spine.set_visible(False)

# Automatically adjust layout for better fit and visibility
plt.tight_layout()

# Display the plot
plt.show()