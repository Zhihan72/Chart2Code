import matplotlib.pyplot as plt

ai_growth = [22, 27, 19, 25, 30]
cyber_growth = [12, 18, 15, 22, 17]
fintech_growth = [35, 28, 40, 33, 45]
edtech_growth = [8, 15, 10, 14, 9]
healthtech_growth = [25, 23, 20, 26, 27]
agritech_growth = [15, 20, 18, 23, 21]  # New data series
cleantech_growth = [30, 34, 32, 33, 31]  # New data series

growth_data = [
    ai_growth, cyber_growth, fintech_growth, edtech_growth, 
    healthtech_growth, agritech_growth, cleantech_growth
]

fig, ax = plt.subplots(figsize=(12, 8))

ax.boxplot(growth_data, vert=False, notch=True, patch_artist=True,
           boxprops=dict(facecolor='lightgreen', color='lightgreen'),
           whiskerprops=dict(color='lightgreen'),
           capprops=dict(color='lightgreen'),
           medianprops=dict(color='lightgreen', linewidth=2),
           flierprops=dict(marker='o', color='lightgreen', markersize=8, alpha=0.5))

ax.set_xticklabels([])
ax.set_yticklabels([])

plt.yticks([])
plt.xticks([])
plt.tight_layout()

plt.show()