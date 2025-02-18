import matplotlib.pyplot as plt
import numpy as np

# Expanded regions and sectors
regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America', 'Oceania']
sectors = ['Wildlife Protection', 'Forest Conservation', 'Ocean Cleanup', 'Renewable Energy', 'Pollution Control']

contributions = np.array([
    [320, 220, 180, 370, 120],
    [270, 310, 150, 420, 210],
    [410, 260, 200, 310, 250],
    [160, 110, 100, 110, 80],
    [190, 160, 110, 160, 100],
    [150, 130, 90, 140, 60]
])

# Setting up hypothetical "positive" and "negative" contributions 
positive_contributions = np.array([
    [160, 110, 90, 185, 60],
    [135, 155, 75, 210, 105],
    [205, 130, 100, 155, 125],
    [80, 55, 50, 55, 40],
    [95, 80, 55, 80, 50],
    [75, 65, 45, 70, 30]
])

negative_contributions = positive_contributions - contributions

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6', '#FFD700']

x = np.arange(len(regions))
# Plot negative contributions on the left
for i, sector in enumerate(sectors):
    ax.bar(x, negative_contributions[:, i], label=f'{sector} (negative)', color=colors[i], alpha=0.65, hatch='//')
    
# Plot positive contributions on the right
for i, sector in enumerate(sectors):
    ax.bar(x, positive_contributions[:, i], label=f'{sector} (positive)', color=colors[i], alpha=0.85, hatch='')

ax.set_ylabel('Contributions (in million $)', fontsize=12, fontweight='bold')
ax.set_xlabel('Regions', fontsize=12, fontweight='bold')
ax.set_title('Diverging Contributions to Conservation Efforts\nby Region & Sector', fontsize=14, fontweight='bold', pad=15)

ax.axhline(0, color='black', linewidth=1)

ax.legend(title='Conservation Sectors', loc='upper right', bbox_to_anchor=(1.15, 1), fontsize=10)

ax.set_xticks(x)
ax.set_xticklabels(regions, rotation=30, ha='right', fontsize=10)

ax.yaxis.grid(True, linestyle='-.', alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()