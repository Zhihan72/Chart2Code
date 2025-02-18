import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

energy_sources = ['Solar', 'Wind', 'Hydro', 'Bio']
energy_production = np.array([1200, 1400, 1600, 600])
growth_rates = np.array([0.05, 0.03, 0.04, 0.045])

# Sort data in descending order based on energy production
sorted_indices = np.argsort(energy_production)[::-1]
energy_sources = [energy_sources[i] for i in sorted_indices]
energy_production = energy_production[sorted_indices]
growth_rates = growth_rates[sorted_indices]

base_colors = ['#FFD700', '#00BFFF', '#32CD32', '#8B4513']
gradient_colors = ['#FFF5CC', '#CCF0FF', '#C9ECC9', '#D2B48C']
base_colors = [base_colors[i] for i in sorted_indices]
gradient_colors = [gradient_colors[i] for i in sorted_indices]

positions = np.arange(len(energy_sources))

fig, ax1 = plt.subplots(figsize=(12, 7))

for idx, (base_color, grad_color) in enumerate(zip(base_colors, gradient_colors)):
    ax1.bar(positions[idx], energy_production[idx], color=base_color, edgecolor=grad_color, linewidth=3, hatch='//', width=0.6)

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

ax1.yaxis.grid(True, linestyle='--', alpha=0.7)

ax2 = ax1.twinx()
ax2.set_ylabel('Growth %', fontsize=14, color='blue')
ax2.plot(positions, growth_rates * 100, color='blue', linestyle='-', marker='o')
ax2.set_ylim(0, 10)
ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.1f}%'))
ax2.spines['right'].set_color('blue')
ax2.tick_params(axis='y', colors='blue')

custom_lines = [plt.Line2D([0], [0], color=color, lw=4, label=label) for color, label in zip(base_colors, energy_sources)]
ax1.legend(handles=custom_lines, loc='upper left', bbox_to_anchor=(1, 1), title='Sources')

plt.tight_layout()
plt.show()