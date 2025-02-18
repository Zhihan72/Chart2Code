import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)
solar = [1.1, 1.4, 1.8, 2.3, 3.0, 3.8, 5.0, 6.2, 8.0, 10.1, 13.2, 17.0, 21.5, 27.0, 34.1, 39.6, 45.0, 52.2, 61.2, 71.3, 83.0]
wind = [4.5, 5.2, 6.1, 7.4, 9.1, 11.0, 13.5, 16.5, 21.2, 26.0, 32.0, 38.8, 45.6, 53.2, 61.8, 70.0, 81.0, 94.0, 108.0, 120.0, 135.0]
hydro = [50.0, 51.0, 52.0, 54.0, 55.0, 57.0, 59.5, 62.0, 65.0, 68.0, 71.0, 74.0, 77.0, 80.5, 84.0, 88.0, 92.0, 96.0, 100.0, 104.0, 109.0]

# New data series
geothermal = [2.0, 2.1, 2.3, 2.5, 2.6, 2.8, 3.0, 3.3, 3.8, 4.2, 4.8, 5.3, 6.0, 6.7, 7.5, 8.0, 8.6, 9.3, 10.0, 11.0, 12.5]
nuclear = [20.0, 20.5, 21.0, 21.5, 22.0, 23.0, 23.5, 24.0, 25.0, 26.0, 27.0, 28.0, 29.0, 30.0, 31.5, 33.0, 34.5, 36.0, 37.5, 39.0, 40.5]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, solar, label='Sun Power', marker='o', color='#FFD700', linewidth=2, linestyle='-')
ax.plot(years, wind, label='Breeze Generation', marker='^', color='#00BFFF', linewidth=2, linestyle='--')
ax.plot(years, hydro, label='Water Flow', marker='s', color='#32CD32', linewidth=2, linestyle='-.')
ax.plot(years, geothermal, label='Earth Heat', marker='D', color='#8B4513', linewidth=2, linestyle=':')
ax.plot(years, nuclear, label='Atomic Force', marker='x', color='#800080', linewidth=2, linestyle='-')

ax.annotate('Wind is Winning', xy=(2013, 27.0), xytext=(2010, 50),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center', color='black')
ax.annotate('Hydro Rules', xy=(2009, 68.0), xytext=(2003, 80),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, ha='center', color='black')

for i, txt in enumerate(solar):
    ax.text(years[i], solar[i] + 2, str(txt), fontsize=9, ha='center', color='#FFD700')

for i, txt in enumerate(wind):
    ax.text(years[i], wind[i] + 2, str(txt), fontsize=9, ha='center', color='#00BFFF')
    
for i, txt in enumerate(hydro):
    ax.text(years[i], hydro[i] - 3, str(txt), fontsize=9, ha='center', color='#32CD32')

# New annotations for additional series
for i, txt in enumerate(geothermal):
    ax.text(years[i], geothermal[i] + 1, str(txt), fontsize=9, ha='center', color='#8B4513')

for i, txt in enumerate(nuclear):
    ax.text(years[i], nuclear[i] - 2, str(txt), fontsize=9, ha='center', color='#800080')

ax.set_title("The Green Surge: Energy Trends with Additional Sources\n(2000-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Calendar Year", fontsize=12)
ax.set_ylabel("Power Usage (TWh)", fontsize=12)

ax.legend(title='Forms of Power', loc='upper left', fontsize=10)
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)
plt.xticks(years[::2], rotation=45)
plt.tight_layout()
plt.show()