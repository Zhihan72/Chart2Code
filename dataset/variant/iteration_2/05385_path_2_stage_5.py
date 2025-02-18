import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

alpha_advancement = np.array([20, 25, 32, 40, 50, 62, 75, 90, 108, 125])
beta_advancement = np.array([15, 22, 31, 42, 58, 72, 85, 104, 120, 140])

alpha_cumulative = np.cumsum(alpha_advancement)
beta_cumulative = np.cumsum(beta_advancement)

fig, ax2 = plt.subplots(figsize=(7, 7))

ax2.bar(years - 0.15, alpha_cumulative, width=0.3, color='orange', alpha=0.7, label='Alpha Cumulative')
ax2.bar(years + 0.15, beta_cumulative, width=0.3, color='cyan', alpha=0.7, label='Beta Cumulative')

ax2.grid(True, linestyle=':', alpha=0.5)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)
ax2.legend(loc='upper left', frameon=False)

plt.tight_layout()
plt.show()