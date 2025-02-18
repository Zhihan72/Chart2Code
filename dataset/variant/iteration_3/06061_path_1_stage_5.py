import matplotlib.pyplot as plt
import numpy as np

specialists = ['Expert X', 'Guru Y', 'Master Z', 'Ninja W', 'Champion V']

monthly_sales = np.array([
    [30, 35, 20, 25, 40, 45, 30, 35, 40, 50, 60, 55],
    [25, 30, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90],
    [40, 45, 50, 55, 60, 65, 55, 50, 45, 40, 35, 30],
    [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
    [50, 55, 60, 65, 45, 50, 35, 40, 75, 80, 85, 90]  # New data series for Champion V
])

sorted_sales = [np.sort(sales) for sales in monthly_sales]
fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.15

r1 = np.arange(len(sorted_sales[0]))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]
r5 = [x + bar_width for x in r4]  # Positioning for the new data series

ax.bar(r1, sorted_sales[0], color='green', width=bar_width, linestyle='dotted', label=specialists[0])
ax.bar(r2, sorted_sales[1], color='purple', width=bar_width, linestyle='dashed', label=specialists[1])
ax.bar(r3, sorted_sales[2], color='cyan', width=bar_width, linestyle='-.', label=specialists[2])
ax.bar(r4, sorted_sales[3], color='magenta', width=bar_width, linestyle='solid', label=specialists[3])
ax.bar(r5, sorted_sales[4], color='orange', width=bar_width, linestyle='-', label=specialists[4])  # New series

ax.set_title('Ranked Outputs of Sales Advisors', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Position in Order', fontsize=14)
ax.set_ylabel('Volume (in units)', fontsize=14)
ax.set_xticks([r + bar_width * 2 for r in range(len(sorted_sales[0]))])
ax.set_xticklabels(['Layer ' + str(i) for i in range(1, len(sorted_sales[0]) + 1)])

ax.legend(loc='upper left')
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()