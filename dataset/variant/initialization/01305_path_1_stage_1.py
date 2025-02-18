import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Existing data series for energy adoption rates
solar_adoption = [2, 3, 5, 7, 10, 14, 18, 25, 30, 35, 40]
wind_adoption = [10, 11, 13, 15, 17, 19, 21, 24, 26, 28, 30]
hydro_adoption = [30, 31, 31, 32, 33, 33, 34, 35, 35, 36, 36]

# New data series for Geothermal Energy
geothermal_adoption = [4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20]

plt.figure(figsize=(12, 6))

plt.plot(years, solar_adoption, label='Solar Energy', color='gold', linestyle='--', marker='o', linewidth=2)
plt.plot(years, wind_adoption, label='Wind Energy', color='skyblue', linestyle='-', marker='s', linewidth=2)
plt.plot(years, hydro_adoption, label='Hydropower', color='lightgreen', linestyle='-.', marker='^', linewidth=2)
plt.plot(years, geothermal_adoption, label='Geothermal Energy', color='brown', linestyle=':', marker='d', linewidth=2)

plt.title('The Evolution of Renewable Energy Adoption\nin EcoLand (2010-2020)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Adoption Rate (% of Total Energy Consumption)', fontsize=12)

plt.legend(title="Energy Source", loc='upper left', fontsize=10)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

plt.annotate('Solar Boost\nInnovations', xy=(2015, 14), xytext=(2013, 25),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, backgroundcolor='w')

plt.annotate('Steady Wind\nPolicy Support', xy=(2017, 24), xytext=(2015, 10),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, backgroundcolor='w')

plt.tight_layout()
plt.show()