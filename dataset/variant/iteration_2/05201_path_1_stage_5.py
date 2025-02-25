import matplotlib.pyplot as plt
import numpy as np

days = np.arange(1, 366)
months = np.arange(1, 13)

high_temps = np.concatenate([
    np.linspace(0, 20, 90),
    np.linspace(20, 25, 61),
    np.linspace(25, 30, 92),
    np.linspace(30, 20, 61),
    np.linspace(20, 10, 61)
])

rainfall = np.array([50, 40, 55, 70, 100, 150, 200, 180, 120, 90, 60, 55])

fig, ax = plt.subplots(1, 2, figsize=(12, 6), dpi=100)

# Randomized stylistic changes
ax[0].plot(days, high_temps, label='Max Temp', color='orange', linestyle='--', marker='o', markersize=3)

ax[0].set_title('2023 Temp Trends in A. City', fontsize=16, fontweight='bold')
ax[0].set_xlabel('Day of the Year', fontsize=12)
ax[0].set_ylabel('Temperature (°C)', fontsize=12)
ax[0].legend(loc='lower right')
ax[0].grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax[1].bar(months, rainfall, color='coral', edgecolor='grey', hatch='/')

ax[1].set_title('2023 Monthly Rainfall in A. City', fontsize=16, fontweight='bold')
ax[1].set_xlabel('Month', fontsize=12)
ax[1].set_ylabel('Rainfall (mm)', fontsize=12)
ax[1].set_xticks(months)
ax[1].set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax[1].grid(False)

plt.tight_layout()
plt.show()