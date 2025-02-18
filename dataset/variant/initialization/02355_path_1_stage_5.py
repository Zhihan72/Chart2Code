import matplotlib.pyplot as plt
import numpy as np

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
for i in range(len(sectors)):
    ax.bar(x, negative_contributions[:, i], color=colors[i], alpha=0.65, hatch='//')
    ax.bar(x, positive_contributions[:, i], color=colors[i], alpha=0.85, hatch='')

ax.axhline(0, color='black', linewidth=1)

ax.set_xticks(x)
ax.set_xticklabels([])  # Removed text labels for x-axis

ax.yaxis.grid(True, linestyle='-.', alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()