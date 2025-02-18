import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_capacity = [1, 2, 3, 5, 7, 10, 15, 21, 28, 36, 45]
wind_capacity = [3, 5, 8, 12, 17, 23, 30, 38, 47, 57, 68]
hydro_capacity = [10, 11, 13, 15, 18, 21, 25, 30, 35, 41, 48]

colors = ['#4FC3F7', '#81C784', '#FFB74D']

fig, ax = plt.subplots(figsize=(12, 8))

bar_height = 0.25
indices = np.arange(len(years))

ax.barh(indices - bar_height, solar_capacity, bar_height, color=colors[2], edgecolor='black')
ax.barh(indices, wind_capacity, bar_height, color=colors[0], edgecolor='black')
ax.barh(indices + bar_height, hydro_capacity, bar_height, color=colors[1], edgecolor='black')

ax.set_yticks(indices)
ax.set_yticklabels(years)

plt.tight_layout()
plt.show()