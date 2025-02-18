import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2023)

# Manually shuffled data
revenue = [88, 130, 60, 72, 160, 55, 190, 104]  # shuffled
profit_margin = [14, 18, 12, 13, 19, 10, 20, 16]  # shuffled

profit = [r * p / 100 for r, p in zip(revenue, profit_margin)]

fig, ax1 = plt.subplots(figsize=(10, 6))

ax1.plot(years, revenue, color='blue', marker='o', linestyle='-')
ax1.tick_params(axis='y', labelcolor='blue')

ax2 = ax1.twinx()
ax2.plot(years, profit, color='green', marker='s', linestyle='--')
ax2.tick_params(axis='y', labelcolor='green')

ax1.grid(True, linestyle='--', color='grey', alpha=0.6)

plt.tight_layout()
plt.show()