import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
europe_renewables = np.array([150, 165, 180, 200, 230, 260, 300, 340, 390, 450, 500])
asia_renewables = np.array([100, 120, 150, 180, 220, 270, 320, 380, 450, 530, 610])
north_america_renewables = np.array([90, 110, 130, 150, 180, 210, 250, 290, 330, 370, 420])
africa_renewables = np.array([30, 35, 40, 50, 60, 80, 100, 130, 170, 220, 290])
oceania_renewables = np.array([20, 25, 30, 35, 45, 55, 70, 90, 110, 130, 160])

total_renewables = europe_renewables + asia_renewables + north_america_renewables + africa_renewables + oceania_renewables

europe_share = (europe_renewables / total_renewables) * 100
asia_share = (asia_renewables / total_renewables) * 100
north_america_share = (north_america_renewables / total_renewables) * 100
africa_share = (africa_renewables / total_renewables) * 100
oceania_share = (oceania_renewables / total_renewables) * 100

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8), sharex=True)

ax1.stackplot(years, europe_renewables, asia_renewables, north_america_renewables,
              africa_renewables, oceania_renewables,
              colors=['#FFD700', '#FF6347', '#4682B4', '#32CD32', '#9370DB'], alpha=0.8)

ax1.legend(loc='upper left', title='Continents')
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax1.annotate('Europe surpasses 400 TWh', xy=(2019, 450), xytext=(2015.5, 600),
             arrowprops=dict(arrowstyle='->', color='black'), color='black', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

ax1.annotate('Asia takes the lead', xy=(2020, 610), xytext=(2017, 750),
             arrowprops=dict(arrowstyle='->', color='black'), color='black', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

ax2.plot(years, europe_share, label='Europe', color='#FFD700', marker='o')
ax2.plot(years, asia_share, label='Asia', color='#FF6347', marker='o')
ax2.plot(years, north_america_share, label='North America', color='#4682B4', marker='o')
ax2.plot(years, africa_share, label='Africa', color='#32CD32', marker='o')
ax2.plot(years, oceania_share, label='Oceania', color='#9370DB', marker='o')

ax2.legend(loc='upper right')
ax2.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()