import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

streamed_hours = np.array([
    [10, 15, 20, 25, 32, 40, 55, 68, 75, 80, 82],  # Streaming A
    [5, 10, 15, 20, 28, 35, 45, 50, 55, 60, 65],   # Streaming B
    [2, 5, 9, 14, 20, 28, 38, 45, 50, 55, 60],     # Streaming C
    [1, 2, 5, 10, 15, 20, 28, 30, 32, 34, 36],     # Streaming D
    [2, 3, 4, 5, 8, 12, 18, 22, 26, 30, 35],       # Streaming E
    [5, 6, 8, 11, 15, 20, 25, 30, 32, 35, 37]      # Other Platforms
])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#7f7f7f', '#9467bd']

# Create stackplot without stylistic components
ax.stackplot(years, streamed_hours, colors=colors, alpha=0.85)

ax.set_title('The Rise of Streaming:\nEvolution of Digital Streaming Platforms from 2010 to 2020', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Hours Streamed (in billion hours)', fontsize=12)

# Remove the legend
# ax.legend(loc='upper left', fontsize=10, title='Streaming Platforms', bbox_to_anchor=(1, 1))

# Remove the grid
# ax.yaxis.grid(True, linestyle='--', alpha=0.7)

ax.set_xticks(years)

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()