import matplotlib.pyplot as plt
import numpy as np

screen_time = np.array([4, 10, 7, 0.5, 8, 5, 6, 3, 9, 12, 2, 11, 1])
sleep_quality = np.array([7.5, 3.5, 5, 9, 4.5, 6.5, 5.5, 8, 4, 2.5, 8, 3, 8.5])
sleep_disturbances = np.array([7, 18, 12, 3, 13, 9, 10, 6, 15, 22, 4, 20, 2])

fig, ax1 = plt.subplots(figsize=(12, 8))

# Changed the color from 'purple' to 'orange', and from 'green' to 'blue'.
ax1.scatter(screen_time, sleep_quality, c='orange', edgecolor='gray', s=120, alpha=0.6, marker='x')

ax2 = ax1.twinx()
ax2.plot(screen_time, sleep_disturbances, color='blue', linewidth=2, linestyle='-.')

ax1.grid(True, linestyle=':', alpha=0.8)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()