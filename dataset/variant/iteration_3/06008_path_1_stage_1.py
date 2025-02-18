import matplotlib.pyplot as plt
import numpy as np

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

strawberry_sales = [150, 120, 130, 200, 180, 240, 250, 220, 210, 190, 160, 180]
banana_sales = [100, 80, 75, 95, 85, 105, 115, 110, 108, 102, 92, 104]
mango_sales = [90, 70, 65, 85, 75, 95, 100, 98, 94, 88, 72, 90]
kiwi_sales = [60, 55, 52, 60, 58, 65, 68, 64, 61, 59, 55, 62]

monthly_sales = np.array([strawberry_sales, banana_sales, mango_sales, kiwi_sales])

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.2
months_idx = np.arange(len(months))
ax.bar(months_idx - 1.5 * bar_width, strawberry_sales, width=bar_width, color='#FF6347', alpha=0.8)
ax.bar(months_idx - 0.5 * bar_width, banana_sales, width=bar_width, color='#FFD700', alpha=0.8)
ax.bar(months_idx + 0.5 * bar_width, mango_sales, width=bar_width, color='#FFA500', alpha=0.8)
ax.bar(months_idx + 1.5 * bar_width, kiwi_sales, width=bar_width, color='#7FFF00', alpha=0.8)

ax.set_xticks(months_idx)
ax.set_xticklabels(months, fontsize=12)

for i, sales in enumerate(monthly_sales):
    for j, value in enumerate(sales):
        ax.text(j - 1.5*bar_width + i*bar_width, value + 5, str(value),
                ha='center', va='bottom', fontsize=9, color='black', fontweight='bold')

ax.set_xlim(-1, len(months))

plt.tight_layout()

plt.show()