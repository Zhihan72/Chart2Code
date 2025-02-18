import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2051)

asia = np.array([0.5, 1.2, 2.5, 4.0, 6.5, 9.3, 13.5, 17.5, 22.0, 27.0, 33.0, 40.0, 48.5, 58.0, 68.5, 80.0, 92.5, 105.0, 120.0, 135.0, 150.0, 170.0, 190.0, 210.0, 235.0, 260.0])
europe = np.array([0.3, 0.8, 1.5, 2.5, 4.0, 6.0, 8.5, 11.0, 14.0, 17.5, 21.5, 26.0, 31.0, 36.5, 42.5, 49.0, 56.0, 64.0, 72.5, 81.5, 91.0, 102.0, 114.0, 127.0, 140.5, 155.5])
north_america = np.array([0.4, 1.0, 1.8, 3.0, 4.8, 7.0, 9.7, 12.5, 15.8, 19.5, 23.5, 28.0, 33.0, 38.5, 44.5, 51.0, 58.0, 66.0, 74.5, 83.5, 93.0, 104.0, 116.0, 129.0, 143.5, 158.5])
africa = np.array([0.1, 0.3, 0.5, 0.8, 1.2, 1.8, 2.5, 3.3, 4.2, 5.3, 6.5, 8.0, 9.5, 11.0, 13.0, 15.0, 17.5, 20.0, 23.0, 26.5, 30.0, 34.0, 38.5, 43.0, 48.5, 54.5])
south_america = np.array([0.2, 0.5, 0.8, 1.3, 2.0, 3.0, 4.2, 5.6, 7.3, 9.3, 11.5, 14.0, 17.0, 20.5, 24.5, 29.0, 34.0, 39.5, 45.5, 52.0, 59.0, 67.0, 76.0, 86.0, 97.5, 110.0])

fig, ax1 = plt.subplots(figsize=(14, 8))

new_colors = ['#32cd32', '#4682b4', '#ff6347', '#dda0dd', '#ffd700']

ax1.stackplot(years, asia, europe, north_america, africa, south_america, labels=['Asia', 'Europe', 'North America', 'Africa', 'South America'], colors=new_colors, alpha=0.75)

ax1.set_title("Global Drone Delivery Usage:\nTrends Across Continents (2025-2050)", fontsize=18, fontweight='bold')
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Millions of Packages Delivered', fontsize=14)
ax1.legend(loc='upper center', fontsize=12, bbox_to_anchor=(0.5, 1.15), ncol=3, frameon=False)
ax1.grid(True, linestyle='-', alpha=0.3)

ax1.set_xlim(2024, 2051)
ax1.set_xticks(np.arange(2025, 2051, 5))
ax1.tick_params(axis='x', rotation=45)

ax1.annotate('Regulatory Peak in Asia', xy=(2034, 22), xytext=(2037, 48),
             arrowprops=dict(facecolor='grey', arrowstyle='->'), fontsize=10, color='blue')
ax1.annotate('NA Expansion Landmark', xy=(2040, 33), xytext=(2043, 77),
             arrowprops=dict(facecolor='red', arrowstyle='->'), fontsize=10, color='green')

ax2 = ax1.twinx()
growth_rate = ((asia + europe + north_america + africa + south_america) /
               (asia[0] + europe[0] + north_america[0] + africa[0] + south_america[0]) - 1) * 100
ax2.plot(years, growth_rate, 'g-.', label='Growth Rate')
ax2.set_ylabel('Growth Rate (%)', fontsize=14)
ax2.yaxis.label.set_color('blue')
ax2.spines['right'].set_color('blue')
ax2.tick_params(axis='y', colors='blue')
ax2.legend(loc='upper left', fontsize=12)

plt.grid(which='both', linestyle=':', linewidth='1', color='black')
plt.tight_layout()

plt.show()