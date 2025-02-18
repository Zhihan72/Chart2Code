import matplotlib.pyplot as plt
import numpy as np

weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
soft_drinks = ['Cola', 'Lemon-Lime', 'Ginger Ale', 'Root Beer']

cola_sales = [150, 160, 170, 180]
lemon_lime_sales = [90, 100, 120, 130]
ginger_ale_sales = [70, 80, 95, 110]
root_beer_sales = [50, 55, 60, 65]

total_sales = [cola_sales, lemon_lime_sales, ginger_ale_sales, root_beer_sales]

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
marker_styles = ['o', 's', '^', 'D']  # Circle, Square, Triangle Up, Diamond
line_styles = ['-', '--', '-.', ':']  # Solid, Dashed, Dash-dot, Dotted

bottom_values = np.zeros(len(weeks))

for sales, color, marker, line in zip(total_sales, colors, marker_styles, line_styles):
    ax.bar(weeks, sales, bottom=bottom_values, color=color, edgecolor='black', alpha=0.85)
    bottom_values += np.array(sales)

ax.legend(soft_drinks, loc='upper center', bbox_to_anchor=(0.5, -0.05), fontsize=12, ncol=4, frameon=False)

ax.yaxis.grid(False)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_linewidth(1.5)
ax.spines['bottom'].set_color('gray')
ax.spines['left'].set_color('gray')

plt.tight_layout()

plt.show()