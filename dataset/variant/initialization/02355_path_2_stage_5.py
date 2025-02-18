import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America']
sectors = ['Wildlife Protection', 'Forest Conservation', 'Ocean Cleanup', 'Renewable Energy']

# Altering some values in the contributions array while keeping its shape
contributions = np.array([
    [150, -220, 130, -250],
    [-180, 245, -140, 360],
    [350, -220, 210, -280],
    [-100, 130, -90, 60],
    [210, -130, 180, -140]
])

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#99FF99', '#FFCC99', '#FF9999', '#66B3FF']

cumulative_positive = np.where(contributions > 0, contributions, 0).cumsum(axis=1)
cumulative_negative = np.where(contributions < 0, contributions, 0).cumsum(axis=1)

for i, sector in enumerate(sectors):
    ax.bar(regions, contributions[:, i],
           color=colors[i], alpha=0.85,
           bottom=cumulative_negative[:, i] if contributions[:, i][0] < 0 else 
           cumulative_positive[:, i] - contributions[:, i])

ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels([])

plt.tight_layout()

plt.show()