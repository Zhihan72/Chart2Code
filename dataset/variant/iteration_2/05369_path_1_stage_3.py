import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
asia = [45, 50, 58, 65, 70, 80, 95, 110, 130, 150, 170]
europe = [30, 35, 40, 48, 55, 65, 75, 85, 95, 107, 120]
north_america = [25, 28, 35, 44, 50, 60, 70, 82, 95, 110, 125]

plt.figure(figsize=(14, 8))

plt.plot(years, asia, marker='x', linestyle='-.', color='red', label='Asia', linewidth=2)
plt.plot(years, europe, marker='d', linestyle='-', color='cyan', label='Europe', linewidth=2)
plt.plot(years, north_america, marker='v', linestyle=':', color='magenta', label='North America', linewidth=2)

plt.title("Decade of Solar Energy Generation Growth\n(2010-2020)", fontsize=18, fontweight='bold', pad=20)
plt.xlabel("Year", fontsize=14)
plt.ylabel("Solar Generation (Gigawatts)", fontsize=14)
plt.xticks(years, rotation=45, fontsize=10)
plt.yticks(np.arange(0, 201, 20), fontsize=10)
plt.grid(True, linestyle=':', linewidth=1, alpha=0.9)
plt.legend(title='Regions', loc='lower right', fontsize=12, shadow=True)

for region, data, color in zip(['Asia', 'Europe', 'North America'],
                               [asia, europe, north_america],
                               ['red', 'cyan', 'magenta']):
    max_gen = max(data)
    max_year = years[data.index(max_gen)]
    plt.annotate(f'Peak: {max_gen} GW', xy=(max_year, max_gen),
                 xytext=(max_year - 0.5, max_gen + 5),
                 arrowprops=dict(facecolor=color, arrowstyle='->'),
                 fontsize=10, color=color)

plt.tight_layout()
plt.show()