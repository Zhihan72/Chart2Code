import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define data
years = np.arange(2010, 2021)
cities = ['NY', 'LDN', 'TKY']  # Removed 'SYD'
initiatives = ['S. Grids', 'I. Trans.', 'D. Gov.', 'G. Bldg.']

ny_budgets = np.array([
    [50, 40, 30, 20], [52, 42, 35, 25], [54, 45, 38, 28], [57, 47, 40, 32],
    [60, 50, 43, 35], [63, 53, 46, 38], [65, 55, 50, 40], [68, 58, 52, 42],
    [70, 60, 54, 44], [72, 63, 57, 47], [75, 65, 60, 50]
])
ldn_budgets = np.array([
    [45, 35, 25, 15], [48, 37, 28, 18], [50, 40, 30, 20], [52, 43, 32, 23],
    [55, 45, 35, 25], [57, 48, 38, 27], [60, 50, 40, 30], [63, 53, 42, 32],
    [65, 55, 45, 34], [67, 58, 47, 37], [70, 60, 50, 40]
])
tky_budgets = np.array([
    [40, 30, 20, 10], [42, 32, 22, 13], [45, 34, 25, 15], [47, 37, 28, 18],
    [50, 40, 30, 20], [53, 42, 32, 23], [55, 45, 35, 25], [57, 48, 37, 28],
    [60, 50, 40, 30], [62, 52, 43, 33], [65, 55, 45, 35]
])

# Combine budgets without 'SYD'
budgets = [ny_budgets, ldn_budgets, tky_budgets]
colors = ['#32CD32', '#FFD700', '#FF6347', '#4682B4']

# Initialize plot
fig = plt.figure(figsize=(14, 9))
ax = fig.add_subplot(111, projection='3d')

# Adjust view angle
ax.view_init(elev=30, azim=120)

# Plot data
for c_idx, city in enumerate(cities):
    x = np.array([c_idx] * len(years))
    y = years
    for i_idx, initiative in enumerate(initiatives):
        z = np.zeros_like(years) if i_idx == 0 else np.sum(budgets[c_idx][:, :i_idx], axis=1)
        dz = budgets[c_idx][:, i_idx]
        ax.bar3d(x, y, z, 0.4, 0.8, dz, color=colors[i_idx], alpha=0.9)

# Customize axes
ax.set_title('Smart City Budgets (2010-2020)', fontsize=14, pad=20)
ax.set_xlabel('City', fontsize=12, labelpad=10)
ax.set_ylabel('Year', fontsize=12, labelpad=10)
ax.set_zlabel('Budget (M USD)', fontsize=12, labelpad=10)

ax.set_xticks(np.arange(len(cities)))
ax.set_xticklabels(cities, fontsize=10, rotation=20)
ax.set_yticks(years)
ax.set_yticklabels(years, fontsize=9)

# Remove pane colors
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Improve layout
plt.tight_layout()

# Show plot
plt.show()