import matplotlib.pyplot as plt
import numpy as np

zones = ['North', 'East', 'South', 'West']
seagrass_coverage_km2 = np.array([120, 150, 180, 160])
biodiversity_index = np.array([70, 80, 90, 85])
coral_reef_quality = np.array([7, 6, 8, 7.5])

# Sort data by seagrass_coverage_km2 in descending order
sorted_indices = np.argsort(seagrass_coverage_km2)[::-1]
zones = [zones[i] for i in sorted_indices]
seagrass_coverage_km2 = seagrass_coverage_km2[sorted_indices]
biodiversity_index = biodiversity_index[sorted_indices]
coral_reef_quality = coral_reef_quality[sorted_indices]

bar_width = 0.4

fig, ax1 = plt.subplots(figsize=(14, 8))
x_positions = np.arange(len(zones))

# Change colors
ax1.bar(x_positions - bar_width/2, seagrass_coverage_km2, bar_width, color='darkolivegreen')

ax2 = ax1.twinx()
ax2.plot(x_positions, biodiversity_index, color='royalblue', lw=2, marker='o')
ax2.plot(x_positions, coral_reef_quality, color='tomato', lw=2, marker='s')

annotations = {
    'North': ('Conserv Efforts', (10, 50)),
    'South': ('Coral Restor', (-65, -30)),
}

for zone, (text, offset) in annotations.items():
    if zone in zones:
        index = zones.index(zone)
        ax1.annotate(
            text,
            (x_positions[index], seagrass_coverage_km2[index]),
            xytext=offset, textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='grey'),
            ha='center', fontsize=10, color='darkred'
        )

ax1.set_title("Seagrass & Biodiversity in Zones (2023)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Zone", fontsize=14)
ax1.set_ylabel("Seagrass (km²)", fontsize=14, color='darkolivegreen')
ax2.set_ylabel("Indices", fontsize=14, color='royalblue')

ax1.set_xticks(x_positions)
ax1.set_xticklabels(zones, rotation=45, ha='right', fontsize=12)
ax1.yaxis.set_tick_params(labelcolor='darkolivegreen')
ax2.yaxis.set_tick_params(labelcolor='royalblue')

plt.tight_layout()

plt.show()