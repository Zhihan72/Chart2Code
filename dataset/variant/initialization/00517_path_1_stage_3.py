import matplotlib.pyplot as plt
import numpy as np

continents = ['Europe', 'Asia', 'North America', 'South America']
sources = ['Solar', 'Wind', 'Hydro']

energy_data = np.array([
    [200, 150, 100],
    [300, 200, 250],
    [250, 220, 180],
    [120, 100, 300]
])

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Define bar width and positions
bar_width = 0.2
x_indices = np.arange(len(continents))

# Plot each energy source data as a separate group
for i, source in enumerate(sources):
    ax.bar(x_indices + i * bar_width, energy_data[:, i], bar_width, label=source)

# Labeling the axes and title
ax.set_xlabel('Continents', fontsize=12)
ax.set_ylabel('Energy Generation (GW)', fontsize=12)
ax.set_title('2030 Renewable Energy Generation Across Continents', fontsize=16, fontweight='bold', pad=20)

# Set x-ticks and labels
ax.set_xticks(x_indices + bar_width)
ax.set_xticklabels(continents, rotation=30, ha='right')

# Legend
ax.legend(title='Energy Sources', loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()