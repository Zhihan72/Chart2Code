import matplotlib.pyplot as plt
import numpy as np

# Shuffling sales numbers within each fruit group manually
strawberry_sales = [210, 180, 130, 150, 200, 240, 250, 120, 180, 220, 190, 160]
banana_sales = [75, 85, 80, 100, 95, 105, 115, 110, 92, 102, 104, 108]
mango_sales = [65, 75, 70, 90, 85, 95, 100, 98, 94, 88, 72, 90]
kiwi_sales = [60, 68, 58, 64, 62, 55, 52, 59, 55, 61, 60, 65]

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