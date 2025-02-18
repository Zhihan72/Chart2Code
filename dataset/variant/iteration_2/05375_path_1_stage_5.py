import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
electronics_sales = np.array([35, 28, 55, 40, 50, 75, 25, 70, 65, 60, 30, 45])
furniture_sales = np.array([38, 25, 52, 22, 45, 30, 48, 35, 20, 40, 42, 50])
clothing_sales = np.array([60, 55, 18, 30, 50, 40, 20, 65, 45, 35, 15, 25])

# Calculate divergences
net_sales = electronics_sales + furniture_sales + clothing_sales
centered_electronics = electronics_sales - net_sales / 3
centered_furniture = furniture_sales - net_sales / 3
centered_clothing = clothing_sales - net_sales / 3

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# The original pie chart remains unchanged
overall_sales = np.array([sum(electronics_sales), sum(furniture_sales), sum(clothing_sales)])
categories = ['Elec', 'Furn', 'Cloth']
ax1.pie(overall_sales, labels=categories, autopct='%1.1f%%', startangle=140, colors=['darkorange', 'darkviolet', 'deepskyblue'])
ax1.set_title("Sales Dist (2023)", fontsize=14, fontweight='bold')

x_indices = np.arange(len(months))

# Plotting the diverging bar chart
ax2.bar(x_indices, centered_electronics, label='Elec', color='darkorange')
ax2.bar(x_indices, centered_furniture, label='Furn', color='darkviolet', bottom=centered_electronics)
ax2.bar(x_indices, centered_clothing, label='Cloth', color='deepskyblue', bottom=centered_electronics + centered_furniture)

ax2.set_title("Diverging Monthly Sales (2023)", fontsize=14, fontweight='bold')
ax2.set_xlabel("Month", fontsize=12)
ax2.set_ylabel("Sales Divergence (k USD)", fontsize=12)
ax2.set_xticks(x_indices)
ax2.set_xticklabels(months)
ax2.legend(title="Product", fontsize=10)
ax2.axhline(0, color='black', linewidth=0.8)
ax2.grid(axis='y', linestyle='--', alpha=0.7)

plt.setp(ax2.get_xticklabels(), rotation=45, horizontalalignment='right', fontsize=10)
plt.setp(ax2.get_yticklabels(), fontsize=10)

plt.tight_layout(pad=3.0)
plt.show()