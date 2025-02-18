import matplotlib.pyplot as plt
import numpy as np

weeks = ['Week 1', 'Week 2', 'Week 3', 'Week 4']
soft_drinks = ['Cola', 'Lemon-Lime', 'Ginger Ale', 'Root Beer', 'Orange Soda']

cola_sales = [150, 160, 170, 180]
lemon_lime_sales = [90, 100, 120, 130]
ginger_ale_sales = [70, 80, 95, 110]
root_beer_sales = [50, 55, 60, 65]
orange_soda_sales = [60, 75, 85, 95]

total_sales = np.array([cola_sales, lemon_lime_sales, ginger_ale_sales, root_beer_sales, orange_soda_sales])

# Calculate average sales for each week
average_sales = np.mean(total_sales, axis=0)

# Calculate divergence from the average sales
divergence = total_sales - average_sales

fig, ax = plt.subplots(figsize=(12, 8))

colors = ['#d62728', '#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd']

for div, sales, color in zip(divergence, total_sales, colors):
    ax.bar(weeks, div, color=color, edgecolor='black', alpha=0.85, label=soft_drinks[np.argmax(sales)])

ax.axhline(0, color='gray', linewidth=0.8)
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fontsize=12, ncol=5, frameon=False)

ax.set_ylabel('Divergence from Average Sales')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_linewidth(1.5)
ax.spines['bottom'].set_color('gray')

plt.tight_layout()
plt.show()