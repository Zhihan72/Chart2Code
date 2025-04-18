import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solartech_share = np.array([20, 22, 24, 26, 27, 29, 31, 34, 36, 38, 40])
firstsolar_share = np.array([15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 28])
others_share = np.array([40, 38, 36, 34, 33, 31, 29, 26, 23, 20, 17])

market_share_data = np.vstack([solartech_share, firstsolar_share, others_share])
labels = ['SolarTech', 'First Solar', 'Others']
colors = ['#ff9999', '#99ff99', '#ffcc99']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))

ax1.stackplot(years, market_share_data, labels=labels, colors=colors, alpha=0.8, edgecolor='black')
ax1.set_title("Solar Energy Market Share Dynamics (2010-2020)", fontsize=14, fontweight='bold', fontstyle='italic')
ax1.set_xlabel("Year", fontsize=12, fontweight='light')
ax1.set_ylabel("Market Share (%)", fontsize=12, fontweight='light')
ax1.legend(loc='upper left', title='Companies', fontsize=9, shadow=True)
ax1.grid(True, linestyle='-.', linewidth=0.7, alpha=0.7)

ax1.plot(years, solartech_share, color='darkblue', linewidth=3, linestyle=':', marker='o', label='SolarTech')
ax1.legend(loc='upper left', fontsize=9, shadow=True)

ax1.annotate('Entry into New Market', xy=(2016, 31), xytext=(2014, 36),
             arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'), fontsize=10)
ax1.annotate('Technological Breakthrough', xy=(2019, 38), xytext=(2017, 42),
             arrowprops=dict(arrowstyle='->', lw=1.5, color='gray'), fontsize=10)

final_year_shares = market_share_data[:, -1]
ax2.pie(final_year_shares, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90,
        wedgeprops={'alpha':0.8, 'edgecolor':'gray', 'linewidth': 1}, textprops={'fontsize': 10})

ax2.set_title("Final Market Shares in 2020", fontsize=14, fontweight='bold', fontstyle='italic')

plt.tight_layout()
plt.show()