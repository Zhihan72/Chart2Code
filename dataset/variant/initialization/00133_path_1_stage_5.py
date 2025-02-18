import numpy as np
import matplotlib.pyplot as plt

months = ['Feb', 'May', 'Apr', 'Jan', 'Mar', 'Jun']  # Randomly altered order
coffee_varieties = ['Americano', 'Mocha', 'Espresso', 'Cappuccino', 'Latte']  # Randomly shuffled

sales_data = np.array([
    [180, 250, 200, 150, 220],
    [230, 190, 260, 210, 180],
    [200, 250, 230, 220, 270],
    [210, 230, 250, 300, 240],
    [220, 250, 320, 270, 260],
    [330, 270, 270, 290, 240]
])

fig, ax = plt.subplots(figsize=(12, 7))
bar_width = 0.15
indices = np.arange(len(months))

colors = ['#8B4513', '#DEB887', '#A0522D', '#CD853F', '#D2691E']  # Adjusted order

for i, variety in enumerate(coffee_varieties):
    ax.bar(
        indices + i * bar_width, 
        sales_data[:, i], 
        bar_width, 
        label=variety, 
        color=colors[i]
    )

ax.set_xticks(indices + bar_width * 2)
ax.set_xticklabels(months)
ax.set_xlabel('Time Period')
ax.set_ylabel('Volume Sold')
ax.set_title('Sales Overview: Coffee Flavors\nOver Monthly Periods', fontsize=14, fontweight='bold')
ax.legend(title='Types of Coffee')

plt.tight_layout()
plt.show()