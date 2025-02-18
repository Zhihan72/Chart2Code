import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

esports_rev = np.array([0.5, 0.7, 1.0, 1.4, 1.9, 2.4, 3.0, 3.8, 4.7, 5.8, 7.0])
robot_rev = np.array([0.3, 0.5, 0.6, 0.8, 1.1, 1.5, 1.9, 2.4, 3.0, 3.7, 4.5])
drone_rev = np.array([0.1, 0.2, 0.4, 0.6, 0.9, 1.3, 1.8, 2.5, 3.3, 4.2, 5.2])
ar_rev = np.array([0.2, 0.3, 0.5, 0.7, 1.0, 1.4, 1.9, 2.3, 2.9, 3.5, 4.1])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, esports_rev, marker='o', linestyle='-', color='orange', linewidth=2, label='E-sports')
ax.plot(years, robot_rev, marker='^', linestyle='-', color='cyan', linewidth=2, label='Robot')
ax.plot(years, drone_rev, marker='s', linestyle='-', color='magenta', linewidth=2, label='Drone')
ax.plot(years, ar_rev, marker='d', linestyle='-', color='brown', linewidth=2, label='AR Sports')

ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Rev (bn USD)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.legend()

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()