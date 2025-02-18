import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Removed the last data group
energy_production = np.array([1200, 1400, 1600, 400])  # in TWh
growth_rates = np.array([0.05, 0.03, 0.04, 0.02])  # hypothetical growth rates
new_base_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']  # updated set of colors
new_gradient_colors = ['#FFB399', '#99FFB3', '#99B3FF', '#FF99CC']

positions = np.arange(len(energy_production))

fig, ax1 = plt.subplots(figsize=(12, 7))

for idx, (new_base_color, new_grad_color) in enumerate(zip(new_base_colors, new_gradient_colors)):
    ax1.bar(positions[idx], energy_production[idx], color=new_base_color, edgecolor=new_grad_color, linewidth=3, hatch='//', width=0.6)

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
ax2.plot(positions, growth_rates * 100, color='blue', linestyle='-', marker='o')
ax2.set_ylim(0, 10)
ax2.yaxis.set_major_formatter(FuncFormatter(lambda y, _: f'{y:.1f}%'))
ax2.spines['right'].set_color('blue')
ax2.tick_params(axis='y', colors='blue')

plt.tight_layout()
plt.show()