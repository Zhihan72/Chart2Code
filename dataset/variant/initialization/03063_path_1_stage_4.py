import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

energy_production = np.array([1200, 1400, 1600, 400])  # in TWh
growth_rates = np.array([0.05, 0.03, 0.04, 0.02])  # hypothetical growth rates
new_base_colors = ['#FF5733', '#33FF57', '#3357FF', '#FF33A6']
new_gradient_colors = ['#FFB399', '#99FFB3', '#99B3FF', '#FF99CC']

positions = np.arange(len(energy_production))

fig, ax1 = plt.subplots(figsize=(12, 7))

for idx, (new_base_color, new_grad_color) in enumerate(zip(new_base_colors, new_gradient_colors)):
    ax1.barh(positions[idx], energy_production[idx], color=new_base_color, edgecolor=new_grad_color, linewidth=3, hatch='//', height=0.6)

total_production = np.sum(energy_production)
for idx, bar in enumerate(ax1.patches):
    width = bar.get_width()
    percentage = (width / total_production) * 100
    ax1.annotate(f'{width} TWh\n({percentage:.1f}%)',
                 xy=(width, bar.get_y() + bar.get_height() / 2),
                 xytext=(5, 0),
                 textcoords="offset points",
                 ha='left', va='center',
                 fontsize=10, color='black')

ax1.xaxis.grid(True, linestyle='--', alpha=0.7)

ax2 = ax1.twiny()
ax2.plot(growth_rates * 100, positions, color='blue', linestyle='-', marker='o')
ax2.set_xlim(0, 10)
ax2.xaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{x:.1f}%'))
ax2.spines['top'].set_color('blue')
ax2.tick_params(axis='x', colors='blue')

plt.tight_layout()
plt.show()