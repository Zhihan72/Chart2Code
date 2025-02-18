import matplotlib.pyplot as plt
import numpy as np

species = ['Oak Shrubs', 'Pine Shrubs', 'Maple Shrubs', 'Deer Cluster', 'Bird Cluster', 'Flower Meadow', 'River Cluster']

years = np.array([2020, 2021, 2022, 2023, 2024])

oak_growth = np.array([100, 120, 140, 160, 180])
pine_growth = np.array([90, 105, 130, 150, 170])
maple_growth = np.array([80, 95, 115, 135, 155])
deer_growth = np.array([50, 60, 70, 85, 95])
bird_growth = np.array([200, 220, 260, 300, 340])
flower_growth = np.array([30, 45, 55, 70, 90])  # New data
river_growth = np.array([25, 50, 60, 80, 100])  # New data

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, oak_growth, marker='p', linestyle='-', color='#FFA500', linewidth=3, label='Oak Shrubs')
ax.plot(years, pine_growth, marker='x', linestyle=':', color='#00FF00', linewidth=2, label='Pine Shrubs')
ax.plot(years, maple_growth, marker='h', linestyle='--', color='#FF4500', linewidth=2, label='Maple Shrubs')
ax.plot(years, deer_growth, marker='v', linestyle='-.', color='#1E90FF', linewidth=2.5, label='Deer Cluster')
ax.plot(years, bird_growth, marker='x', linestyle='-', color='#8A2BE2', linewidth=1.5, label='Bird Cluster')
ax.plot(years, flower_growth, marker='o', linestyle='-', color='#32CD32', linewidth=1.5, label='Flower Meadow') # New series
ax.plot(years, river_growth, marker='s', linestyle='--', color='#4682B4', linewidth=2, label='River Cluster')    # New series

ax.set_title('Natural System: Yearly Rise Metrics (2020-2024)', fontsize=16)
ax.set_xlabel('Time Frame', fontsize=12)
ax.set_ylabel('Rate of Growth (Randomized Units)', fontsize=12)

ax.grid(True, linestyle='-', linewidth=0.75, alpha=0.5)

ax.legend(title='Habitat', fontsize=10, title_fontsize='13', loc='lower right', frameon=False)

for growth, label, color in zip([oak_growth, pine_growth, maple_growth, deer_growth, bird_growth, flower_growth, river_growth], 
                                ['Oak Shrubs', 'Pine Shrubs', 'Maple Shrubs', 'Deer Cluster', 'Bird Cluster', 'Flower Meadow', 'River Cluster'], 
                                ['#FFA500', '#00FF00', '#FF4500', '#1E90FF', '#8A2BE2', '#32CD32', '#4682B4']):
    ax.annotate(f'{growth[-1]}',
                xy=(years[-1], growth[-1]),
                xytext=(-10, 5),
                textcoords='offset points',
                fontsize=10,
                color=color,
                arrowprops=dict(arrowstyle='->', lw=1))

plt.tight_layout()
plt.show()