import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
north_america_co2 = [5500, 5400, 5300, 5200, 5100, 5000, 4900, 4800, 4700, 4650, 4600]
europe_co2 = [3500, 3450, 3400, 3350, 3300, 3250, 3200, 3150, 3100, 3050, 3000]
north_america_renew = [10, 12, 15, 17, 20, 22, 24, 28, 30, 32, 35]
europe_renew = [15, 18, 20, 23, 25, 28, 30, 33, 36, 38, 40]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 12))

ax1.plot(years, north_america_co2, label="NA", color='red', marker='D', linestyle='-', linewidth=1.5)
ax1.plot(years, europe_co2, label="EU", color='blue', marker='x', linestyle='--', linewidth=2.5)
ax1.axvline(x=2014, color='black', linestyle='-.', linewidth=2)
ax1.text(2015.5, 9000, 'Agreement (2015)', fontsize=9, color='grey')
ax1.set_title("Impact on CO2 Levels (2010-2020)", fontsize=14, pad=20)
ax1.set_xlabel("Timeline", fontsize=12)
ax1.set_ylabel("CO2 Output\n(millions)", fontsize=12)
ax1.legend(loc='lower left', fontsize=9)
ax1.grid(True, linestyle='-', alpha=0.3)
ax1.set_xticks(years)
ax1.annotate('Reduction', xy=(2020, 4600), xytext=(2017, 4800),
             arrowprops=dict(facecolor='purple', arrowstyle='->'), fontsize=10)

ax2.plot(years, north_america_renew, label="NA", color='red', marker='D', linestyle='-', linewidth=1.5)
ax2.plot(years, europe_renew, label="EU", color='blue', marker='x', linestyle='--', linewidth=2.5)
ax2.set_title("Rise in Renewables (2010-2020)", fontsize=14, pad=20)
ax2.set_xlabel("Timeline", fontsize=12)
ax2.set_ylabel("Renewable Use\n(%)", fontsize=12)
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, linestyle='-', alpha=0.3)
ax2.set_xticks(years)
ax2.axvline(x=2019, color='black', linestyle='--', linewidth=1.5)
ax2.text(2020.5, 25, 'Goal Year', fontsize=9, color='grey')

plt.tight_layout()
plt.show()