import matplotlib.pyplot as plt
import numpy as np

years = np.array([2020, 2022, 2024, 2026, 2028, 2030])
solar_efficiency = np.array([18, 20, 23, 25, 27, 30])
wind_efficiency = np.array([34, 36, 38, 40, 42, 44])
hydropower_efficiency = np.array([40, 41, 42, 43, 44, 45])

fig, ax = plt.subplots(figsize=(12, 8))

# Randomized alterations to stylistic elements
ax.plot(years, solar_efficiency, marker='x', linestyle='--', color='#FF5733', linewidth=1.5, label='Solar Energy')
ax.plot(years, wind_efficiency, marker='v', linestyle='-', color='#33FFBD', linewidth=2.5, label='Wind Energy')
ax.plot(years, hydropower_efficiency, marker='d', linestyle=':', color='#335BFF', linewidth=1, label='Hydropower')

# Annotating data points with altered positions
for (year, sol_eff, win_eff, hyd_eff) in zip(years, solar_efficiency, wind_efficiency, hydropower_efficiency):
    ax.annotate(f'{sol_eff}%', (year, sol_eff), textcoords="offset points", xytext=(-5,10), ha='center')
    ax.annotate(f'{win_eff}%', (year, win_eff), textcoords="offset points", xytext=(-5,-20), ha='center')
    ax.annotate(f'{hyd_eff}%', (year, hyd_eff), textcoords="offset points", xytext=(-5,15), ha='center')

# Modifying grid appearance
ax.grid(True, which='major', linestyle='-', linewidth=0.75, color='lightgray', alpha=0.9)

# Altered legend location
ax.set_xlabel('Year', fontsize=12, fontweight='bold')
ax.set_ylabel('Efficiency (%)', fontsize=12, fontweight='bold')
ax.set_title('Technological Leap in Renewable Energy\nEfficiency (2020-2030)', fontsize=16, fontweight='bold', pad=20)
ax.set_xticks(years)
ax.legend(loc='upper left')

plt.tight_layout()
plt.show()