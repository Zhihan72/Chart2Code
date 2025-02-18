import matplotlib.pyplot as plt
import numpy as np

zones = ['N Coast', 'E Coast', 'S Coast', 'W Coast']

seagrass_coverage = np.array([120, 150, 180, 160])
biodiversity_index = np.array([70, 80, 90, 85])
coral_reef_quality = np.array([7, 6, 8, 7.5])

bar_width = 0.4

fig, ax1 = plt.subplots(figsize=(14, 8))
x_positions = np.arange(len(zones))

ax1.bar(x_positions - bar_width/2, seagrass_coverage, bar_width, label='Seagrass (km²)', color='seagreen')

ax2 = ax1.twinx()

ax2.plot(x_positions, biodiversity_index, color='deepskyblue', lw=2, marker='o', label='Biodiversity')
ax2.plot(x_positions, coral_reef_quality, color='coral', lw=2, marker='s', label='Coral Quality')

annotations = {
    'N Coast': ('Conservation', (10, 50)),
    'S Coast': ('Restoration', (-65, -30)),
}

for zone, (text, offset) in annotations.items():
    index = np.where(np.array(zones) == zone)[0][0]
    ax1.annotate(
        text,
        (x_positions[index], seagrass_coverage[index]),
        xytext=offset,
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='grey'),
        ha='center', fontsize=10, color='darkred'
    )

ax1.set_title("Seagrass & Biodiversity\n(2023)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Zone", fontsize=14)
ax1.set_ylabel("Seagrass (km²)", fontsize=14, color='seagreen')
ax2.set_ylabel("Index", fontsize=14, color='deepskyblue')

bars = ax1.patches
lines = ax2.get_lines()
labels = [bar.get_label() for bar in bars] + [line.get_label() for line in lines]
ax1.legend(lines + [ax1.containers[0]], labels, loc='upper left', fontsize=12)

ax1.set_xticks(x_positions)
ax1.set_xticklabels(zones, rotation=45, ha='right', fontsize=12)
ax1.yaxis.set_tick_params(labelcolor='seagreen')
ax2.yaxis.set_tick_params(labelcolor='deepskyblue')

ax1.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()