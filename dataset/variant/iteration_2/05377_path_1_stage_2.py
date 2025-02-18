import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

esports_revenue = np.array([0.5, 0.7, 1.0, 1.4, 1.9, 2.4, 3.0, 3.8, 4.7, 5.8, 7.0])
robot_combat_revenue = np.array([0.3, 0.5, 0.6, 0.8, 1.1, 1.5, 1.9, 2.4, 3.0, 3.7, 4.5])
drone_racing_revenue = np.array([0.1, 0.2, 0.4, 0.6, 0.9, 1.3, 1.8, 2.5, 3.3, 4.2, 5.2])
ar_sports_revenue = np.array([0.2, 0.3, 0.5, 0.7, 1.0, 1.4, 1.9, 2.3, 2.9, 3.5, 4.1])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, esports_revenue, marker='o', linestyle='-', color='red', linewidth=2)
ax.plot(years, robot_combat_revenue, marker='^', linestyle='-', color='blue', linewidth=2)
ax.plot(years, drone_racing_revenue, marker='s', linestyle='-', color='green', linewidth=2)
ax.plot(years, ar_sports_revenue, marker='d', linestyle='-', color='purple', linewidth=2)

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Revenue (billion USD)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()