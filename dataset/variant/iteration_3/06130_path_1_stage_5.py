import matplotlib.pyplot as plt
import numpy as np

categories = ['Elec', 'Clth', 'Home']
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

sales_data = {
    'Elec': [25, 22, 27, 20, 30, 35, 40, 38, 45, 50, 55, 60],
    'Clth': [20, 25, 30, 28, 35, 40, 38, 42, 50, 55, 60, 65],
    'Home': [18, 22, 27, 23, 25, 30, 35, 33, 37, 40, 43, 45]
}

fig, ax = plt.subplots(figsize=(12, 8))
height = 0.2
y = np.arange(len(months))

colors = ['cyan', 'orange', 'purple']  # shuffled colors list

for i, (category, sales) in enumerate(sales_data.items()):
    ax.barh(y + i * height, sales, height=height, label=category, color=colors[i])

ax.set_ylabel('Months', fontsize=12)
ax.set_xlabel('Sales (k units)', fontsize=12)
ax.set_title('Sales Data 2023', fontsize=14, fontweight='bold')
ax.set_yticks(y + (len(categories) - 1) * height / 2)
ax.set_yticklabels(months)
ax.invert_yaxis()
ax.legend()

for i, sales in enumerate(sales_data.values()):
    for j, value in enumerate(sales):
        ax.text(value + 1, j + i * height, f'{value}', ha='left', va='center', fontsize=8, color='black')

plt.tight_layout()
plt.show()