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
width = 0.2
x = np.arange(len(months))

for i, (category, sales) in enumerate(sales_data.items()):
    ax.bar(x + i * width, sales, width=width)

ax.set_xlabel('Mnths', fontsize=12)
ax.set_ylabel('Sales (k units)', fontsize=12)
ax.set_title('Sales Data 2023', fontsize=14, fontweight='bold')
ax.set_xticks(x + (len(categories) - 1) * width / 2)
ax.set_xticklabels(months)

for i, sales in enumerate(sales_data.values()):
    for j, value in enumerate(sales):
        ax.text(j + i * width, value + 1, f'{value}', ha='center', va='bottom', fontsize=8, color='black')

plt.tight_layout()
plt.show()