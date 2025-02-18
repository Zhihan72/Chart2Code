import matplotlib.pyplot as plt
import numpy as np

monthly_sales = np.array([
    [35, 40, 20, 25, 45, 30, 55, 35, 40, 30, 50, 60],  # First group's content altered
    [85, 60, 45, 30, 90, 55, 65, 50, 75, 25, 70, 80],  # Second group's content altered
    [45, 65, 30, 55, 50, 40, 55, 35, 60, 50, 40, 45],  # Third group's content altered
    [60, 70, 25, 35, 40, 20, 30, 45, 75, 55, 65, 50]   # Fourth group's content altered
])

fig, ax = plt.subplots(figsize=(14, 8))
bar_width = 0.2
r1 = np.arange(len(monthly_sales[0]))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]
r4 = [x + bar_width for x in r3]

common_color = 'c'
ax.bar(r1, monthly_sales[0], color=common_color, width=bar_width)
ax.bar(r2, monthly_sales[1], color=common_color, width=bar_width)
ax.bar(r3, monthly_sales[2], color=common_color, width=bar_width)
ax.bar(r4, monthly_sales[3], color=common_color, width=bar_width)

ax.set_xticks([r + bar_width for r in range(len(monthly_sales[0]))])
ax.set_xticklabels([])

plt.tight_layout()
plt.show()