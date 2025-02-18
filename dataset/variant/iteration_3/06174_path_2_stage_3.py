import matplotlib.pyplot as plt
import numpy as np

categories = ["Apples", "Bananas", "Oranges", "Peaches", "Plums"]
q1_sales = [120, 80, 150, 90, 60]
q2_sales = [130, 85, 160, 95, 70]
q3_sales = [140, 95, 170, 100, 75]
q4_sales = [150, 100, 180, 110, 80]
avg_sales_per_quarter = np.mean([q1_sales, q2_sales, q3_sales, q4_sales], axis=0)

fig, ax1 = plt.subplots(figsize=(14, 8))

height = 0.2
y = np.arange(len(categories))

# Shuffled color assignments for the quarterly sales bars
bars1 = ax1.barh(y - 1.5*height, q1_sales, height, label='Q1', color='firebrick', hatch='/', edgecolor='maroon')
bars2 = ax1.barh(y - 0.5*height, q2_sales, height, label='Q2', color='forestgreen', hatch='\\', edgecolor='darkgreen')
bars3 = ax1.barh(y + 0.5*height, q3_sales, height, label='Q3', color='steelblue', hatch='-', edgecolor='navy')
bars4 = ax1.barh(y + 1.5*height, q4_sales, height, label='Q4', color='darkorange', hatch='|', edgecolor='tan')

ax1.set_title("Quarterly Sales Performance of Fruits", fontsize=18, weight='bold', pad=20)
ax1.set_ylabel("Fruit Categories", fontsize=14)
ax1.set_xlabel("Sales (Thousands)", fontsize=14, color='midnightblue')
ax1.set_yticks(y)
ax1.set_yticklabels(categories, fontsize=12)
ax1.tick_params(axis='x', colors='midnightblue')
ax1.grid(axis='y', linestyle=':', linewidth=0.75, alpha=0.7)

ax2 = ax1.twiny()
ax2.plot(avg_sales_per_quarter, categories, color='darkviolet', linestyle='-', marker='s', markersize=10, label='Avg Sales', alpha=0.8)
ax2.set_xlabel("Avg Sales (Thousands)", fontsize=14, color='darkviolet')
ax2.tick_params(axis='x', colors='darkviolet')

fig.legend(loc='upper left', bbox_to_anchor=(0.05, 1), fontsize=12, frameon=True, framealpha=0.3)

plt.tight_layout()
plt.show()