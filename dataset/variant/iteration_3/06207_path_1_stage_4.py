import matplotlib.pyplot as plt
import numpy as np

regions = ['N', 'S', 'E', 'W']

apple_sales = np.array([
    [10, 15, 20, 25],
    [30, 35, 40, 45],
    [40, 45, 50, 55],
    [25, 30, 35, 40]
])
orange_sales = np.array([
    [20, 15, 10, 5],
    [25, 30, 35, 40],
    [35, 40, 45, 50],
    [30, 35, 45, 40]
])
banana_sales = np.array([
    [15, 20, 25, 30],
    [20, 25, 30, 35],
    [30, 35, 45, 50],
    [35, 40, 45, 50]
])

sizes = [apple_sales.sum(), orange_sales.sum(), banana_sales.sum()]
single_color = ['#ff9999']  # One consistent color for all

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(16, 8))

ax2.pie(sizes, explode=(0.1, 0, 0), labels=['Apple', 'Orange', 'Banana'], colors=single_color * 3,
        autopct='%1.1f%%', shadow=True, startangle=140, textprops={'fontsize': 10}, 
        wedgeprops={'width': 0.3})  # Changed for donut chart
ax2.axis('equal')
ax2.set_title('Sales Dist.', fontsize=14, fontweight='bold', pad=20)

x = np.arange(len(regions))
bar_width = 0.25

ax1.bar(x - bar_width, apple_sales.sum(axis=0), bar_width, label='Apple', color=single_color[0])
ax1.bar(x, orange_sales.sum(axis=0), bar_width, label='Orange', color=single_color[0])
ax1.bar(x + bar_width, banana_sales.sum(axis=0), bar_width, label='Banana', color=single_color[0])

ax1.set_title('Fruit Sales by Region', fontsize=14, fontweight='bold', pad=20)
ax1.set_xlabel('Region', fontsize=12)
ax1.set_ylabel('Sales Vol. (k)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(regions, fontsize=10)
ax1.legend(title='Fruit', loc='upper right')
ax1.grid(axis='y', linestyle='--', alpha=0.7)

fig.suptitle('Fruit Sales', fontsize=16, fontweight='bold', y=0.98)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()