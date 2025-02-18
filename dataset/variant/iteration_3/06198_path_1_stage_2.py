import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = np.array([12, 18, 45, 78, 140, 230, 410, 610, 790, 930, 980])
wind_energy = np.array([18, 28, 55, 85, 135, 210, 330, 460, 590, 730, 880])

fig, ax1 = plt.subplots(figsize=(14, 5))

bar_width = 0.35
bar1 = ax1.bar(years - bar_width/2, solar_energy, bar_width, label='Solar Energy (GWh)', color='goldenrod', alpha=0.7)
bar2 = ax1.bar(years + bar_width/2, wind_energy, bar_width, label='Wind Energy (GWh)', color='steelblue', alpha=0.7)

for bar in bar1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height}', ha='center', va='bottom')
for bar in bar2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height}', ha='center', va='bottom')

ax1.set_title("Growth in Renewable Energy Production (2010-2020)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Energy Production (GWh)", fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()