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

# Single color for all bars
single_color = '#1E90FF'

bottom = np.zeros(len(sectors))
for i in range(energy_consumption_sorted.shape[1]):
    ax.bar(sectors_sorted, energy_consumption_sorted[:, i], color=single_color, alpha=0.85, bottom=bottom)
    bottom += energy_consumption_sorted[:, i]

ax.set_ylabel('Energy Use (TWh)', fontsize=12, fontweight='bold')
ax.set_xlabel('Energy Sectors', fontsize=12, fontweight='bold')
ax.set_title('Energy Utilization by Sector & Type (Future Predictions)', 
             fontsize=14, fontweight='bold', pad=15)

# Customize tick labels
ax.set_xticks(np.arange(len(sectors)))
ax.set_xticklabels(sectors_sorted, rotation=45, ha='right', fontsize=10)

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

for bar in ax.patches:
    height = bar.get_height()
    if height > 0:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_y() + height / 2,
            f'{int(height)}',
            ha='center', va='center',
            fontsize=10, color='black'
        )

plt.tight_layout()

plt.show()