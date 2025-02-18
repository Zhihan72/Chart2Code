import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)
self_driving_cars = np.array([0.5, 1, 2, 3, 5, 9, 15, 25, 38, 54, 75])
road_accidents = np.array([35, 36, 37, 35, 34, 32, 30, 26, 23, 20, 17])

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