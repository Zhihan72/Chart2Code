import matplotlib.pyplot as plt
import numpy as np

energy_sources = ['Solar', 'Wind', 'Hydro', 'Bio']
energy_production = np.array([1200, 1400, 1600, 600])
growth_rates = np.array([0.05, 0.03, 0.04, 0.045])

# Sort data in descending order based on energy production
sorted_indices = np.argsort(energy_production)[::-1]
energy_sources = [energy_sources[i] for i in sorted_indices]
energy_production = energy_production[sorted_indices]
growth_rates = growth_rates[sorted_indices]

# New set of colors
base_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']

positions = np.arange(len(energy_sources))

fig, ax1 = plt.subplots(figsize=(12, 7))

for idx, base_color in enumerate(base_colors):
    ax1.bar(positions[idx], energy_production[idx], color=base_color, width=0.6)

ax1.set_xticks(positions)
ax1.set_xticklabels(energy_sources, fontsize=12, rotation=45, ha='right')
ax1.set_ylabel('Production (TWh)', fontsize=14, color='black')
ax1.set_title('Renewable Energy 2023', fontsize=16, fontweight='bold', pad=20)

total_production = np.sum(energy_production)
for idx, bar in enumerate(ax1.patches):
    height = bar.get_height()
    percentage = (height / total_production) * 100
    ax1.annotate(f'{height} TWh\n({percentage:.1f}%)',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 5),
                 textcoords="offset points",
                 ha='center', va='bottom',
                 fontsize=10, color='black')

ax2 = ax1.twinx()
ax2.set_ylabel('Growth %', fontsize=14, color='blue')
ax2.plot(positions, growth_rates * 100, color='blue', linestyle='-', marker='o')
ax2.set_ylim(0, 10)
ax2.yaxis.set_major_formatter(lambda y, _: f'{y:.1f}%')

plt.tight_layout()
plt.show()