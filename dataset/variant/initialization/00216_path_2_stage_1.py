import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2020, 2031)

solar_energy = [150, 170, 190, 220, 260, 310, 370, 440, 530, 640, 770]
wind_energy = [200, 215, 230, 260, 300, 350, 410, 490, 590, 710, 860]
hydro_energy = [180, 182, 185, 190, 195, 200, 205, 210, 215, 220, 225]

fossil_energy = [1200, 1180, 1160, 1120, 1100, 1050, 1000, 950, 900, 850, 800]
nuclear_energy = [450, 445, 440, 435, 430, 425, 420, 415, 410, 405, 400]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6), gridspec_kw={'width_ratios': [2, 1]})

ax1.plot(years, solar_energy, marker='o', linestyle='-', color='gold', linewidth=2, label='Solar')
ax1.plot(years, wind_energy, marker='s', linestyle='--', color='skyblue', linewidth=2, label='Wind')
ax1.plot(years, hydro_energy, marker='^', linestyle='-.', color='green', linewidth=2, label='Hydro')

ax1.annotate('Solar Up', xy=(2025, solar_energy[5]), xytext=(2022, 360),
             arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5), fontsize=9, ha='center')
ax1.annotate('Wind Break', xy=(2028, wind_energy[8]), xytext=(2025, 650),
             arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5), fontsize=9, ha='center')

ax1.set_title("Renewable Growth\nEurope (2020-30)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Production (GWh)", fontsize=12)
ax1.legend(title='Source', loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.5)

width = 0.4

ax2.bar(years - width / 2, fossil_energy, width, label='Fossil', color='gray', alpha=0.7)
ax2.bar(years - width / 2, nuclear_energy, width, bottom=fossil_energy, label='Nuclear', color='darkblue', alpha=0.7)

ax2.set_title("Non-Renewable Mix\nEurope (2020-30)", fontsize=12, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Production (GWh)", fontsize=12)
ax2.legend(title='Source', loc='upper right', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()