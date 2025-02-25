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

ax1.plot(years, alpha_advancement, label='Alpha Model', color='purple', marker='x', linestyle='-', linewidth=2)
ax1.plot(years, beta_advancement, label='Beta Model', color='orange', marker='D', linestyle=':', linewidth=2)
ax1.plot(years, gamma_advancement, label='Gamma Model', color='brown', marker='*', linestyle='-.', linewidth=2)

ax1.set_title('Annual Technological Advancements of AI Models', fontsize=12)
ax1.set_xlabel('Year', fontsize=10)
ax1.set_ylabel('Advancement Metric', fontsize=10)
ax1.legend(title='AI Models', loc='lower right', fontsize=8)
ax1.grid(False)
ax1.set_xticks(years)
ax1.set_xticklabels(years, rotation=45, fontsize=8)

ax2.bar(years - 0.3, alpha_cumulative, width=0.2, color='purple', alpha=0.7, label='Alpha Model')
ax2.bar(years, beta_cumulative, width=0.2, color='orange', alpha=0.7, label='Beta Model')
ax2.bar(years + 0.3, gamma_cumulative, width=0.2, color='brown', alpha=0.7, label='Gamma Model')

ax2.set_title('Cumulative Technological Advancements of AI Models', fontsize=12)
ax2.set_xlabel('Year', fontsize=10)
ax2.set_ylabel('Cumulative Metric', fontsize=10)
ax2.legend(title='AI Models', loc='upper right', fontsize=8)
ax2.grid(False)
ax2.set_xticks(years)
ax2.set_xticklabels(years, rotation=45, fontsize=8)

plt.tight_layout()
plt.show()