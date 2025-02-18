import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2022, 2024, 2026, 2028, 2030])
solar_efficiency = np.array([18, 20, 23, 25, 27, 30])
wind_efficiency = np.array([34, 36, 38, 40, 42, 44])
hydropower_efficiency = np.array([40, 41, 42, 43, 44, 45])

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, solar_efficiency, marker='o', linestyle='-', color='#FF5733', linewidth=2, label='Solar')
ax.plot(years, wind_efficiency, marker='s', linestyle='--', color='#33FFBD', linewidth=2, label='Wind')
ax.plot(years, hydropower_efficiency, marker='^', linestyle='-.', color='#335BFF', linewidth=2, label='Hydro')

for (year, sol_eff, win_eff, hyd_eff) in zip(years, solar_efficiency, wind_efficiency, hydropower_efficiency):
    ax.annotate(f'{sol_eff}%', (year, sol_eff), textcoords="offset points", xytext=(-10,10), ha='center')
    ax.annotate(f'{win_eff}%', (year, win_eff), textcoords="offset points", xytext=(-10,-15), ha='center')
    ax.annotate(f'{hyd_eff}%', (year, hyd_eff), textcoords="offset points", xytext=(-10,15), ha='center')

ax.grid(True, which='both', linestyle='--', linewidth=0.5, color='gray', alpha=0.7)

ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Eff. (%)', fontsize=12, fontweight='bold')
ax.set_title('Renewables Efficiency\n(2020-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(years)
ax.legend(loc='lower right')

plt.tight_layout()
plt.show()