import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar_adoption = [2, 3, 5, 7, 10, 14, 18, 25, 30, 35, 40]
wind_adoption = [10, 11, 13, 15, 17, 19, 21, 24, 26, 28, 30]
hydro_adoption = [30, 31, 31, 32, 33, 33, 34, 35, 35, 36, 36]
geothermal_adoption = [4, 5, 6, 7, 8, 10, 12, 14, 16, 18, 20]

plt.figure(figsize=(12, 6))

# Change the color, linestyle, and marker for each plot
plt.plot(years, solar_adoption, label='Solar Energy', color='navy', linestyle='-', marker='v', linewidth=2)
plt.plot(years, wind_adoption, label='Wind Energy', color='tomato', linestyle='-', marker='*', linewidth=2)
plt.plot(years, hydro_adoption, label='Hydropower', color='darkorange', linestyle='--', marker='x', linewidth=2)
plt.plot(years, geothermal_adoption, label='Geothermal Energy', color='royalblue', linestyle=':', marker='p', linewidth=2)

plt.title('The Evolution of Renewable Energy Adoption\nin EcoLand (2010-2020)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Adoption Rate (% of Total Energy Consumption)', fontsize=12)

# Change legend title and location
plt.legend(title="Renewable Sources", loc='lower right', fontsize=10)

# Change grid style
plt.grid(True, which='both', linestyle='-.', linewidth=0.7, color='gray')

# Change annotation style
plt.annotate('Solar Peak', xy=(2015, 14), xytext=(2013, 25),
             arrowprops=dict(facecolor='gray', arrowstyle='wedge,tail_width=0.7'),
             fontsize=10, backgroundcolor='lightyellow')

plt.annotate('Policy Gain', xy=(2017, 24), xytext=(2015, 10),
             arrowprops=dict(facecolor='gray', arrowstyle='wedge,tail_width=0.7'),
             fontsize=10, backgroundcolor='lightyellow')

plt.tight_layout()
plt.show()