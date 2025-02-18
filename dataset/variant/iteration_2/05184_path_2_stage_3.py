import numpy as np
import matplotlib.pyplot as plt

# Companies and sectors
companies = ['TechCorp', 'InnovateX', 'FutureSolutions', 'SkyNet', 'QuantumTech']
sectors = ['AI', 'IoT', 'Cloud Computing', 'Cybersecurity', 'Blockchain']

# Revenue data (in billion USD) for each sector in the companies across the years 2019-2022
revenues = np.array([
    [15, 20, 25, 30, 22],
    [10, 15, 20, 18, 16],
    [25, 28, 30, 35, 40],
    [8, 10, 12, 15, 13],
    [5, 7, 9, 11, 6]
])

# Colors for each sector, shuffled
colors = ['#FF6347', '#32CD32', '#9370DB', '#4682B4', '#FFD700']  # Random shuffled colors

# Set up positions and bar width
x = np.arange(len(companies))
bar_width = 0.15

# Generate bar positions for each year
positions = [x - 2*bar_width, x - bar_width, x, x + bar_width, x + 2*bar_width]

# Setup the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Create bars for each year with varied styles and markers
patterns = ['/', '\\', '|', '-', '+']  # Different bar patterns
for i, (pos, sector, color) in enumerate(zip(positions, sectors, colors)):
    ax.bar(pos, revenues[i], bar_width, label=sector, color=color, hatch=patterns[i])

# Adding grid lines
ax.yaxis.grid(True, linestyle='--', linewidth=0.7, which='both', color='gray')

# Labeling and titling
ax.set_xlabel('Companies', fontsize=14)
ax.set_ylabel('Revenue (in Billion USD)', fontsize=14)
ax.set_title('Revenue Growth in Tech Sectors for Leading Companies (2019-2022)', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(companies)
ax.legend(title='Sectors', fontsize=12, frameon=False)

# Custom border
ax.spines['top'].set_linewidth(1.5)
ax.spines['right'].set_linewidth(1.5)
ax.spines['bottom'].set_linewidth(1.5)
ax.spines['left'].set_linewidth(1.5)

plt.tight_layout()
plt.show()