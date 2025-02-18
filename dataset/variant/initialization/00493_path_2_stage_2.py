import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec

years = np.arange(1990, 2021)

solar_energy = np.array([0, 1, 3, 7, 15, 25, 50, 90, 140, 200, 280, 350, 440, 550, 680, 820, 970, 1130, 1300, 1480, 1670, 1870, 2080, 2300, 2530, 2770, 3020, 3280, 3550, 3830, 4120])
wind_energy = np.array([0, 1, 4, 9, 20, 35, 60, 100, 160, 230, 320, 420, 530, 650, 780, 920, 1070, 1230, 1400, 1580, 1770, 1970, 2180, 2400, 2630, 2870, 3120, 3380, 3650, 3930, 4220])
hydroelectric_energy = np.array([500, 510, 525, 540, 560, 580, 600, 620, 650, 680, 710, 740, 770, 800, 830, 860, 890, 920, 950, 980, 1010, 1040, 1070, 1100, 1130, 1160, 1190, 1220, 1250, 1280, 1310])
geothermal_energy = np.array([10, 11, 13, 16, 20, 25, 31, 38, 46, 55, 65, 76, 88, 101, 115, 130, 146, 163, 181, 200, 220, 241, 263, 286, 310, 335, 361, 388, 416, 445, 475])

growth_rate_solar = np.gradient(solar_energy)
growth_rate_wind = np.gradient(wind_energy)
growth_rate_hydroelectric = np.gradient(hydroelectric_energy)
growth_rate_geothermal = np.gradient(geothermal_energy)

fig = plt.figure(figsize=(16, 10))
gs = GridSpec(1, 2, figure=fig)

ax1 = fig.add_subplot(gs[0, 0])
ax1.stackplot(years, solar_energy, wind_energy, hydroelectric_energy, geothermal_energy,
              colors=['#00BFFF', '#00BFFF', '#00BFFF', '#00BFFF'], alpha=0.8)

ax1.set_title('The Evolution of Green Technologies:\nRenewable Energy Contributions Over the Decades',
              fontsize=16, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Energy Production (TWh)', fontsize=12)
ax1.set_xticks(np.arange(1990, 2021, 5))
ax1.set_xticklabels(np.arange(1990, 2021, 5), rotation=45, ha='right')

ax1.annotate('Start of Global Renewable Initiatives', (2005, 900), 
             textcoords="offset points", xytext=(30, 10), ha='center', fontsize=10,
             arrowprops=dict(arrowstyle='->', color='black'))
ax1.annotate('Technological Breakthroughs in Solar', (2010, 1600),
             textcoords="offset points", xytext=(-20, 10), ha='center', fontsize=10,
             arrowprops=dict(arrowstyle='->', color='black'))

ax2 = fig.add_subplot(gs[0, 1])
ax2.plot(years, growth_rate_solar, color='#00BFFF', linewidth=2, linestyle='-')
ax2.plot(years, growth_rate_wind, color='#00BFFF', linewidth=2, linestyle='--')
ax2.plot(years, growth_rate_hydroelectric, color='#00BFFF', linewidth=2, linestyle='-.')
ax2.plot(years, growth_rate_geothermal, color='#00BFFF', linewidth=2, linestyle=':')

ax2.set_title('Annual Growth Rates of Renewable Technologies', fontsize=16, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Growth Rate (TWh/year)', fontsize=12)
ax2.set_xticks(np.arange(1990, 2021, 5))
ax2.set_xticklabels(np.arange(1990, 2021, 5), rotation=45, ha='right')

plt.tight_layout()
plt.show()