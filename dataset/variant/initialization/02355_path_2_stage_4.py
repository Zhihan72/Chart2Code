import matplotlib.pyplot as plt
import numpy as np

regions = ['North America', 'Europe', 'Asia', 'Africa', 'South America']
sectors = ['Wildlife Protection', 'Forest Conservation', 'Ocean Cleanup', 'Renewable Energy']

contributions = np.array([
    [320, -220, 180, -370],
    [-270, 310, -150, 420],
    [410, -260, 200, -310],
    [-160, 110, -100, 110],
    [190, -160, 110, -160]
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

# Removed axis labels and title
ax.set_xticks(np.arange(len(regions)))
ax.set_xticklabels([])  # Removed group labels

plt.tight_layout()

plt.show()