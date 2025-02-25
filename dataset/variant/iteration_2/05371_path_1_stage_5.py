import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_capacity = [3, 7, 2, 15, 5, 36, 1, 28, 21, 10, 45]  
wind_capacity = [8, 30, 47, 68, 3, 38, 57, 12, 23, 5, 17]
hydro_capacity = [48, 18, 21, 35, 11, 41, 25, 13, 10, 30, 15]

colors = ['#4FC3F7', '#81C784', '#FFB74D']

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.25
indices = np.arange(len(years))

ax.barh(indices - bar_height, solar_capacity, bar_height, color=colors[2])
ax.barh(indices, wind_capacity, bar_height, color=colors[0])
ax.barh(indices + bar_height, hydro_capacity, bar_height, color=colors[1])

ax.set_yticks(indices)
ax.set_yticklabels(years)

plt.tight_layout()
plt.show()