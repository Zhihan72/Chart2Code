import numpy as np
import matplotlib.pyplot as plt

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
coffee_varieties = ['Espresso', 'Latte', 'Cappuccino', 'Americano', 'Mocha']

sales_data = np.array([
    [200, 150, 220, 180, 250],
    [260, 210, 180, 230, 190],
    [230, 220, 270, 200, 250],
    [250, 300, 240, 210, 230],
    [320, 270, 260, 220, 250],
    [270, 290, 240, 330, 270]
])

fig, ax = plt.subplots(figsize=(12, 7))
bar_width = 0.15
indices = np.arange(len(months))

colors = ['#A0522D', '#D2691E', '#8B4513', '#CD853F', '#DEB887']

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
ax.set_xlabel('Months')
ax.set_ylabel('Units Sold')
ax.set_title('Monthly Sales Performance\nof Coffee Varieties', fontsize=14, fontweight='bold')
ax.legend(title='Coffee Varieties')

plt.tight_layout()
plt.show()