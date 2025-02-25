import numpy as np
import matplotlib.pyplot as plt

# Companies and sectors
companies = ['TechCorp', 'InnovateX', 'FutureSolutions', 'SkyNet', 'QuantumTech']
sectors = ['AI', 'IoT', 'Cloud Computing', 'Cybersecurity', 'Blockchain']

# Revenue data (in billion USD) for each sector in the companies across the years 2019-2022
revenues = np.array([
    [15, 20, 25, 30, 22],  # AI
    [10, 15, 20, 18, 16],  # IoT
    [25, 28, 30, 35, 40],  # Cloud Computing
    [8, 10, 12, 15, 13],   # Cybersecurity
    [5, 7, 9, 11, 6]       # Blockchain
])

# Colors for each sector
colors = ['#32CD32', '#FFD700', '#4682B4', '#FF6347', '#9370DB']  # (Now includes Blockchain)

# Set up positions and bar width
x = np.arange(len(companies))
bar_width = 0.15

# Generate bar positions for each year
positions = [x - 2*bar_width, x - bar_width, x, x + bar_width, x + 2*bar_width]

# Setup the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Create bars for each year
for i, pos, sector, color in zip(range(len(positions)), positions, sectors, colors):
    ax.bar(pos, revenues[i], bar_width, label=sector, color=color)

# Labeling and titling the plot
ax.set_xlabel('Companies', fontsize=14)
ax.set_ylabel('Revenue (in Billion USD)', fontsize=14)
ax.set_title('Revenue Growth in Tech Sectors for Leading Companies (2019-2022)', fontsize=16, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(companies)
ax.legend(title='Sectors', fontsize=12)

# Ensure the layout is tight to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()