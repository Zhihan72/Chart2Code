import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

alpha_advancement = np.array([20, 25, 32, 40, 50, 62, 75, 90, 108, 125])
beta_advancement = np.array([15, 22, 31, 42, 58, 72, 85, 104, 120, 140])

alpha_cumulative = np.cumsum(alpha_advancement)
beta_cumulative = np.cumsum(beta_advancement)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), sharex=True)

# Randomly altering stylistic elements
ax1.plot(years, alpha_advancement, color='blue', marker='v', linestyle='-', linewidth=1.5, label='Alpha')
ax1.plot(years, beta_advancement, color='green', marker='x', linestyle=':', linewidth=2.5, label='Beta')

# Adjusting grid style and appearance
ax1.grid(True, linestyle=':', alpha=0.5)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)
ax1.legend(loc='upper left', frameon=False)

# Altered bar plot colors and styles
ax2.bar(years - 0.15, alpha_cumulative, width=0.3, color='orange', alpha=0.7, label='Alpha Cumulative')
ax2.bar(years + 0.15, beta_cumulative, width=0.3, color='cyan', alpha=0.7, label='Beta Cumulative')

# Grid and legend adjustments
ax2.grid(True, linestyle=':', alpha=0.5)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.legend(loc='upper left', frameon=False)

plt.tight_layout()
plt.show()