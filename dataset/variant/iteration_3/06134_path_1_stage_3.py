import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

solar_energy =    np.array([1, 260, 3, 8, 15, 22, 30, 150, 45, 60, 80, 100, 130, 4, 180, 220, 2, 300, 350, 400, 450])
wind_energy =     np.array([4, 440, 11, 7, 17, 25, 35, 270, 70, 100, 135, 180, 220, 320, 320, 50, 670, 510, 590, 380, 750])
hydropower =      np.array([100, 145, 110, 115, 120, 215, 132, 138, 105, 195, 205, 168, 177, 186, 195, 205, 215, 153, 236, 247, 160])
geothermal_energy = np.array([10, 11, 88, 14, 16, 18, 21, 25, 29, 134, 40, 46, 53, 69, 29, 88, 78, 99, 110, 122, 61])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar_energy, label='Sun Power', color='purple', linestyle='-', marker='o', linewidth=2)
ax.plot(years, wind_energy, label='Breeze Force', color='cyan', linestyle='--', marker='s', linewidth=2)
ax.plot(years, hydropower, label='Water Flow Energy', color='lime', linestyle='-.', marker='^', linewidth=2)
ax.plot(years, geothermal_energy, label='Earth Heat', color='magenta', linestyle=':', marker='d', linewidth=2)

ax.set_title("Rise in Clean Energy (2000-2020):\nEnergy Output from Sun, Wind, Water, and Earth Sources", 
             fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Chronological Years", fontsize=12)
ax.set_ylabel("Energy Output (TWh)", fontsize=12)

ax.grid(True, linestyle='--', alpha=0.5)

important_events = {
    2008: 'Crucial Economic Shift\nRenewable Focus',
    2015: 'Climate Pact Milestone',
    2020: 'Renewable Surge'
}

for year, event in important_events.items():
    plt.annotate(event, (year, solar_energy[year-2000]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, 
                 arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5))

ax.legend(loc='upper left', fontsize=10)

plt.tight_layout()

plt.show()