import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2013, 2023)

alpha_advancement = np.array([20, 25, 32, 40, 50, 62, 75, 90, 108, 125])
beta_advancement = np.array([15, 22, 31, 42, 58, 72, 85, 104, 120, 140])

alpha_cumulative = np.cumsum(alpha_advancement)
beta_cumulative = np.cumsum(beta_advancement)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 7), sharex=True)

# Apply a single color 'purple' to both line plots on ax1
ax1.plot(years, alpha_advancement, color='purple', marker='o', linestyle='--', linewidth=2)
ax1.plot(years, beta_advancement, color='purple', marker='s', linestyle='-.', linewidth=2)

ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45)

# Apply the same color 'purple' to both bar plots on ax2
ax2.bar(years - 0.125, alpha_cumulative, width=0.25, color='purple', alpha=0.6)
ax2.bar(years + 0.125, beta_cumulative, width=0.25, color='purple', alpha=0.6)

ax2.grid(True, linestyle='--', alpha=0.5)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45)

plt.tight_layout()
plt.show()