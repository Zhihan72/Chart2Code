import matplotlib.pyplot as plt
import numpy as np

coffee_types = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha']

sales_Q1 = [150, 200, 180, 220, 210]
sales_Q3 = [170, 220, 200, 240, 230]
sales_Q4 = [180, 230, 210, 250, 240]

data = [sales_Q1, sales_Q3, sales_Q4]

x = np.arange(len(coffee_types))
fig, ax = plt.subplots(figsize=(12, 7))
width = 0.2

single_color = '#3498db'

for i, sales in enumerate(data):
    ax.bar(x + i * width, sales, width, color=single_color)

ax.set_xticks(x + width)
ax.set_xticklabels(coffee_types)

ax.yaxis.grid(True, linestyle=':', linewidth=1, alpha=0.3)

plt.tight_layout()
plt.show()