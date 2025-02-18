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

planting_data_t = np.array(planting_data).T

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

for i, color in enumerate(colors):
    if i == 0:
        bars = ax.bar(years, planting_data_t[:, i], color=color, edgecolor='black')
    else:
        bars = ax.bar(years, planting_data_t[:, i], bottom=np.sum(planting_data_t[:, :i], axis=1), color=color, edgecolor='black')

# Remove textual elements such as labels and title
ax.yaxis.grid(True, linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()