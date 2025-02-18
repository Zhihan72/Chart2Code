import numpy as np
import matplotlib.pyplot as plt

months = ['Jun', 'Jan', 'Apr', 'Mar', 'May', 'Feb']
coffee_varieties = ['Espresso', 'Americano', 'Latte', 'Cappuccino']
sales_data = np.array([
    [150, 180, 200, 250],
    [240, 180, 270, 330],
    [200, 230, 250, 270],
    [180, 220, 230, 260],
    [210, 250, 260, 320],
    [220, 190, 230, 260]
])

fig, ax = plt.subplots(figsize=(10, 6))

# Adjusted sales_data without Mocha
sales_data = sales_data.T
bar_width = 0.2
x_indices = np.arange(len(months))

# Plot each remaining coffee type
for i, coffee in enumerate(coffee_varieties):
    ax.bar(x_indices + i * bar_width, sales_data[i], width=bar_width, label=coffee)

ax.set_xticks(x_indices + bar_width * 1.5)
ax.set_xticklabels(months)
ax.set_xlabel('Months', labelpad=10)
ax.set_ylabel('Units Sold', labelpad=10)

ax.set_title('Monthly Sales Performance by Coffee Type', fontsize=14)
ax.legend(loc='best', fontsize=10)

plt.tight_layout()
plt.show()