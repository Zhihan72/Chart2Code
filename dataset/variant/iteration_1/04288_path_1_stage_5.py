import matplotlib.pyplot as plt
import numpy as np

# Original data
years = np.arange(2010, 2021)
north_america_co2 = [5500, 5400, 5300, 5200, 5100, 5000, 4900, 4800, 4700, 4650, 4600]
europe_co2 = [3350, 3450, 3200, 3300, 3400, 3250, 3050, 3150, 3000, 3100, 3500]  # Shuffled
asia_co2 = [12000, 10400, 11200, 13200, 10800, 11600, 12600, 10000, 12400, 12900, 12200]  # Shuffled
north_america_renew = [12, 10, 24, 30, 35, 15, 17, 20, 28, 32, 22]  # Shuffled
europe_renew = [40, 23, 18, 38, 15, 20, 28, 30, 36, 25, 33]  # Shuffled
asia_renew = [5, 28, 18, 22, 6, 15, 12, 8, 20, 10, 25]  # Shuffled

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 16))

# Plot for CO2 emissions
ax1.plot(years, north_america_co2, color='blue', marker='o', linestyle='-', linewidth=2)
ax1.plot(years, europe_co2, color='blue', marker='s', linestyle='--', linewidth=2)
ax1.plot(years, asia_co2, color='blue', marker='^', linestyle='-.', linewidth=2)
ax1.axvline(x=2015, color='grey', linestyle=':', linewidth=1)
ax1.text(2015.5, 9000, 'Paris (2015)', fontsize=9, color='grey')
ax1.set_title("CO2 Emissions (2010-20)", fontsize=14, pad=20)
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("CO2 (MMT)", fontsize=12)
ax1.set_xticks(years)
ax1.spines['top'].set_linewidth(0)
ax1.spines['right'].set_linewidth(0)
ax1.annotate('Decline', xy=(2019, 4650), xytext=(2016, 5000),
             arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Plot for renewable energy
ax2.plot(years, north_america_renew, color='blue', marker='o', linestyle='-', linewidth=2)
ax2.plot(years, europe_renew, color='blue', marker='s', linestyle='--', linewidth=2)
ax2.plot(years, asia_renew, color='blue', marker='^', linestyle='-.', linewidth=2)
ax2.set_title("Renewables (%) (2010-20)", fontsize=14, pad=20)
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Renewables (%)", fontsize=12)
ax2.set_xticks(years)
ax2.spines['top'].set_linewidth(0)
ax2.spines['right'].set_linewidth(0)
ax2.axvline(x=2020, color='grey', linestyle=':', linewidth=1)
ax2.text(2020.5, 25, 'Target 2020', fontsize=9, color='grey')

plt.tight_layout()
plt.show()