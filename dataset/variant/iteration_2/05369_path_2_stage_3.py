import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

asia = [50, 65, 95, 70, 45, 80, 170, 110, 58, 150, 130]
europe = [40, 35, 120, 55, 95, 65, 107, 85, 30, 48, 75]
north_america = [44, 125, 25, 60, 28, 82, 35, 110, 95, 70, 50]
oceania = [7, 30, 10, 5, 40, 15, 45, 55, 20, 25, 35]

plt.figure(figsize=(14, 8))

plt.plot(years, asia, marker='o', linestyle='-', color='red', label='Asia', linewidth=2)
plt.plot(years, europe, marker='s', linestyle='--', color='cyan', label='Europe', linewidth=2)
plt.plot(years, north_america, marker='^', linestyle='-.', color='brown', label='N. America', linewidth=2)
plt.plot(years, oceania, marker='D', linestyle=':', color='magenta', label='Oceania', linewidth=2)

plt.title("Solar Growth 2010-2020", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Gen. (GW)", fontsize=14)
plt.xticks(years, rotation=45, fontsize=10)
plt.yticks(np.arange(0, 201, 20), fontsize=10)
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend(title='Region', loc='upper left', fontsize=12)

for region, data, color in zip(['Asia', 'Europe', 'N. America', 'Oceania'],
                               [asia, europe, north_america, oceania],
                               ['red', 'cyan', 'brown', 'magenta']):
    max_gen = max(data)
    max_year = years[data.index(max_gen)]
    plt.annotate(f'Peak: {max_gen}', xy=(max_year, max_gen),
                 xytext=(max_year - 0.5, max_gen + 5),
                 arrowprops=dict(facecolor=color, arrowstyle='->'),
                 fontsize=10, color=color)

plt.tight_layout()
plt.show()