import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_power = [5, 6, 8, 12, 15, 19, 25, 30, 40, 45, 50]
wind_energy = [10, 12, 15, 17, 21, 24, 28, 32, 37, 39, 42]
hydroelectric_power = [30, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41]

plt.figure(figsize=(12, 8))

# Updated colors for the plots
new_colors = ['#FF5733', '#33FF57', '#3357FF']

plt.plot(years, solar_power, marker='o', linestyle='-', color=new_colors[0], linewidth=2, label='Solar Power')
plt.plot(years, wind_energy, marker='^', linestyle='--', color=new_colors[1], linewidth=2, label='Wind Energy')
plt.plot(years, hydroelectric_power, marker='s', linestyle='-.', color=new_colors[2], linewidth=2, label='Hydroelectric Power')

annotations = {
    2012: ("Solar Surge\nTech Breakthrough", solar_power[2]),
    2016: ("Wind Energy\nMajor Project", wind_energy[6]),
    2020: ("Hydro\nEfficiency Boost", hydroelectric_power[10])
}

for year, (text, y_value) in annotations.items():
    plt.annotate(text, xy=(year, y_value), xytext=(year, y_value + 3),
                 arrowprops=dict(facecolor='gray', shrink=0.05, width=1, headwidth=5),
                 fontsize=9, color='black', ha='center')

plt.title('Growth of Renewable Energy Sources (2010-2020)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage Contribution (%)', fontsize=12)

plt.legend(title='Energy Source', loc='upper left', fontsize=10)
plt.xticks(years, rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()