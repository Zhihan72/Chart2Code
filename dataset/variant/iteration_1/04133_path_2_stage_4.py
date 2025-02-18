import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022, 2024, 2026])

# Randomly altered the content within certain data groups while preserving the dimensional structure
new_york_green_spaces = np.array([32, 30, 38, 35, 42, 60, 46, 55, 51])
tokyo_green_spaces = np.array([27, 25, 32, 29, 35, 52, 39, 47, 43])
berlin_green_spaces = np.array([23, 20, 30, 26, 34, 50, 38, 47, 42])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, new_york_green_spaces, marker='o', linestyle='-', color='purple', linewidth=2)
ax.plot(years, tokyo_green_spaces, marker='s', linestyle='--', color='orange', linewidth=2)
ax.plot(years, berlin_green_spaces, marker='^', linestyle='-.', color='cyan', linewidth=2)

plt.tight_layout()
plt.show()