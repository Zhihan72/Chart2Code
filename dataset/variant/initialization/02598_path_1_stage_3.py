import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2022, 2024, 2026, 2028, 2030])

# Randomly altered efficiencies while preserving dimensionality
solar_efficiency = np.array([23, 30, 20, 18, 27, 25])  # shuffled
wind_efficiency = np.array([42, 38, 44, 34, 36, 40])  # shuffled
hydropower_efficiency = np.array([43, 41, 45, 40, 44, 42])  # shuffled

fig, ax = plt.subplots(figsize=(12, 8))

consistent_color = '#FF5733'
ax.plot(years, solar_efficiency, marker='x', linestyle='--', color=consistent_color, linewidth=1.5, label='Solar Energy')
ax.plot(years, wind_efficiency, marker='v', linestyle='-', color=consistent_color, linewidth=2.5, label='Wind Energy')
ax.plot(years, hydropower_efficiency, marker='d', linestyle=':', color=consistent_color, linewidth=1, label='Hydropower')

for (year, sol_eff, win_eff, hyd_eff) in zip(years, solar_efficiency, wind_efficiency, hydropower_efficiency):
    ax.annotate(f'{sol_eff}%', (year, sol_eff), textcoords="offset points", xytext=(-5,10), ha='center')
    ax.annotate(f'{win_eff}%', (year, win_eff), textcoords="offset points", xytext=(-5,-20), ha='center')
    ax.annotate(f'{hyd_eff}%', (year, hyd_eff), textcoords="offset points", xytext=(-5,15), ha='center')

ax.grid(True, which='major', linestyle='-', linewidth=0.75, color='lightgray', alpha=0.9)

ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Efficiency (%)', fontsize=12, fontweight='bold')
ax.set_title('Technological Leap in Renewable Energy\nEfficiency (2020-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(years)
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()