import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

solar_energy =    np.array([1, 260, 3, 8, 15, 22, 30, 150, 45, 60, 80, 100, 130, 4, 180, 220, 2, 300, 350, 400, 450])
wind_energy =     np.array([4, 440, 11, 7, 17, 25, 35, 270, 70, 100, 135, 180, 220, 320, 320, 50, 670, 510, 590, 380, 750])
hydropower =      np.array([100, 145, 110, 115, 120, 215, 132, 138, 105, 195, 205, 168, 177, 186, 195, 205, 215, 153, 236, 247, 160])
geothermal_energy = np.array([10, 11, 88, 14, 16, 18, 21, 25, 29, 134, 40, 46, 53, 69, 29, 88, 78, 99, 110, 122, 61])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar_energy, label='Solar Power', color='orange', linestyle=':', marker='*', linewidth=1.5)
ax.plot(years, wind_energy, label='Wind Energy', color='blue', linestyle='-', marker='x', linewidth=2)
ax.plot(years, hydropower, label='Hydropower', color='green', linestyle='--', marker='1', linewidth=1)
ax.plot(years, geothermal_energy, label='Geothermal Energy', color='red', linestyle='-.', marker='v', linewidth=2)

ax.set_title("Clean Energy Growth (2000-2020)", fontsize=14, weight='bold', pad=15)
ax.set_xlabel("Years", fontsize=11)
ax.set_ylabel("Energy Output (TWh)", fontsize=11)

ax.grid(True, linestyle=':', alpha=0.4)

important_events = {
    2008: 'Economic Focus Shift',
    2015: 'Climate Accord',
    2020: 'Peak Surge'
}

for year, event in important_events.items():
    plt.annotate(event, (year, solar_energy[year-2000]), textcoords="offset points", xytext=(-30,15), ha='center', fontsize=9, 
                 arrowprops=dict(facecolor='gray', arrowstyle='->', linewidth=1.2))

ax.legend(loc='lower right', fontsize=9)

plt.tight_layout()

plt.show()