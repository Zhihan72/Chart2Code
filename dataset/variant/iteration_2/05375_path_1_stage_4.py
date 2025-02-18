import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
electronics_sales = [35, 28, 55, 40, 50, 75, 25, 70, 65, 60, 30, 45]
furniture_sales = [38, 25, 52, 22, 45, 30, 48, 35, 20, 40, 42, 50]
clothing_sales = [60, 55, 18, 30, 50, 40, 20, 65, 45, 35, 15, 25]

overall_sales = np.array([sum(electronics_sales), sum(furniture_sales), sum(clothing_sales)])
categories = ['Elec', 'Furn', 'Cloth']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ax1.pie(overall_sales, labels=categories, autopct='%1.1f%%', startangle=140, colors=['darkorange', 'darkviolet', 'deepskyblue'])
ax1.set_title("Sales Dist (2023)", fontsize=14, fontweight='bold')

bar_width = 0.25
x_indices = np.arange(len(months))

ax2.bar(x_indices, electronics_sales, bar_width, label='Elec', color='darkorange')
ax2.bar(x_indices + bar_width, furniture_sales, bar_width, label='Furn', color='darkviolet')
ax2.bar(x_indices + 2 * bar_width, clothing_sales, bar_width, label='Cloth', color='deepskyblue')

ax2.set_title("Monthly Sales (2023)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Mon", fontsize=12)
ax2.set_ylabel("Sales (k USD)", fontsize=12)
ax2.set_xticks(x_indices + bar_width)
ax2.set_xticklabels(months)
ax2.legend(title="Prod", fontsize=10)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

plt.setp(ax2.get_xticklabels(), rotation=45, horizontalalignment='right', fontsize=10)
plt.setp(ax2.get_yticklabels(), fontsize=10)

ax2.annotate('Max Sales', xy=(11, 75), xytext=(8, 80),
             arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)
ax2.annotate('Summer', xy=(7, 55), xytext=(4, 60),
             arrowprops=dict(facecolor='black', arrowstyle='->', alpha=0.7), fontsize=11)

plt.tight_layout(pad=3.0)

plt.show()