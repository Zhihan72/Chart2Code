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

bottom_values = np.zeros(len(weeks))

for sales, color in zip(total_sales, colors):
    ax.bar(weeks, sales, bottom=bottom_values, color=color, edgecolor='black', alpha=0.85)
    bottom_values += np.array(sales)

ax.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)

ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()

plt.show()