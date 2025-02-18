import matplotlib.pyplot as plt
import numpy as np

sectors = ['Industrial', 'Public Services', 'Transport', 'Commercial', 'Residential']
energy_sources = ['Hydroelectric', 'Renewable', 'Nuclear', 'Fossil Fuels']

energy_consumption = np.array([
    [120, 180, 30, 40],
    [110, 210, 60, 50],
    [90, 240, 80, 70],
    [70, 110, 40, 20],
    [130, 190, 70, 60]
])

total_energy = energy_consumption.sum(axis=1)

sorted_indices = np.argsort(total_energy)
sectors_sorted = [sectors[i] for i in sorted_indices]
energy_consumption_sorted = energy_consumption[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

# Use varied colors for each energy source
colors = ['#ff9999','#66b3ff','#99ff99','#ffcc99']

bottom = np.zeros(len(sectors))
for i in range(energy_consumption_sorted.shape[1]):
    ax.bar(sectors_sorted, energy_consumption_sorted[:, i], color=colors[i], alpha=0.85, bottom=bottom, label=energy_sources[i])
    bottom += energy_consumption_sorted[:, i]

ax.set_ylabel('Energy Use (TWh)', fontsize=12, fontweight='bold', color='purple')
ax.set_xlabel('Energy Sectors', fontsize=12, fontweight='bold', color='purple')
ax.set_title('Energy Utilization by Sector & Type (Future Predictions)', fontsize=14, fontweight='bold', color='darkgreen', pad=15)

# Customize tick labels
ax.set_xticks(np.arange(len(sectors)))
ax.set_xticklabels(sectors_sorted, rotation=45, ha='right', fontsize=10, color='brown')

# A different grid style
ax.yaxis.grid(True, linestyle='-', linewidth=1, alpha=0.3)

# Add a border of the entire plot
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1.5)
    spine.set_color('gray')

# Allowing legend and modifying its style
ax.legend(loc='upper left', fontsize=10, title='Energy Sources', title_fontsize='13', frameon=True, shadow=True)

for bar in ax.patches:
    height = bar.get_height()
    if height > 0:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_y() + height / 2,
            f'{int(height)}',
            ha='center', va='center',
            fontsize=10, color='blue'
        )

plt.tight_layout()

plt.show()