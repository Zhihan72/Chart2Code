import matplotlib.pyplot as plt
import numpy as np

years = ['2018', '2019', '2020', '2021', '2022']
planting_data = [
    [50, 60, 45, 70, 80],   # Oak
    [80, 90, 100, 85, 95],  # Pine
    [40, 50, 55, 65, 70],   # Maple
    [30, 45, 60, 40, 50],   # Birch
    [20, 25, 30, 35, 45],   # Cherry
    [25, 30, 35, 40, 50],   # Willow
    [30, 35, 40, 45, 55]    # Cedar
]

# Transpose the dataset
planting_data_t = np.array(planting_data).T

# Colors for each set of bars
colors = [
    (0.267004, 0.004874, 0.329415, 1.0),
    (0.127568, 0.566949, 0.550556, 1.0),
    (0.993248, 0.906157, 0.143936, 1.0),
    (0.229739, 0.322361, 0.545706, 1.0),
    (0.369214, 0.788888, 0.382914, 1.0),
    (0.993248, 0.906157, 0.143936, 1.0),
    (0.039215, 0.749756, 0.189921, 1.0)
]

fig, ax = plt.subplots(figsize=(12, 8))

# Calculating midpoint to split the data
midpoint = len(planting_data_t[0]) // 2

# Plot bars for positive values (right side of the axis)
for i, color in enumerate(colors[:midpoint]):
    if i == 0:
        ax.bar(years, planting_data_t[:, i], color=color)
    else:
        ax.bar(years, planting_data_t[:, i], bottom=np.sum(planting_data_t[:, :i], axis=1), color=color)

# Plot bars for negative values (left side of the axis)
for i, color in enumerate(colors[midpoint:], start=midpoint):
    if i == midpoint:
        ax.bar(years, -planting_data_t[:, i], color=color)
    else:
        ax.bar(years, -planting_data_t[:, i], bottom=-np.sum(planting_data_t[:, midpoint:i], axis=1), color=color)

ax.yaxis.grid(False)
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.spines['bottom'].set_visible(False)

ax.set_ylabel('Number of Trees')
ax.axhline(0, color='black', linewidth=0.8)

plt.tight_layout()
plt.show()