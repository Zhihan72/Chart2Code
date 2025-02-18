import matplotlib.pyplot as plt
import numpy as np

# Seagrass Coverage and Marine Biodiversity in Coastal Zones

# Coastal zones
zones = ['North Coast', 'East Coast', 'South Coast', 'West Coast']

# Data: Seagrass coverage (square kilometers)
seagrass_coverage_km2 = np.array([120, 150, 180, 160])

# Data: Marine biodiversity index (out of 100)
biodiversity_index = np.array([70, 80, 90, 85])

# Data: Coral reef quality index (out of 10)
coral_reef_quality = np.array([7, 6, 8, 7.5])

# Bar width for seagrass coverage bars
bar_width = 0.4

fig, ax1 = plt.subplots(figsize=(14, 8))

# Position of the bars on the x-axis
x_positions = np.arange(len(zones))

# Create bar chart for seagrass coverage
bars1 = ax1.bar(x_positions - bar_width/2, seagrass_coverage_km2, bar_width, label='Seagrass Coverage (km²)', color='seagreen')

# Create secondary y-axis for marine biodiversity index and coral reef quality
ax2 = ax1.twinx()

# Line plot for marine biodiversity index
line1 = ax2.plot(x_positions, biodiversity_index, color='deepskyblue', lw=2, marker='o', label='Marine Biodiversity Index')

# Line plot for coral reef quality
line2 = ax2.plot(x_positions, coral_reef_quality, color='coral', lw=2, marker='s', label='Coral Reef Quality Index')

# Annotate significant points
annotations = {
    'North Coast': ('Conservation Efforts', (10, 50)),
    'South Coast': ('Coral Restoration', (-65, -30)),
}

for zone, (text, offset) in annotations.items():
    index = np.where(np.array(zones) == zone)[0][0]
    ax1.annotate(
        text,
        (x_positions[index], seagrass_coverage_km2[index]),
        xytext=offset,
        textcoords='offset points',
        arrowprops=dict(arrowstyle='->', color='grey'),
        ha='center', fontsize=10, color='darkred'
    )

# Titles and labels
ax1.set_title("Seagrass Coverage and Marine Biodiversity in Coastal Zones\n(2023)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Coastal Zone", fontsize=14)
ax1.set_ylabel("Seagrass Coverage (km²)", fontsize=14, color='seagreen')
ax2.set_ylabel("Index Values", fontsize=14, color='deepskyblue')

# Legends
bars = bars1.patches
lines = line1 + line2
labels = [bar.get_label() for bar in bars] + [line.get_label() for line in lines]
ax1.legend(lines + [bars1], labels, loc='upper left', fontsize=12)

# Setting x-ticks and x-tick labels
ax1.set_xticks(x_positions)
ax1.set_xticklabels(zones, rotation=45, ha='right', fontsize=12)

# Styling
ax1.yaxis.set_tick_params(labelcolor='seagreen')
ax2.yaxis.set_tick_params(labelcolor='deepskyblue')

# Grid and layout adjustments
ax1.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# Show the plot
plt.show()