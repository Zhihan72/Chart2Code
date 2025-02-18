import matplotlib.pyplot as plt

sectors = ['Artificial Intelligence', 'Cybersecurity', 'Fintech', 'EdTech', 'HealthTech']

ai_growth = [22, 27, 19, 25, 30]
cyber_growth = [12, 18, 15, 22, 17]
fintech_growth = [35, 28, 40, 33, 45]
edtech_growth = [8, 15, 10, 14, 9]
healthtech_growth = [25, 23, 20, 26, 27]

growth_data = [ai_growth, cyber_growth, fintech_growth, edtech_growth, healthtech_growth]

fig, ax = plt.subplots(figsize=(12, 8))

ax.boxplot(growth_data, vert=False, notch=True, patch_artist=True,
           labels=sectors,
           boxprops=dict(facecolor='lightgreen', color='lightgreen'),
           whiskerprops=dict(color='lightgreen'),
           capprops=dict(color='lightgreen'),
           medianprops=dict(color='lightgreen', linewidth=2),
           flierprops=dict(marker='o', color='lightgreen', markersize=8, alpha=0.5))

plt.yticks(rotation=15)
plt.tight_layout()

plt.show()