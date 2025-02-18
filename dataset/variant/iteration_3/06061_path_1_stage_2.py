import matplotlib.pyplot as plt
import numpy as np

specialists = ['Specialist A', 'Specialist B', 'Specialist C', 'Specialist D']

monthly_sales = np.array([
    [30, 35, 20, 25, 40, 45, 30, 35, 40, 50, 60, 55],
    [25, 30, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],
    [40, 45, 50, 55, 60, 65, 55, 50, 45, 40, 35, 30],
    [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75]
])

satisfaction_scores = np.array([8.5, 9.0, 7.5, 8.0])

# Sorting the monthly sales for each specialist in ascending order
sorted_sales = [np.sort(sales) for sales in monthly_sales]

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.2

r1 = np.arange(len(sorted_sales[0]))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

ax.bar(r1, sorted_sales[0], color='b', width=bar_width, edgecolor='grey', label=specialists[0])
ax.bar(r2, sorted_sales[1], color='orange', width=bar_width, edgecolor='grey', label=specialists[1])
ax.bar(r3, sorted_sales[2], color='r', width=bar_width, edgecolor='grey', label=specialists[2])
ax.bar(r4, sorted_sales[3], color='g', width=bar_width, edgecolor='grey', label=specialists[3])

ax.set_title('Sorted Sales Performance of Sales Specialists', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Order of Sorted Sales', fontsize=14)
ax.set_ylabel('Sales (in thousands)', fontsize=14)
ax.set_xticks([r + bar_width * 1.5 for r in range(len(sorted_sales[0]))])
ax.set_xticklabels(['Order ' + str(i) for i in range(1, len(sorted_sales[0]) + 1)])
ax.legend()

plt.tight_layout()
plt.show()