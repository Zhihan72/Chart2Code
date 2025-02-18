import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2022, 2024, 2026, 2028, 2030])
solar_efficiency = np.array([23, 18, 30, 25, 27, 20])
wind_efficiency = np.array([38, 34, 42, 36, 40, 44])
hydropower_efficiency = np.array([42, 41, 45, 43, 44, 40])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, solar_efficiency, marker='o', linestyle='-', color='#D7263D', linewidth=2)
ax.plot(years, wind_efficiency, marker='s', linestyle='--', color='#1F77B4', linewidth=2)
ax.plot(years, hydropower_efficiency, marker='^', linestyle='-.', color='#2CA02C', linewidth=2)

for (year, sol_eff, win_eff, hyd_eff) in zip(years, solar_efficiency, wind_efficiency, hydropower_efficiency):
    ax.annotate(f'{sol_eff}%', (year, sol_eff), textcoords="offset points", xytext=(-10,10), ha='center')
    ax.annotate(f'{win_eff}%', (year, win_eff), textcoords="offset points", xytext=(-10,-15), ha='center')
    ax.annotate(f'{hyd_eff}%', (year, hyd_eff), textcoords="offset points", xytext=(-10,15), ha='center')

ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Eff. (%)', fontsize=12, fontweight='bold')
ax.set_title('Renewables Efficiency\n(2020-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(years)

plt.tight_layout()
plt.show()