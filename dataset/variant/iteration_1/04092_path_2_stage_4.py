import matplotlib.pyplot as plt
import numpy as np

cities = ['Londres', 'SaoPaulo', 'Tokyo', 'Beijing', 'Sidney', 'NovaYork', 'Paris', 'Berlin', 'Mumbai', 'Cairo']
coffee_consumption = [250, 300, 200, 280, 240, 220, 160, 180, 210, 220]

fig, ax = plt.subplots(figsize=(14, 8))

colors = ['#33FF57', '#3357FF', '#F333FF', '#FF5733', '#FF33C4', '#33FFC4', '#FF3364', '#33F3FF', '#FF9633', '#3367FF']

edge_styles = ['dotted', 'dashed', 'dashdot', 'solid', 'dotted', 'dashed', 'dashdot', 'solid', 'dotted', 'dashed']

# Reordering edge styles to illustrate changes in the visual style
bars = ax.bar(cities, coffee_consumption, color=colors, edgecolor='black', linestyle=edge_styles[1])

for bar, consumption in zip(bars, coffee_consumption):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, yval + 5, f'{consumption}', ha='center', va='bottom', fontsize=10, fontweight='bold', color='black')

# Title and labels shuffled and altered
ax.set_title('Monthly Coffee Rows by Place', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Metropolises', fontsize=12, labelpad=10)
ax.set_ylabel('Monthly Caffeine Portions', fontsize=12, labelpad=10)

ax.set_xticks(np.arange(len(cities)))
ax.set_xticklabels(cities, rotation=45, ha='right', fontsize=11)

ax.yaxis.grid(True, linestyle=':', linewidth=0.5, alpha=0.7)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()