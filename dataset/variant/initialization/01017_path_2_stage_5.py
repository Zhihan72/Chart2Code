import matplotlib.pyplot as plt

avalon = [30, 45, 40, 38, 60, 72, 55, 48, 63, 35]
camelot = [50, 65, 62, 58, 80, 95, 82, 75, 78, 67]
gondor = [45, 50, 55, 52, 48, 65, 60, 58, 53, 47]

data = [avalon, camelot, gondor]
kingdoms = ['Gondor', 'Avalon', 'Camelot']

fig, ax = plt.subplots(figsize=(10, 6))

bp = ax.boxplot(data, patch_artist=True, notch=True, vert=False, labels=kingdoms, widths=0.6)

new_colors = ['#ff9999', '#66b3ff', '#99ff99']
for patch, color in zip(bp['boxes'], new_colors):
    patch.set_facecolor(color)

for whisker in bp['whiskers']:
    whisker.set(color='black', linewidth=1.5, linestyle="--")
for cap in bp['caps']:
    cap.set(color='black', linewidth=1.5)
for median in bp['medians']:
    median.set(color='darkblue', linewidth=2)

# Remove the grid
# ax.xaxis.grid(True, linestyle='--', alpha=0.7)

ax.set_xlabel('Days on Quest', fontsize=12)
ax.set_ylabel('Regions', fontsize=12)

# Remove the title
# ax.set_title('Duration of Quests in the Middle Ages\nPer Kingdom', fontsize=14)

plt.tight_layout()
plt.show()