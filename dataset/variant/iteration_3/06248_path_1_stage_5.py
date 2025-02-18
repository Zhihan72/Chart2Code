import matplotlib.pyplot as plt
import numpy as np

zones = ['N Coast', 'E Coast', 'S Coast', 'W Coast']
seagrass_coverage = np.array([130, 140, 170, 150])
biodiversity_index = np.array([85, 75, 95, 80])
coral_reef_quality = np.array([8, 5.5, 7.5, 7])

bar_height = 0.4
fig, ax1 = plt.subplots(figsize=(14, 8))
y_positions = np.arange(len(zones))

# Shuffled colors for each data group
ax1.barh(y_positions - bar_height/2, seagrass_coverage, bar_height, label='Seagrass Coverage', color='tomato')

ax2 = ax1.twiny()

ax2.plot(biodiversity_index, y_positions, color='mediumaquamarine', lw=2, marker='v', linestyle='--', label='Biodiversity')
ax2.plot(coral_reef_quality, y_positions, color='royalblue', lw=2, marker='d', linestyle='-.', label='Coral Quality')

annotations = {
    'N Coast': ('Conservation', (-65, -30)),
    'S Coast': ('Restoration', (50, -30)),
}

for zone, (text, offset) in annotations.items():
    index = np.where(np.array(zones) == zone)[0][0]
    ax1.annotate(
        text,
        (seagrass_coverage[index], y_positions[index]),
        xytext=offset,
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='black'),
        ha='center', fontsize=10, color='firebrick'
    )

ax1.set_title("Seagrass & Biodiversity\n(2023)", fontsize=16, fontweight='bold', pad=20)
ax1.set_ylabel("Zone", fontsize=14)
ax1.set_xlabel("Seagrass (km²)", fontsize=14, color='tomato')
ax2.set_xlabel("Index", fontsize=14, color='mediumaquamarine')

ax1.set_yticks(y_positions)
ax1.set_yticklabels(zones, rotation=0, fontsize=12)
ax1.xaxis.set_tick_params(labelcolor='tomato')
ax2.xaxis.set_tick_params(labelcolor='mediumaquamarine')

bars = ax1.patches
lines = ax2.get_lines()
labels = [bar.get_label() for bar in bars] + [line.get_label() for line in lines]
ax1.legend(lines + [ax1.containers[0]], labels, loc='upper right', fontsize=11)
ax1.grid(False)
plt.tight_layout()
plt.show()