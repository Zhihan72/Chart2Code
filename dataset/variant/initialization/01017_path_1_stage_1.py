import matplotlib.pyplot as plt

avalon = [30, 45, 40, 38, 60, 72, 55, 48, 63, 35]
camelot = [50, 65, 62, 58, 80, 95, 82, 75, 78, 67]
winterfell = [20, 25, 22, 30, 18, 35, 25, 28, 33, 27]
gondor = [45, 50, 55, 52, 48, 65, 60, 58, 53, 47]

data = [avalon, camelot, winterfell, gondor]

kingdoms = ['Avalon', 'Camelot', 'Winterfell', 'Gondor']

fig, ax = plt.subplots(figsize=(10, 6))

bp = ax.boxplot(data, patch_artist=True, notch=True, vert=False, labels=kingdoms, widths=0.6)

colors = ['#d6a0f6', '#9fc5e8', '#ffe599', '#f9cb9c']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for whisker in bp['whiskers']:
    whisker.set(color='black', linewidth=1.5, linestyle="--")
for cap in bp['caps']:
    cap.set(color='black', linewidth=1.5)
for median in bp['medians']:
    median.set(color='darkblue', linewidth=2)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)
ax.set_title('Quest Durations of Medieval Knights\nAcross Different Kingdoms', fontsize=14)
ax.set_ylabel('Kingdoms', fontsize=12)
ax.set_xlabel('Quest Duration (Days)', fontsize=12)

plt.tight_layout()
plt.show()