import matplotlib.pyplot as plt
import numpy as np

# Data
distances = np.array([225, 628, 1221, 1070, 1182, 77, 42])
population_capacity = np.array([10, 5, 15, 8, 7, 3, 12])

# Remove one data group
distances = distances[:-1]
population_capacity = population_capacity[:-1]

# Sort data in descending order
sorted_indices = np.argsort(-distances)
sorted_distances = distances[sorted_indices]
sorted_population_capacity = population_capacity[sorted_indices]

# Create bar chart with stylistic changes
fig, ax = plt.subplots(figsize=(14, 9))
bar = ax.bar(np.arange(len(sorted_distances)), sorted_distances, 
             color=['skyblue', 'salmon', 'yellowgreen', 'cornflowerblue', 'lightcoral', 'burlywood'], 
             edgecolor='black', linestyle='--')

# Annotate bar chart with population capacity
for rect, label in zip(bar, sorted_population_capacity):
    height = rect.get_height()
    ax.text(rect.get_x() + rect.get_width()/2, height, f'{label}',
            ha='center', va='bottom', fontsize=12, style='italic')

# Add grid with only horizontal lines
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, color='gray')
ax.xaxis.grid(False)

plt.xticks(np.arange(len(sorted_distances)), ['D'+str(i) for i in sorted_indices], rotation=45)
plt.xlabel('Data Points', fontsize=14, fontweight='bold', color='darkblue')
plt.ylabel('Distances', fontsize=14, fontweight='bold', color='darkgreen')
plt.title('Sorted Bar Chart of Distances', fontsize=16, fontweight='bold', color='darkred')

# Add a legend
ax.legend(['Distances'], loc='upper right', fontsize=12)

# Remove borders to some extent
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)

plt.tight_layout()
plt.show()