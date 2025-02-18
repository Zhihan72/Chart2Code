import matplotlib.pyplot as plt
import numpy as np

cities = ['Tokyo', 'New York', 'Sydney', 'London', 'Paris', 'Berlin', 'Mumbai', 'São Paulo', 'Beijing', 'Cairo']
coffee_consumption = [250, 300, 200, 280, 240, 220, 160, 180, 210, 220]

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#33FF57', '#3357FF', '#F333FF', '#FF5733', '#FF33C4', '#33FFC4', '#FF3364', '#33F3FF', '#FF9633', '#3367FF']

edge_styles = ['dotted', 'dashed', 'dashdot', 'solid', 'dotted', 'dashed', 'dashdot', 'solid', 'dotted', 'dashed']

bars = ax.bar(cities, coffee_consumption, color=colors, edgecolor='black', linestyle=edge_styles[0])

for bar, consumption in zip(bars, coffee_consumption):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{consumption}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

ax.set_title('Coffee Consumption by City', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Cities', fontsize=12, labelpad=10)
ax.set_ylabel('Cups of Coffee per Month', fontsize=12, labelpad=10)

ax.set_xticks(np.arange(len(cities)))
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=11)

ax.yaxis.grid(True, linestyle=':', linewidth=0.5, alpha=0.7)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()