import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

alpha_advancement = np.array([20, 25, 32, 40, 50, 62, 75, 90, 108, 125])
beta_advancement = np.array([15, 22, 31, 42, 58, 72, 85, 104, 120, 140])
gamma_advancement = np.array([10, 18, 25, 34, 47, 55, 68, 84, 100, 115])

alpha_cumulative = np.cumsum(alpha_advancement)
beta_cumulative = np.cumsum(beta_advancement)
gamma_cumulative = np.cumsum(gamma_advancement)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), sharex=True)

ax1.plot(years, alpha_advancement, color='b', marker='o', linestyle='--', linewidth=2)
ax1.plot(years, beta_advancement, color='g', marker='s', linestyle='-.', linewidth=2)
ax1.plot(years, gamma_advancement, color='r', marker='^', linestyle='-', linewidth=2)

ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

ax2.bar(years - 0.25, alpha_cumulative, width=0.25, color='b', alpha=0.6)
ax2.bar(years, beta_cumulative, width=0.25, color='g', alpha=0.6)
ax2.bar(years + 0.25, gamma_cumulative, width=0.25, color='r', alpha=0.6)

ax2.grid(True, linestyle='--', alpha=0.5)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)

plt.tight_layout()
plt.show()