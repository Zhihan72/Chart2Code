import matplotlib.pyplot as plt
import numpy as np

# Data
distances = np.array([225, 628, 1221, 1070, 1182, 77, 42])
population_capacity = np.array([10, 5, 15, 8, 7, 3, 12])

# Remove one data group
# Let's decide to remove the data point corresponding to the shortest distance for simplification
distances = distances[:-1]
population_capacity = population_capacity[:-1]

# Sort data in descending order
sorted_indices = np.argsort(-distances)
sorted_distances = distances[sorted_indices]
sorted_population_capacity = population_capacity[sorted_indices]

# Create bar chart
fig, ax = plt.subplots(figsize=(14, 9))
bar = ax.bar(np.arange(len(sorted_distances)), sorted_distances, 
             color='skyblue', edgecolor='gray')

# Annotate bar chart with population capacity
for rect, label in zip(bar, sorted_population_capacity):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, height, f'{label}',
            ha='center', va='bottom')

plt.xticks(np.arange(len(sorted_distances)), ['D'+str(i) for i in sorted_indices])
plt.xlabel('Data Points')
plt.ylabel('Distances')
plt.title('Sorted Bar Chart of Distances')

plt.tight_layout()
plt.show()