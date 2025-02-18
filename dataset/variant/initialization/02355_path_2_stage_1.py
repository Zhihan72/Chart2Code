import matplotlib.pyplot as plt
import numpy as np

# Regions and conservation sectors
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America']
sectors = ['Wildlife Protection', 'Forest Conservation', 'Ocean Cleanup', 'Renewable Energy']

# Simulate diverging contributions from a central baseline
contributions = np.array([
    [320, -220, 180, -370],  # North America
    [-270, 310, -150, 420],  # Europe
    [410, -260, 200, -310],  # Asia
    [-160, 110, -100, 110],  # Africa
    [190, -160, 110, -160]   # South America
])

fig, ax = plt.subplots(figsize=(12, 8))

# Colors for each conservation sector
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

# Calculate cumulative values for stacking
cumulative_positive = np.where(contributions > 0, contributions, 0).cumsum(axis=1)
cumulative_negative = np.where(contributions < 0, contributions, 0).cumsum(axis=1)

# Plot each sector with positive and negative divergence
for i, sector in enumerate(sectors):
    ax.bar(regions, contributions[:, i],
           label=sector, color=colors[i], alpha=0.85,
           bottom=cumulative_negative[:, i] if contributions[:, i][0] < 0 else 
           cumulative_positive[:, i] - contributions[:, i])

# Adding labels and title
ax.set_ylabel('Contributions (in million $)', fontsize=12, fontweight='bold')
ax.set_xlabel('Regions', fontsize=12, fontweight='bold')
ax.set_title('Diverging Contributions to Global Conservation Efforts\nby Region and Sector',
             fontsize=14, fontweight='bold', pad=15)

# Adding legend
ax.legend(title='Conservation Sectors', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

# Customize tick labels
ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)

# Adding a grid
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()