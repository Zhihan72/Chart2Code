import matplotlib.pyplot as plt
import numpy as np

years = np.array([2018, 2019, 2020, 2021, 2022])
city_zephyr = np.array([500, 550, 600, 650, 700])
city_aerios = np.array([400, 450, 470, 490, 520])

fig, ax = plt.subplots(figsize=(12, 7))

# Using the same color for all data groups
ax.plot(years, city_zephyr, marker='o', linestyle='-', color='dodgerblue')
ax.plot(years, city_aerios, marker='s', linestyle='-', color='dodgerblue')

ax.set_xticks(years)

plt.tight_layout()

plt.show()