import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solartech_share = np.array([20, 22, 24, 26, 27, 29, 31, 34, 36, 38, 40])
sunpower_share = np.array([25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15])
firstsolar_share = np.array([15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 28])
others_share = np.array([40, 38, 36, 34, 33, 31, 29, 26, 23, 20, 17])

market_share_data = np.vstack([solartech_share, sunpower_share, firstsolar_share, others_share])
labels = ['SolarTech', 'SunPower', 'First Solar', 'Others']
colors = ['#66b3ff', '#ffcc99', '#ff9999', '#99ff99']  # Different color order

fig, ax1 = plt.subplots(figsize=(9, 8))

ax1.stackplot(years, market_share_data, labels=labels, colors=colors, alpha=0.8)
ax1.set_title("Solar Energy Market Share Dynamics (2010-2020)", fontsize=14, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Market Share (%)", fontsize=12)
ax1.legend(loc='lower right', title='Companies', fontsize=10)  # Changed legend location
ax1.grid(True, linestyle=':', alpha=0.6)  # Changed grid style

ax1.plot(years, solartech_share, color='black', linewidth=2, linestyle='-.', marker='o', label='SolarTech Trend')
ax1.legend(loc='lower right', fontsize=10)

ax1.annotate('Entry into New Market', xy=(2016, 31), xytext=(2013, 35),
             arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10)  # Changed annotation styles
ax1.annotate('Technological Breakthrough', xy=(2019, 38), xytext=(2017, 42),
             arrowprops=dict(facecolor='blue', arrowstyle='->'), fontsize=10)

plt.tight_layout()
plt.show()