import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_adoption = [2, 3, 5, 7, 10, 14, 18, 25, 30, 35, 40]
wind_adoption = [10, 11, 13, 15, 17, 19, 21, 24, 26, 28, 30]
hydro_adoption = [30, 31, 31, 32, 33, 33, 34, 35, 35, 36, 36]

plt.figure(figsize=(12, 6))

plt.plot(years, solar_adoption, label='Solar Energy', color='orange', linestyle='-', marker='D', linewidth=1.5)
plt.plot(years, wind_adoption, label='Wind Energy', color='blue', linestyle=':', marker='x', linewidth=2)
plt.plot(years, hydro_adoption, label='Hydropower', color='green', linestyle='-', marker='h', linewidth=1)

plt.title('Renewable Energy Adoption in EcoLand (2010-2020)', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Adoption Rate (% of Total Energy)', fontsize=12)

plt.legend(title="Energy Type", loc='lower right', fontsize=9, frameon=False, shadow=True)

plt.grid(False)

plt.annotate('Solar Surge', xy=(2015, 14), xytext=(2013, 25),
             arrowprops=dict(facecolor='grey', arrowstyle='->'),
             fontsize=9, backgroundcolor='w')

plt.annotate('Wind Growth', xy=(2017, 24), xytext=(2015, 10),
             arrowprops=dict(facecolor='grey', arrowstyle='->'),
             fontsize=9, backgroundcolor='w')

plt.subplot().spines['top'].set_visible(False)
plt.subplot().spines['right'].set_visible(False)

plt.tight_layout()
plt.show()