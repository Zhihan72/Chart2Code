import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar = [5, 7, 10, 14, 18, 23, 29, 35, 42, 50, 58]
wind = [4, 6, 9, 13, 17, 22, 27, 33, 40, 47, 55]
hydro = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
geothermal = [1, 2, 3, 4, 6, 8, 11, 14, 17, 21, 25]
biomass = [3, 4, 5, 6, 8, 10, 13, 16, 19, 23, 27]

fig, ax1 = plt.subplots(figsize=(16, 9))

# Updated color set
ax1.plot(years, solar, marker='o', linestyle='-', color='#FF5733', linewidth=2, label='Solar')
ax1.plot(years, wind, marker='s', linestyle='--', color='#33FF57', linewidth=2, label='Wind')
ax1.plot(years, hydro, marker='^', linestyle='-.', color='#5733FF', linewidth=2, label='Hydro')
ax1.plot(years, geothermal, marker='d', linestyle=':', color='#FF33C8', linewidth=2, label='Geothermal')
ax1.plot(years, biomass, marker='*', linestyle='-', color='#FFC300', linewidth=2, label='Biomass')

ax1.set_title('Adoption Trend of Renewable Energy Technologies (2010-2020)', fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Adoption Rate (%)', fontsize=14)
ax1.set_xticks(years)
ax1.grid(visible=True, linestyle='--', alpha=0.6)
ax1.legend(title='Technologies', loc='upper left', fontsize=12)

ax1.annotate('Solar Power Surges', xy=(2018, 42), xytext=(2017, 50),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='#FF5733')
ax1.annotate('Geothermal Picks Up Pace', xy=(2016, 8), xytext=(2014, 15),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=12, color='#FF33C8')

plt.tight_layout()
plt.show()