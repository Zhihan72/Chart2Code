import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

solar_energy = np.array([15, 22, 3, 8, 1, 300, 350, 260, 80, 150, 100, 45, 260, 30, 4, 130, 220, 2, 400, 450, 180])
wind_energy = np.array([180, 7, 11, 50, 440, 70, 270, 25, 4, 100, 135, 670, 35, 17, 750, 2, 220, 510, 590, 380, 320])
hydropower = np.array([145, 132, 115, 100, 110, 160, 260, 138, 186, 153, 168, 105, 215, 205, 120, 195, 177, 247, 225, 126, 236])
geothermal_energy = np.array([134, 110, 99, 14, 29, 12, 40, 16, 11, 25, 69, 61, 21, 78, 88, 122, 46, 10, 34, 53, 18])

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar_energy, label='Solar', color='orange', linestyle='-', marker='o', linewidth=2)
ax.plot(years, wind_energy, label='Wind', color='blue', linestyle='--', marker='s', linewidth=2)
ax.plot(years, hydropower, label='Hydro', color='green', linestyle='-.', marker='^', linewidth=2)
ax.plot(years, geothermal_energy, label='Geo', color='red', linestyle=':', marker='d', linewidth=2)

ax.set_title("Renewable Energy Growth (2000-2020)", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Gen. (TWh)", fontsize=12)

ax.grid(True, linestyle='--', alpha=0.5)

significant_years = {
    2008: 'Financial Crisis',
    2015: 'Paris Agreement',
    2020: 'Peak Adoption'
}

for year, event in significant_years.items():
    plt.annotate(event, (year, solar_energy[year-2000]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=10, arrowprops=dict(facecolor='black', arrowstyle='->', linewidth=1.5))

ax.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()