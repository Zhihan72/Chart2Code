import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
campaign_A = np.array([2, 3, 5, 7, 11, 13, 15, 20, 23, 30, 35])
campaign_B = np.array([1, 2, 3, 5, 8, 12, 17, 25, 31, 38, 45])
campaign_C = np.array([0, 1, 2, 4, 7, 10, 13, 18, 22, 29, 33])

cumulative_A = np.cumsum(campaign_A)
cumulative_B = np.cumsum(campaign_B)
cumulative_C = np.cumsum(campaign_C)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

ax1.plot(years, campaign_A, marker='o', linestyle='-', color='purple', linewidth=2)
ax1.plot(years, campaign_B, marker='s', linestyle='-', color='purple', linewidth=2)
ax1.plot(years, campaign_C, marker='^', linestyle='-', color='purple', linewidth=2)
ax1.grid(True, linestyle='--', alpha=0.6)

ax2.plot(years, cumulative_A, marker='o', linestyle='-', color='purple', linewidth=2)
ax2.plot(years, cumulative_B, marker='s', linestyle='-', color='purple', linewidth=2)
ax2.plot(years, cumulative_C, marker='^', linestyle='-', color='purple', linewidth=2)
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()