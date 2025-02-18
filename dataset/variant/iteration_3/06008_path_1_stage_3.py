import matplotlib.pyplot as plt
import numpy as np

strawberry_sales = [150, 120, 130, 200, 180, 240, 250, 220, 210, 190, 160, 180]
banana_sales = [100, 80, 75, 95, 85, 105, 115, 110, 108, 102, 92, 104]
mango_sales = [90, 70, 65, 85, 75, 95, 100, 98, 94, 88, 72, 90]
kiwi_sales = [60, 55, 52, 60, 58, 65, 68, 64, 61, 59, 55, 62]

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.2
months_idx = np.arange(len(strawberry_sales))

single_color = '#4B0082'
ax.bar(months_idx - 1.5 * bar_width, strawberry_sales, width=bar_width, color=single_color, alpha=0.8)
ax.bar(months_idx - 0.5 * bar_width, banana_sales, width=bar_width, color=single_color, alpha=0.8)
ax.bar(months_idx + 0.5 * bar_width, mango_sales, width=bar_width, color=single_color, alpha=0.8)
ax.bar(months_idx + 1.5 * bar_width, kiwi_sales, width=bar_width, color=single_color, alpha=0.8)

ax.set_xticks([])
ax.set_yticks([])

ax.set_xlim(-1, len(strawberry_sales))

plt.tight_layout()

plt.show()