import matplotlib.pyplot as plt

neighborhoods = ['Green', 'Sunny', 'Hill']
volunteering_hours = [
    [2, 4, 6, 8, 12, 14, 16, 18, 20, 25],  # Greenfield
    [3, 5, 7, 10, 11, 13, 15, 17, 21, 23], # Sunnydale
    [2, 4, 9, 11, 12, 15, 17, 18, 19, 22]  # Hillcrest
]

fig, ax = plt.subplots(figsize=(14, 8))
bp = ax.boxplot(volunteering_hours, vert=False, patch_artist=True, notch=True,
                meanline=True, showmeans=True, meanprops=dict(linestyle='-', linewidth=2, color='darkorange'))

colors = ['#FF9999', '#99FF99', '#FFCC99']
for patch, color in zip(bp['boxes'], colors):
    patch.set(facecolor=color, alpha=0.7)

for whisker in bp['whiskers']:
    whisker.set(color='gray', linewidth=1.5, linestyle="--")

for cap in bp['caps']:
    cap.set(color='gray', linewidth=1.5)

for median in bp['medians']:
    median.set(color='blue', linewidth=2)

for mean in bp['means']:
    mean.set(marker='o', markerfacecolor='darkorange', markersize=8)

ax.set_title('Volunteer Hours by Area', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Hours', fontsize=13)
ax.set_yticklabels(neighborhoods, fontsize=12)

ax.xaxis.grid(True, linestyle='--', alpha=0.7)

mean_legend = plt.Line2D([], [], color='darkorange', marker='o', linestyle='None', markersize=8, label='Mean')
median_legend = plt.Line2D([], [], color='blue', linestyle='-', linewidth=2, label='Median')
ax.legend(handles=[mean_legend, median_legend], loc='lower right')

plt.tight_layout()
plt.show()