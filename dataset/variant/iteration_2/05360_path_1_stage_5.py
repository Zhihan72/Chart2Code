import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
# Manually shuffled data within campaigns while retaining the same structure
campaign_A = np.array([13, 5, 2, 7, 3, 15, 11, 23, 20, 35, 30])
campaign_B = np.array([17, 3, 1, 31, 2, 12, 5, 8, 45, 25, 38])
campaign_C = np.array([2, 4, 13, 1, 7, 22, 0, 10, 33, 18, 29])

cumulative_A = np.cumsum(campaign_A)
cumulative_B = np.cumsum(campaign_B)
cumulative_C = np.cumsum(campaign_C)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5), sharey=True)

ax1.plot(years, campaign_A, marker='*', linestyle='--', color='green', linewidth=1.5)
ax1.plot(years, campaign_B, marker='D', linestyle='-.', color='blue', linewidth=1.5)
ax1.plot(years, campaign_C, marker='x', linestyle=':', color='red', linewidth=1.5)
ax1.grid(True, linestyle='-', alpha=0.9)
ax1.set_title("Annual Campaign Data")

ax2.plot(years, cumulative_A, marker='h', linestyle='--', color='orange', linewidth=1.5)
ax2.plot(years, cumulative_B, marker='p', linestyle='-', color='gray', linewidth=1.5)
ax2.plot(years, cumulative_C, marker='v', linestyle='-', color='brown', linewidth=1.5)
ax2.grid(False)
ax2.set_title("Cumulative Campaign Data")

plt.legend(['Campaign A', 'Campaign B', 'Campaign C'], loc='upper left', bbox_to_anchor=(1, 1))
plt.tight_layout()
plt.show()