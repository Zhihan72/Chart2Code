import matplotlib.pyplot as plt

energy_sources = ['Solar', 'Wind', 'Hydro', 'Bio', 'Geo']
efficiency_data = [
    [90, 75, 78, 80, 82, 93, 95, 77, 88, 85],
    [68, 70, 75, 66, 60, 69, 71, 73, 72, 74],
    [84, 85, 92, 87, 91, 89, 86, 88, 90, 85],
    [63, 56, 62, 60, 57, 58, 61, 55, 64, 59],
    [75, 72, 71, 73, 76, 80, 78, 70, 77, 74],
]

fig, ax = plt.subplots(figsize=(14, 8))

bp = ax.boxplot(efficiency_data, vert=False, patch_artist=True, notch=True, showmeans=True,
                meanline=True, meanprops=dict(linestyle='-', linewidth=2.5, color='blue'))

colors = ['#C70039', '#FFC300', '#581845', '#FF5733', '#900C3F']
for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color, alpha=0.6)

for whisker in bp['whiskers']:
    whisker.set(color='#2C3E50', linewidth=2, linestyle="--")

for cap in bp['caps']:
    cap.set(color='#2C3E50', linewidth=2)

for median in bp['medians']:
    median.set(color='green', linewidth=3)

ax.set_xlabel('Score (%)', fontsize=13)
ax.set_yticklabels(energy_sources, fontsize=12)

ax.set_xlim(50, 100)

plt.tight_layout()
plt.show()