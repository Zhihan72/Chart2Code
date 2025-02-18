import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_power = [5, 6, 8, 12, 15, 19, 25, 30, 40, 45, 50]
wind_energy = [10, 12, 15, 17, 21, 24, 28, 32, 37, 39, 42]
hydroelectric_power = [30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]

plt.figure(figsize=(12, 8))

# Updated styles for varied appearance
plt.plot(years, solar_power, marker='D', linestyle=':', color='#FFA07A', linewidth=1.5, label='Solar Power')
plt.plot(years, wind_energy, marker='p', linestyle='-', color='#6495ED', linewidth=2.5, label='Wind Energy')
plt.plot(years, hydroelectric_power, marker='*', linestyle='--', color='#90EE90', linewidth=1, label='Hydroelectric Power')

annotations = {
    2012: ("Solar Surge\nTech Breakthrough", solar_power[2]),
    2016: ("Wind Energy\nMajor Project", wind_energy[6]),
    2020: ("Hydro\nEfficiency Boost", hydroelectric_power[10])
}

for year, (text, y_value) in annotations.items():
    plt.annotate(text, xy=(year, y_value), xytext=(year, y_value + 3),
                 arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5),
                 fontsize=9, color='black', ha='center')

plt.title('Growth of Renewable Energy Sources (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage Contribution (%)', fontsize=12)
plt.legend(title='Energy Source', loc='lower right', fontsize=10)
plt.xticks(years, rotation=45)
plt.grid(True, linestyle='-', alpha=0.3)
plt.tight_layout()
plt.show()