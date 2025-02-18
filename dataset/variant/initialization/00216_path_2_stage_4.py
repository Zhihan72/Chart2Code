import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

solar_energy = [150, 170, 190, 220, 260, 310, 370, 440, 530, 640, 770]
wind_energy = [200, 215, 230, 260, 300, 350, 410, 490, 590, 710, 860]
hydro_energy = [180, 182, 185, 190, 195, 200, 205, 210, 215, 220, 225]
geothermal_energy = [50, 55, 60, 70, 85, 105, 130, 160, 195, 235, 280]  # new data series

fossil_energy = [1200, 1180, 1160, 1120, 1100, 1050, 1000, 950, 900, 850, 800]
nuclear_energy = [450, 445, 440, 435, 430, 425, 420, 415, 410, 405, 400]
renewable_energy = [380, 400, 435, 495, 570, 665, 780, 920, 1110, 1300, 1535]  # collective renewable data

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})

width = 0.4

ax1.bar(years - width / 2, fossil_energy, width, label='Fossil', color='dimgray', alpha=0.6)
ax1.bar(years - width / 2, nuclear_energy, width, bottom=fossil_energy, label='Nuclear', color='navy', alpha=0.8)
ax1.bar(years - width / 2, renewable_energy, width, bottom=np.array(fossil_energy) + np.array(nuclear_energy),
        label='Renewable', color='coral', alpha=0.7)  # new data series

ax1.set_title("Non-Renewable Mix\nEurope (2020-30)", fontsize=13, fontweight='normal', fontstyle='italic')
ax1.set_xlabel("Year", fontsize=11)
ax1.set_ylabel("Production (GWh)", fontsize=11)
ax1.legend(title='Sources', loc='upper left', fontsize=9)
ax1.grid(True, linestyle='-', alpha=0.3)

ax2.plot(years, solar_energy, marker='*', linestyle=':', color='goldenrod', linewidth=2.5, label='Solar')
ax2.plot(years, wind_energy, marker='D', linestyle='-', color='deepskyblue', linewidth=1.5, label='Wind')
ax2.plot(years, hydro_energy, marker='p', linestyle='--', color='forestgreen', linewidth=2, label='Hydro')
ax2.plot(years, geothermal_energy, marker='o', linestyle='-.', color='purple', linewidth=2, label='Geothermal')  # new data series

ax2.annotate('Solar Up', xy=(2025, solar_energy[5]), xytext=(2022, 360),
             arrowprops=dict(facecolor='red', arrowstyle='wedge,tail_width=0.5', linewidth=1.5), fontsize=8, ha='center')
ax2.annotate('Wind Break', xy=(2028, wind_energy[8]), xytext=(2025, 650),
             arrowprops=dict(facecolor='orange', arrowstyle='fancy', linewidth=1.5), fontsize=8, ha='center')

ax2.set_title("Renewable Growth\nEurope (2020-30)", fontsize=13, fontweight='normal', fontstyle='italic')
ax2.set_xlabel("Year", fontsize=11)
ax2.set_ylabel("Production (GWh)", fontsize=11)
ax2.legend(title='Sources', loc='lower right', fontsize=9)
ax2.grid(True, linestyle=':', alpha=0.3)

plt.tight_layout()
plt.show()