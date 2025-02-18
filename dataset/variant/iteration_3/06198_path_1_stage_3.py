import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = np.array([12, 18, 45, 78, 140, 230, 410, 610, 790, 930, 980])
wind_energy = np.array([18, 28, 55, 85, 135, 210, 330, 460, 590, 730, 880])

fig, ax1 = plt.subplots(figsize=(14, 5))

bar_width = 0.35
bar1 = ax1.bar(years - bar_width/2, solar_energy, bar_width, label='Solar Energy (GWh)', color='darkorange', alpha=0.8, hatch='/')
bar2 = ax1.bar(years + bar_width/2, wind_energy, bar_width, label='Wind Energy (GWh)', color='royalblue', alpha=0.8, hatch='\\')

for bar in bar1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height + 20, f'{height}', ha='center', va='bottom', fontsize=9, color='darkred')
for bar in bar2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height + 20, f'{height}', ha='center', va='bottom', fontsize=9, color='navy')

ax1.set_title("Growth in Renewable Energy Production (2010-2020)", fontsize=18, fontweight='bold', color='darkgreen')
ax1.set_xlabel("Year", fontsize=14, color='brown')
ax1.set_ylabel("Energy Production (GWh)", fontsize=14, color='brown')

ax1.legend(loc='lower right', fontsize=11, shadow=True)
ax1.grid(False)

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()