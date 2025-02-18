import matplotlib.pyplot as plt
import numpy as np

# Updated sectors and energy sources
sectors = ['Residential', 'Commercial', 'Industrial', 'Public Services', 'Transport']
energy_sources = ['Renewable', 'Fossil Fuels', 'Nuclear', 'Hydro']

# Updated energy consumption array with additional sector and energy source
energy_consumption = np.array([
    [120, 180, 30, 50],
    [110, 210, 60, 40],
    [90, 240, 80, 70],
    [70, 110, 40, 30],
    [100, 150, 50, 90]  # Transport
])

total_consumption = energy_consumption.sum(axis=1)

sorted_indices = np.argsort(total_consumption)[::-1]
sorted_sectors = [sectors[i] for i in sorted_indices]
sorted_energy_consumption = energy_consumption[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

# Include a new color for the additional energy source
source_colors = ['#8e44ad', '#3498db', '#2ecc71', '#f1c40f']  # Purple, Blue, Green, Yellow

bottom = np.zeros(len(sorted_sectors))
for i, source in enumerate(energy_sources):
    ax.bar(sorted_sectors, sorted_energy_consumption[:, i],
           label=source, color=source_colors[i], alpha=0.85, bottom=bottom)
    bottom += sorted_energy_consumption[:, i]

ax.set_ylabel('Energy Consumption (TWh)', fontsize=12, fontweight='bold')
ax.set_xlabel('Sectors', fontsize=12, fontweight='bold')
ax.set_title('Smart City Initiatives: Energy Consumption by Sector and Source (2025 Projections)', 
             fontsize=14, fontweight='bold', pad=15)

ax.legend(title='Energy Sources', loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

ax.set_xticks(np.arange(len(sorted_sectors)))
ax.set_xticklabels(sorted_sectors, rotation=45, ha='right', fontsize=10)

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