import numpy as np
import matplotlib.pyplot as plt

years = np.arange(2010, 2021)
road_accidents = np.array([35, 36, 37, 35, 34, 32, 30, 26, 23, 20, 17])

base_accidents = 37
accidents_reduction_percentage = ((base_accidents - road_accidents) / base_accidents) * 100

fig, ax1 = plt.subplots(figsize=(14, 8))

# Removed self_driving_cars plot and related annotations

ax1.set_title('Road Safety Accidents Reduction (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_xticks(years)

ax2 = ax1.twinx()

ax2.plot(years, accidents_reduction_percentage, 'purple', linewidth=2)
for (x, y) in zip(years, accidents_reduction_percentage):
    ax2.text(x, y - 2, f'{y:.1f}%', ha='center', va='top', fontsize=10, color='purple')

ax2.set_ylabel('Accidents Reduction (%)', fontsize=12, color='purple')
ax2.tick_params(axis='y', colors='purple')

plt.tight_layout()
plt.show()