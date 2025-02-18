import matplotlib.pyplot as plt
import numpy as np

# Synthetic temperature differences (in Celsius) for a week in different cities
city_A = [-5, -3, 0, 2, 1, -1, -4, 3, 2, 0, -2, -3, 1, 2, -3]
city_B = [0, 3, -1, 4, 3, -2, 0, 3, -1, 2, 3, -1, -2, 1, 2]
city_C = [2, 4, 5, 6, 7, 6, 5, 4, 4, 5, 6, 7, 6, 5, 4]
city_D = [10, 15, 13, 14, 12, 13, 15, 14, 12, 10, 11, 12, 13, 14, 12]
city_E = [-10, -8, -9, -7, -8, -9, -11, -12, -9, -8, -10, -7, -5, -6, -8]
# Additional city
city_F = [5, 6, 7, 8, 9, 8, 7, 6, 5, 6, 7, 8, 9, 8, 7]

data = [city_A, city_B, city_C, city_D, city_E, city_F]
cities = ['City A', 'City B', 'City C', 'City D', 'City E', 'City F']

plt.figure(figsize=(14, 10))

# Create the violin plot
violin = plt.violinplot(data, vert=False, showmeans=False, showmedians=True)

# Add the horizontal boxplot on top of the violin plot
box = plt.boxplot(data, vert=False, patch_artist=True, notch=True, whis=1.5,
                  boxprops=dict(facecolor='white', color='black', alpha=0.7),
                  whiskerprops=dict(color='black'),
                  capprops=dict(color='black'),
                  medianprops=dict(color='red', linewidth=1.5),
                  flierprops=dict(marker='o', color='green', alpha=0.5))

colors = ['#fbb4ae', '#b3cde3', '#ccebc5', '#decbe4', '#fed9a6', '#b3de69']
for patch, color in zip(box['boxes'], colors):
    patch.set_facecolor(color)

# Title and labels
plt.title('Temperature Variability During the Week\nin Different Fictional Cities', fontsize=16, fontweight='bold')
plt.xlabel('Temperature Change (°C)', fontsize=12)
plt.yticks(range(1, len(cities) + 1), cities, fontsize=10)

# Annotate with mean values for additional context
for i, city in enumerate(data):
    mean_val = np.mean(city)
    plt.text(mean_val + 0.2, i + 1, f'Mean: {mean_val:.1f}', verticalalignment='center', fontsize=9, color='darkblue')

# Grid for readability
plt.grid(visible=True, axis='x', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()