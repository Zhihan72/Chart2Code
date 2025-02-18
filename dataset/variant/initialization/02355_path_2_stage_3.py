import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America']
sectors = ['Wildlife Protection', 'Forest Conservation', 'Ocean Cleanup', 'Renewable Energy']

contributions = np.array([
    [320, -220, 180, -370],  # North America
    [-270, 310, -150, 420],  # Europe
    [410, -260, 200, -310],  # Asia
    [-160, 110, -100, 110],  # Africa
    [190, -160, 110, -160]   # South America
])

fig, ax = plt.subplots(figsize=(12, 8))

# Manually shuffled colors
colors = ['#99FF99', '#FFCC99', '#FF9999', '#66B3FF']

cumulative_positive = np.where(contributions > 0, contributions, 0).cumsum(axis=1)
cumulative_negative = np.where(contributions < 0, contributions, 0).cumsum(axis=1)

for i, sector in enumerate(sectors):
    ax.bar(regions, contributions[:, i],
           color=colors[i], alpha=0.85,
           bottom=cumulative_negative[:, i] if contributions[:, i][0] < 0 else 
           cumulative_positive[:, i] - contributions[:, i])

ax.set_ylabel('Contributions (in million $)', fontsize=12, fontweight='bold')
ax.set_xlabel('Regions', fontsize=12, fontweight='bold')
ax.set_title('Diverging Contributions to Global Conservation Efforts\nby Region and Sector',
             fontsize=14, fontweight='bold', pad=15)

ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels(regions, rotation=45, ha='right', fontsize=10)

plt.tight_layout()

plt.show()