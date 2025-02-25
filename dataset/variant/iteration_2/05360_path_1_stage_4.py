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