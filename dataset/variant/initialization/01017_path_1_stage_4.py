import matplotlib.pyplot as plt

avalon = [30, 45, 40, 38, 60, 72, 55, 48, 63, 35]
camelot = [50, 65, 62, 58, 80, 95, 82, 75, 78, 67]
winterfell = [20, 25, 22, 30, 18, 35, 25, 28, 33, 27]
gondor = [45, 50, 55, 52, 48, 65, 60, 58, 53, 47]

data = [avalon, camelot, winterfell, gondor]
kingdoms = ['Gondor', 'Winterfell', 'Camelot', 'Avalon']

fig, ax = plt.subplots(figsize=(10, 6))

bp = ax.boxplot(data, patch_artist=True, notch=True, vert=False, labels=kingdoms, widths=0.6)

# New color scheme
colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']
for patch, color in zip(bp['boxes'], colors):
    patch.set_facecolor(color)

for whisker in bp['whiskers']:
    whisker.set(color='purple', linewidth=2.0, linestyle='-.')

for cap in bp['caps']:
    cap.set(color='red', linewidth=2.0)

for median in bp['medians']:
    median.set(color='green', linewidth=3)

ax.yaxis.grid(True, linestyle='-', alpha=0.5)
ax.set_title('Duration of Quests in Mythical Lands', fontsize=16, fontweight='bold')
ax.set_ylabel('Realm Names', fontsize=13, fontstyle='italic')
ax.set_xlabel('Time Taken (Days)', fontsize=13, color='gray')

ax.legend(['Gondor Legend', 'Winterfell Legend', 'Camelot Legend', 'Avalon Legend'], loc='upper right', fontsize=10, frameon=False)

plt.tight_layout()
plt.show()