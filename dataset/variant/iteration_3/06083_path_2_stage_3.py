import matplotlib.pyplot as plt
import numpy as np

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# Altered temperature data while keeping the same dimension
temperatures_ny = [32, 30, 29, 35, 31, 33, 30]  # Shuffled values
temperatures_la = [57, 61, 55, 63, 58, 56, 60]  # Shuffled values
temperatures_chicago = [21, 19, 24, 22, 25, 22, 20]  # Shuffled values

fig, ax = plt.subplots(figsize=(12, 8))

# Color remains unchanged
color = 'purple'

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