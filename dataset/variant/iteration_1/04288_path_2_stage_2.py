import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
north_america_co2 = [5500, 5400, 5300, 5200, 5100, 5000, 4900, 4800, 4700, 4650, 4600]
europe_co2 = [3500, 3450, 3400, 3350, 3300, 3250, 3200, 3150, 3100, 3050, 3000]
asia_co2 = [10000, 10400, 10800, 11200, 11600, 12000, 12200, 12400, 12600, 12900, 13200]
north_america_renew = [10, 12, 15, 17, 20, 22, 24, 28, 30, 32, 35]
europe_renew = [15, 18, 20, 23, 25, 28, 30, 33, 36, 38, 40]
asia_renew = [5, 6, 8, 10, 12, 15, 18, 20, 22, 25, 28]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

ax1.plot(years, north_america_co2, label="North America", color='orange', marker='o', linestyle='-', linewidth=2)
ax1.plot(years, europe_co2, label="Europe", color='purple', marker='s', linestyle='--', linewidth=2)
ax1.plot(years, asia_co2, label="Asia", color='teal', marker='^', linestyle='-.', linewidth=2)
ax1.axvline(x=2015, color='grey', linestyle=':', linewidth=1)
ax1.text(2015.5, 9000, 'Paris Agreement (2015)', fontsize=9, color='grey')
ax1.set_title("Impact of Climate Policy on CO2 Emissions (2010-2020)", fontsize=14, pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("CO2 Emissions (in million metric tons)", fontsize=12)
ax1.legend(loc='upper right', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.6)
ax1.set_xticks(years)
ax1.annotate('Steady decline', xy=(2019, 4650), xytext=(2016, 5000),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

ax2.plot(years, north_america_renew, label="North America", color='orange', marker='o', linestyle='-', linewidth=2)
ax2.plot(years, europe_renew, label="Europe", color='purple', marker='s', linestyle='--', linewidth=2)
ax2.plot(years, asia_renew, label="Asia", color='teal', marker='^', linestyle='-.', linewidth=2)
ax2.set_title("Renewable Energy Adoption Rates (2010-2020)", fontsize=14, pad=20)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Renewable Energy Adoption (%)", fontsize=12)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.6)
ax2.set_xticks(years)
ax2.axvline(x=2020, color='grey', linestyle=':', linewidth=1)
ax2.text(2020.5, 25, '2020 Target Year', fontsize=9, color='grey')

plt.tight_layout()
plt.show()