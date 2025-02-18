import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2023)

revenue = [88, 130, 60, 72, 160, 55, 190, 104]
profit_margin = [14, 18, 12, 13, 19, 10, 20, 16]

profit = [r * p / 100 for r, p in zip(revenue, profit_margin)]

fig, ax1 = plt.subplots(figsize=(10, 6))

# Altered marker types and line styles
ax1.plot(years, revenue, color='purple', marker='^', linestyle=':')
ax1.tick_params(axis='y', labelcolor='purple')

ax2 = ax1.twinx()
ax2.plot(years, profit, color='orange', marker='x', linestyle='-.')
ax2.tick_params(axis='y', labelcolor='orange')

# Altered grid style
ax1.grid(True, linestyle='-', color='black', alpha=0.3)

# Added border around the plot area
for spine in ax1.spines.values():
    spine.set_edgecolor('black')
    spine.set_linewidth(1.2)

plt.tight_layout()
plt.show()