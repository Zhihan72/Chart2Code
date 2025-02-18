import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
temperatures_ny = [30, 32, 35, 33, 30, 31, 29]
temperatures_la = [55, 57, 56, 58, 60, 61, 63]
temperatures_chicago = [20, 22, 25, 24, 22, 21, 19]

fig, ax = plt.subplots(figsize=(12, 8))

# Use a single color for all data groups
color = 'purple' # The selected consistent color

ax.plot(days, temperatures_ny, marker='o', linestyle='-', color=color, linewidth=2, markersize=6)
ax.plot(days, temperatures_la, marker='s', linestyle='--', color=color, linewidth=2, markersize=6)
ax.plot(days, temperatures_chicago, marker='^', linestyle='-.', color=color, linewidth=2, markersize=6)

for i in range(len(days)):
    ax.text(i, temperatures_ny[i] + 1, f'{temperatures_ny[i]}°F', ha='center', va='bottom', fontsize=10, color=color)
    ax.text(i, temperatures_la[i] + 1, f'{temperatures_la[i]}°F', ha='center', va='bottom', fontsize=10, color=color)
    ax.text(i, temperatures_chicago[i] + 1, f'{temperatures_chicago[i]}°F', ha='center', va='bottom', fontsize=10, color=color)

ax.set_title('Average Daily Temperatures in a Week\nfor New York, Los Angeles, and Chicago', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Days of the Week', fontsize=14)
ax.set_ylabel('Temperature (°F)', fontsize=14)

ax.set_xticks(np.arange(len(days)))
ax.set_xticklabels(days, fontsize=12, rotation=30, ha='right')

plt.tight_layout()
plt.show()