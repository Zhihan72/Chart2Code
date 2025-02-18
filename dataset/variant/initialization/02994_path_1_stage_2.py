import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
europe_renewables = np.array([150, 165, 180, 200, 230, 260, 300, 340, 390, 450, 500])
asia_renewables = np.array([100, 120, 150, 180, 220, 270, 320, 380, 450, 530, 610])
north_america_renewables = np.array([90, 110, 130, 150, 180, 210, 250, 290, 330, 370, 420])
africa_renewables = np.array([30, 35, 40, 50, 60, 80, 100, 130, 170, 220, 290])
oceania_renewables = np.array([20, 25, 30, 35, 45, 55, 70, 90, 110, 130, 160])
south_america_renewables = np.array([40, 50, 65, 80, 100, 120, 150, 180, 220, 270, 340])
antarctica_renewables = np.array([2, 3, 5, 7, 10, 15, 25, 30, 40, 50, 60])

fig, ax = plt.subplots(figsize=(10, 8))

ax.stackplot(years, europe_renewables, asia_renewables, north_america_renewables,
             africa_renewables, oceania_renewables, south_america_renewables, antarctica_renewables,
             labels=['Europe', 'Asia', 'North America', 'Africa', 'Oceania', 'South America', 'Antarctica'],
             colors=['#FFD700', '#FF6347', '#4682B4', '#32CD32', '#9370DB', '#FF8C00', '#40E0D0'], alpha=0.8)

ax.set_title('Global Renewable Energy Production by Continent (2010-2020)', fontsize=14, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Renewable Energy Production (TWh)', fontsize=12)
ax.legend(loc='upper left', title='Continents')
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax.annotate('Europe surpasses 400 TWh', xy=(2019, 450), xytext=(2015.5, 600),
            arrowprops=dict(arrowstyle='->', color='black'), color='black', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

ax.annotate('Asia takes the lead', xy=(2020, 610), xytext=(2017, 750),
            arrowprops=dict(arrowstyle='->', color='black'), color='black', fontsize=10, bbox=dict(facecolor='white', alpha=0.8))

plt.xticks(years, rotation=45)
plt.tight_layout()
plt.show()