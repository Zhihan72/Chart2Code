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

# New color palette
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']

bottom = np.zeros(len(regions))
marker_styles = ['o', '^', 's', 'D']
for i, sector in enumerate(sectors):
    ax.bar(regions, contributions[:, i], label=sector, color=colors[i], alpha=0.85, bottom=bottom, hatch=marker_styles[i])
    bottom += contributions[:, i]

ax.set_ylabel('Contributions (in million $)', fontsize=12, fontweight='bold')
ax.set_xlabel('Regions', fontsize=12, fontweight='bold')
ax.set_title('Annual Contributions to Conservation Efforts\nby Region & Sector', fontsize=14, fontweight='bold', pad=15)

ax.legend(title='Conservation Sectors', loc='upper right', bbox_to_anchor=(1, 0.5), fontsize=10)

ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels(regions, rotation=30, ha='right', fontsize=10)

ax.yaxis.grid(True, linestyle='-.', alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()