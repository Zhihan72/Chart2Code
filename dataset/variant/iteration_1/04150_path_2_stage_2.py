import matplotlib.pyplot as plt
import numpy as np

cities = ['City A', 'City B', 'City C', 'City D']

flu_cases_data = {
    'City A': [30, 25, 40, 35, 50, 60, 45, 55, 65, 70, 75, 80],
    'City B': [20, 18, 25, 28, 30, 35, 40, 45, 50, 55, 60, 65],
    'City C': [15, 10, 20, 25, 30, 35, 40, 45, 55, 60, 70, 75],
    'City D': [10, 5, 8, 12, 18, 20, 25, 30, 40, 50, 55, 60]
}

data_for_box = [flu_cases_data[city] for city in cities]

fig, ax = plt.subplots(figsize=(12, 7))

# Apply a single color consistently
color = '#76C7C0'

box = ax.boxplot(data_for_box, patch_artist=True, notch=True, vert=False,
                 boxprops=dict(facecolor=color, color='black'),
                 whiskerprops=dict(color='black'),
                 capprops=dict(color='black'),
                 medianprops=dict(color='red'),
                 flierprops=dict(markerfacecolor=color, marker='o', markersize=5, alpha=0.6))

ax.set_title('Seasonal Flu Cases Distribution\n Across Different Cities (2023)', fontsize=16, fontweight='bold')
ax.set_xlabel('Number of Flu Cases', fontsize=12)
ax.set_ylabel('Cities', fontsize=12)

ax.set_yticks(np.arange(1, len(cities) + 1))
ax.set_yticklabels(cities, fontsize=11)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()