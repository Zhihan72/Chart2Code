import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America']
sectors = ['Wildlife Protection', 'Forest Conservation', 'Ocean Cleanup', 'Renewable Energy']

contributions = np.array([
    [320, 220, 180, 370],
    [270, 310, 150, 420],
    [410, 260, 200, 310],
    [160, 110, 100, 110],
    [190, 160, 110, 160]
])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']

bottom = np.zeros(len(regions))
marker_styles = ['o', '^', 's', 'D']  # Different marker styles added
for i, sector in enumerate(sectors):
    ax.bar(regions, contributions[:, i], label=sector, color=colors[i], alpha=0.85, bottom=bottom, hatch=marker_styles[i])
    bottom += contributions[:, i]

ax.set_ylabel('Contributions (in million $)', fontsize=12, fontweight='bold')
ax.set_xlabel('Regions', fontsize=12, fontweight='bold')
ax.set_title('Annual Contributions to Conservation Efforts\nby Region & Sector', fontsize=14, fontweight='bold', pad=15)

ax.legend(title='Conservation Sectors', loc='upper right', bbox_to_anchor=(1, 0.5), fontsize=10)  # Changed legend position

# Customize tick labels
ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels(regions, rotation=30, ha='right', fontsize=10)  # Changed rotation angle

# Adding a different grid style
ax.yaxis.grid(True, linestyle='-.', alpha=0.5)  # Changed grid style and transparency

# Remove top and right borders
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()