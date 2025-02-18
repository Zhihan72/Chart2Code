import matplotlib.pyplot as plt
import numpy as np

categories = ["Elec", "Fash", "Home", "Beaut", "Toys", "Books", "Sports", "Grocery"]
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

sales_data = [
    [120, 110, 105, 100, 95, 110],
    [80, 85, 90, 85, 80, 75],
    [50, 55, 60, 65, 70, 75],
    [30, 35, 40, 45, 50, 55],
    [20, 30, 25, 35, 30, 40],
    [10, 15, 20, 25, 30, 35],
    [40, 45, 50, 55, 60, 65],
    [100, 120, 110, 130, 120, 140]
]

sales_data = np.array(sales_data)

fig, ax = plt.subplots(figsize=(14, 8))

x = np.arange(len(months))
bar_width = 0.1

# Randomly alter the colors, note it's done manually as per restriction
colors = ['#99ff99', '#ffcc99', '#66b3ff', '#ff9999', '#ff6666', '#c2c2f0', '#ffb3e6', '#66ff99']

# Randomly alter bar border styles
linestyles = ['-', '--', '-.', ':', '-', '--', '-.', ':']

for i in range(len(categories)):
    ax.bar(x + i*bar_width, sales_data[i], width=bar_width, color=colors[i], 
           edgecolor='black', linestyle=linestyles[i], label=categories[i])

ax.set_title('Monthly Sales', fontsize=16, pad=20)
ax.set_ylabel('Sales (k USD)', fontsize=14)
ax.set_xticks(x + bar_width * (len(categories) - 1) / 2)
ax.set_xticklabels(months, rotation=45, ha='right', fontsize=12)

# Randomly change legend appearance
ax.legend(title="Categories", title_fontsize='12', fontsize='10', loc='upper left')

# Add a random grid style
ax.grid(axis='y', linestyle=':', linewidth=0.5, alpha=0.9)
plt.tight_layout()

plt.show()