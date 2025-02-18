import matplotlib.pyplot as plt
import numpy as np

# Altered temperature data for a 10x10 grid representing the city
temperature_data = np.array([
    [33, 26, 20, 24, 31, 22, 33, 30, 28, 27],
    [28, 32, 31, 17, 30, 27, 26, 29, 25, 21],
    [19, 22, 25, 32, 18, 24, 31, 30, 26, 29],
    [33, 29, 31, 32, 28, 25, 23, 26, 20, 30],
    [28, 32, 21, 25, 34, 27, 31, 23, 22, 28],
    [29, 30, 22, 34, 31, 24, 19, 26, 33, 21],
    [23, 31, 34, 35, 33, 28, 20, 18, 24, 32],
    [30, 27, 26, 29, 30, 31, 32, 25, 34, 31],
    [31, 24, 25, 23, 22, 30, 27, 32, 33, 32],
    [19, 20, 29, 24, 28, 31, 21, 33, 30, 31],
])

fig, ax = plt.subplots(figsize=(10, 8))
cax = ax.imshow(temperature_data, cmap='hot', interpolation='nearest', aspect='auto')
cbar = fig.colorbar(cax, ax=ax, orientation='vertical')
cbar.set_label('Temperature (°C)', rotation=270, labelpad=20)

ax.set_xlabel('Neighborhoods (East to West)', fontsize=12)
ax.set_ylabel('Neighborhoods (North to South)', fontsize=12)
ax.set_xticks(range(10))
ax.set_yticks(range(10))
ax.set_xticklabels([f'E{i+1}' for i in range(10)], rotation=45, ha='right', fontsize=10)
ax.set_yticklabels([f'N{i+1}' for i in range(10)], fontsize=10)
ax.set_title('Urban Heat Map of Metropolis:\nAnalyzing Urban Heat Islands', fontsize=14, pad=20)

annotations = {
    (4, 5): 'CBD',
    (7, 7): 'Old Town',
    (2, 4): 'Riverside'
}

for (i, j), text in annotations.items():
    ax.text(j, i, text, ha='center', va='center', color='blue', fontsize=9, fontweight='bold',
            bbox=dict(facecolor='white', alpha=0.7, edgecolor='blue'))

ax.grid(False)
plt.tight_layout()
plt.show()