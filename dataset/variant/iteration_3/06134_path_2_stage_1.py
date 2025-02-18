import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

solar_energy = np.array([1, 2, 3, 4, 8, 15, 22, 30, 45, 60, 80, 100, 130, 150, 180, 220, 260, 300, 350, 400, 450])
wind_energy = np.array([2, 4, 7, 11, 17, 25, 35, 50, 70, 100, 135, 180, 220, 270, 320, 380, 440, 510, 590, 670, 750])
hydropower = np.array([100, 105, 110, 115, 120, 126, 132, 138, 145, 153, 160, 168, 177, 186, 195, 205, 215, 225, 236, 247, 260])
geothermal_energy = np.array([10, 11, 12, 14, 16, 18, 21, 25, 29, 34, 40, 46, 53, 61, 69, 78, 88, 99, 110, 122, 134])

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