import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2022, 2024, 2026, 2028, 2030])

solar_efficiency = np.array([23, 30, 20, 18, 27, 25])
wind_efficiency = np.array([42, 38, 44, 34, 36, 40])
hydropower_efficiency = np.array([43, 41, 45, 40, 44, 42])

fig, ax = plt.subplots(figsize=(12, 8))

consistent_color = '#FF5733'
ax.plot(years, solar_efficiency, marker='x', linestyle='--', color=consistent_color, linewidth=1.5, label='Solar')
ax.plot(years, wind_efficiency, marker='v', linestyle='-', color=consistent_color, linewidth=2.5, label='Wind')
ax.plot(years, hydropower_efficiency, marker='d', linestyle=':', color=consistent_color, linewidth=1, label='Hydro')

for (year, sol_eff, win_eff, hyd_eff) in zip(years, solar_efficiency, wind_efficiency, hydropower_efficiency):
    ax.annotate(f'{sol_eff}%', (year, sol_eff), textcoords="offset points", xytext=(-5,10), ha='center')
    ax.annotate(f'{win_eff}%', (year, win_eff), textcoords="offset points", xytext=(-5,-20), ha='center')
    ax.annotate(f'{hyd_eff}%', (year, hyd_eff), textcoords="offset points", xytext=(-5,15), ha='center')

ax.grid(True, which='major', linestyle='-', linewidth=0.75, color='lightgray', alpha=0.9)

ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Eff. (%)', fontsize=12, fontweight='bold')
ax.set_title('Renewable Energy Efficiency\n(2020-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(years)
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()