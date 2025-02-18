import matplotlib.pyplot as plt
import numpy as np

# Data for renewable energy generation
energy_data = np.array([
    [200, 150, 100, 50],  # Europe
    [300, 200, 250, 30],  # Asia
    [250, 220, 180, 40],  # North America
    [120, 100, 300, 20],  # South America
    [180, 90, 70, 10]     # Africa
])

regions = ['Europe', 'Asia', 'North America', 'South America', 'Africa']
categories = ['Solar', 'Wind', 'Hydro', 'Biomass']

fig, ax = plt.subplots(figsize=(12, 8))

# Define bar colors
colors = ['#ffcc99', '#99ff99', '#66b3ff', '#ff6666']

# Calculate the negative and positive positions
neg_positions = -np.cumsum(energy_data[:, :2], axis=1)
pos_positions = np.cumsum(energy_data[:, 2:], axis=1)

bar_width = 0.4

# Create diverging bar chart
for i, color in enumerate(colors[:2]):
    ax.barh(regions, energy_data[:, i], color=color, edgecolor='black', height=bar_width, left=neg_positions[:, i])

for i, color in enumerate(colors[2:], start=2):
    ax.barh(regions, energy_data[:, i], color=color, edgecolor='black', height=bar_width, left=pos_positions[:, i-2]-energy_data[:, i])
    
# Set grid, labels, and title
ax.set_yticks(np.arange(len(regions)))
ax.set_yticklabels(regions)
ax.axvline(0, color='black', linewidth=0.8)
ax.set_xlabel('Energy Generation (GWh)')
ax.set_title('Diverging Bar Chart of Renewable Energy Generation')

plt.tight_layout()
plt.show()