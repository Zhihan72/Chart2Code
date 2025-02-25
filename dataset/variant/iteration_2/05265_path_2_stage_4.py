import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)
self_driving_cars = np.array([2, 9, 15, 0.5, 38, 54, 5, 75, 1, 3, 25])
road_accidents = np.array([30, 20, 35, 17, 32, 23, 26, 34, 37, 36, 35])

base_accidents = 37
accidents_reduction_percentage = ((base_accidents - road_accidents) / base_accidents) * 100

fig, ax1 = plt.subplots(figsize=(14, 8))

ax1.plot(years, self_driving_cars, marker='o', color='green', linewidth=2)
ax1.set_xticks(years)

ax2 = ax1.twinx()
ax2.plot(years, accidents_reduction_percentage, color='orange', linewidth=2)
ax2.tick_params(axis='y', colors='orange')

for milestone_year in [2012, 2016, 2018, 2020]:
    plt.axvline(x=milestone_year, color='grey', linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()