import matplotlib.pyplot as plt

# Altered screen time data preserving the original structure
screen_time_data = [
    [125, 105, 110, 150, 140, 130, 145, 100, 115, 120],  # 6-12
    [230, 190, 240, 180, 250, 210, 235, 225, 220, 200],  # 13-18
    [210, 220, 205, 220, 195, 180, 200, 210, 175, 215],  # 19-25
    [175, 180, 160, 185, 160, 190, 150, 160, 175, 170],  # 26-40
    [100, 95, 85, 80, 110, 90, 105, 95, 100, 90],        # 41-60
    [65, 60, 75, 55, 50, 80, 60, 70, 55, 70]             # 60+
]

fig, ax = plt.subplots(figsize=(14, 8))

box = ax.boxplot(screen_time_data, vert=True, patch_artist=True, flierprops=dict(marker='x', color='red'))

colors = ['#da70d6', '#32cd32', '#ffa07a', '#ffebcd', '#7b68ee', '#ff7f50']
for patch, color in zip(box['boxes'], colors):
    patch.set(facecolor=color, linestyle=':', linewidth=2)

ax.legend(['6-12', '13-18', '19-25', '26-40', '41-60', '60+'], loc='upper right', fontsize=12)
ax.set_title('Monthly Screen Time by Age', fontsize=18, pad=15)
ax.set_ylabel('Hours/Month', fontsize=14)
ax.set_xticklabels(['6-12', '13-18', '19-25', '26-40', '41-60', '60+'], fontsize=12)
ax.set_xlabel('Age Groups', fontsize=14)

ax.xaxis.grid(True, linestyle=':', color='gray', alpha=0.5)

plt.tight_layout()
plt.show()