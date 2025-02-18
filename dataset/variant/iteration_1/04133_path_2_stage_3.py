import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2026])
new_york_green_spaces = np.array([30, 32, 35, 38, 42, 46, 51, 55, 60])
tokyo_green_spaces = np.array([25, 27, 29, 32, 35, 39, 43, 47, 52])
berlin_green_spaces = np.array([20, 23, 26, 30, 34, 38, 42, 47, 50])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, new_york_green_spaces, marker='o', linestyle='-', color='purple', linewidth=2)
ax.plot(years, tokyo_green_spaces, marker='s', linestyle='--', color='orange', linewidth=2)
ax.plot(years, berlin_green_spaces, marker='^', linestyle='-.', color='cyan', linewidth=2)

plt.tight_layout()
plt.show()