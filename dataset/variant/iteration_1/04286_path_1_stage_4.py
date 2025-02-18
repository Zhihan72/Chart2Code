import matplotlib.pyplot as plt
import numpy as np

sectors = ['Residential', 'Commercial', 'Industrial', 'Public Services', 'Transport']
energy_sources = ['Renewable', 'Fossil Fuels', 'Nuclear', 'Hydro']

energy_consumption = np.array([
    [120, 180, 30, 50],
    [110, 210, 60, 40],
    [90, 240, 80, 70],
    [70, 110, 40, 30],
    [100, 150, 50, 90]
])

total_consumption = energy_consumption.sum(axis=1)
sorted_indices = np.argsort(total_consumption)[::-1]
sorted_sectors = [sectors[i] for i in sorted_indices]
sorted_energy_consumption = energy_consumption[sorted_indices]

fig, ax = plt.subplots(figsize=(12, 8))

source_colors = ['#8e44ad', '#3498db', '#2ecc71', '#f1c40f']
bottom = np.zeros(len(sorted_sectors))

for i in range(len(energy_sources)):
    ax.bar(sorted_sectors, sorted_energy_consumption[:, i], color=source_colors[i], alpha=0.85, bottom=bottom)
    bottom += sorted_energy_consumption[:, i]

ax.set_xticks(np.arange(len(sorted_sectors)))
ax.set_xticklabels(sorted_sectors, rotation=45, ha='right')

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