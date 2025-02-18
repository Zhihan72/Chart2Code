import numpy as np
import matplotlib.pyplot as plt

months = ['Jun', 'Jan', 'Apr', 'Mar', 'May', 'Feb']
coffee_varieties = ['Mocha', 'Espresso', 'Americano', 'Latte', 'Cappuccino']
sales_data = np.array([
    [240, 150, 180, 200, 250],
    [150, 240, 180, 270, 330],
    [210, 200, 230, 250, 270],
    [200, 180, 220, 230, 260],
    [220, 210, 250, 260, 320],
    [180, 220, 190, 230, 260]
])

fig, ax = plt.subplots(figsize=(10, 6))

# Swap the sales_data matrix axes to iterate over months 
# Each bar represents a coffee type's sales in a specific month
sales_data = sales_data.T
bar_width = 0.15
x_indices = np.arange(len(months))

# Plot each coffee type
for i, coffee in enumerate(coffee_varieties):
    ax.bar(x_indices + i * bar_width, sales_data[i], width=bar_width, label=coffee)

ax.set_xticks(x_indices + bar_width * 2)
ax.set_xticklabels(months)
ax.set_xlabel('Months', labelpad=10)
ax.set_ylabel('Units Sold', labelpad=10)

ax.set_title('Monthly Sales Performance by Coffee Type', fontsize=14)
ax.legend(loc='best', fontsize=10)

plt.tight_layout()
plt.show()