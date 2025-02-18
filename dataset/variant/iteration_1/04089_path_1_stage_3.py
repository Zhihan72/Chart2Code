import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

nasa_missions = np.array([17, 15, 22, 16, 18, 16, 19, 21, 18, 15, 19])
spacex_missions = np.array([2, 3, 4, 1, 7, 5, 12, 10, 18, 22, 14])
esa_missions = np.array([11, 13, 10, 15, 12, 14, 13, 16, 15, 11, 14])
roscosmos_missions = np.array([13, 15, 12, 16, 14, 12, 14, 16, 15, 13, 14])

data = np.vstack([nasa_missions, spacex_missions, esa_missions, roscosmos_missions])

fig, ax = plt.subplots(figsize=(14, 9))

# Shuffled colors manually
colors = ['#d62728', '#1f77b4', '#ff7f0e', '#2ca02c']
agencies = ['NASA', 'SpaceX', 'ESA', 'ROS']

ax.stackplot(years, data, labels=agencies, colors=colors, alpha=0.8)

ax.annotate('Rise in SpaceX', xy=(2019, 18), xytext=(2016, 20),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, color='darkblue')

ax.set_title('Missions by Agency (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('# of Missions', fontsize=12)
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 71, 10))
ax.set_ylim(0, 70)

ax.legend(loc='upper left', fontsize=10, title='Agencies')

ax.grid(linestyle='--', alpha=0.5)

plt.xticks(rotation=45, ha='right')

plt.tight_layout()

plt.show()