import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)

# Altered revenue data for different sports leagues in billion USD
esports_revenue = np.array([0.5, 0.7, 1.2, 1.0, 2.0, 1.9, 2.7, 3.9, 4.5, 5.7, 6.5])
robot_combat_revenue = np.array([0.4, 0.3, 0.7, 0.9, 1.0, 1.4, 1.6, 2.5, 2.9, 3.8, 4.9])
drone_racing_revenue = np.array([0.2, 0.1, 0.3, 0.7, 0.8, 1.2, 1.9, 2.3, 3.2, 4.1, 5.0])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(years, esports_revenue, marker='o', linestyle='-', color='purple', linewidth=2)
ax.plot(years, robot_combat_revenue, marker='^', linestyle='-', color='orange', linewidth=2)
ax.plot(years, drone_racing_revenue, marker='s', linestyle='-', color='cyan', linewidth=2)

ax.set_title('Growth of Non-Traditional Sports Leagues\nRevenue from 2010 to 2020', fontsize=16, fontweight='bold')
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Revenue (billion USD)', fontsize=12)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)

ax.annotate('Exponential Growth',
            xy=(2015, 1.9), xytext=(2013.5, 5),
            arrowprops=dict(facecolor='purple', arrowstyle='->'), fontsize=11, color='indigo')

ax.annotate('Rising Popularity',
            xy=(2018, 2.5), xytext=(2016, 3), 
            arrowprops=dict(facecolor='orange', arrowstyle='->'), fontsize=11, color='darkorange')

plt.tight_layout()
plt.show()