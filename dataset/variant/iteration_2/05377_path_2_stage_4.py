import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

esports_revenue = np.array([0.5, 0.7, 1.2, 1.0, 2.0, 1.9, 2.7, 3.9, 4.5, 5.7, 6.5])
robot_combat_revenue = np.array([0.4, 0.3, 0.7, 0.9, 1.0, 1.4, 1.6, 2.5, 2.9, 3.8, 4.9])
drone_racing_revenue = np.array([0.2, 0.1, 0.3, 0.7, 0.8, 1.2, 1.9, 2.3, 3.2, 4.1, 5.0])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, esports_revenue, marker='o', linestyle='-', color='purple', linewidth=2)
ax.plot(years, robot_combat_revenue, marker='^', linestyle='-', color='orange', linewidth=2)
ax.plot(years, drone_racing_revenue, marker='s', linestyle='-', color='cyan', linewidth=2)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

plt.tight_layout()
plt.show()