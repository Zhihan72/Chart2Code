import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2051)

asia = np.array([22.0, 13.5, 4.0, 48.5, 105.0, 58.0, 0.5, 135.0, 150.0, 6.5, 1.2, 27.0, 260.0, 68.5, 9.3, 33.0, 17.5, 92.5, 170.0, 190.0, 210.0, 80.0, 40.0, 27.0, 235.0, 120.0])
europe = np.array([21.5, 127.0, 64.0, 4.0, 36.5, 102.0, 1.5, 91.0, 56.0, 72.5, 0.3, 49.0, 81.5, 11.0, 38.5, 2.5, 6.0, 155.5, 14.0, 114.0, 140.5, 31.0, 8.5, 26.0, 42.5, 17.5])
north_america = np.array([1.0, 38.5, 6.0, 158.5, 51.0, 129.0, 3.0, 66.0, 93.0, 104.0, 12.5, 66.0, 0.4, 38.5, 44.5, 74.5, 4.8, 33.0, 9.7, 11.0, 15.8, 116.0, 19.5, 143.5, 23.5, 83.5])
africa = np.array([43.0, 0.5, 11.0, 0.1, 5.3, 3.3, 6.5, 15.0, 4.2, 13.0, 38.5, 23.0, 30.0, 1.8, 20.0, 26.5, 17.5, 9.5, 54.5, 1.2, 8.0, 2.5, 0.8, 34.0, 1.8, 0.3])
south_america = np.array([97.5, 45.5, 9.3, 1.3, 24.5, 7.3, 20.5, 34.0, 14.0, 2.0, 76.0, 59.0, 5.6, 39.5, 29.0, 17.0, 110.0, 52.0, 3.0, 67.0, 86.0, 11.5, 0.5, 0.2, 4.2, 1.3])

fig, ax1 = plt.subplots(figsize=(14, 8))

colors = ['#2ca02c', '#1f77b4', '#9467bd', '#d62728', '#ff7f0e']
ax1.stackplot(years, asia, europe, north_america, africa, south_america, labels=['Asian', 'EU', 'N. America', 'African Nations', 'S. America'], colors=colors, alpha=0.85)

ax1.set_title("Drone Delivery Phenomena through 2025-2050", fontsize=16, fontweight='light')
ax1.set_xlabel('Timeline (Year)', fontsize=12)
ax1.set_ylabel('Packages Delivered (Millions)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10, bbox_to_anchor=(1.05, 1))
ax1.grid(True, linestyle='-', alpha=0.7)

ax1.set_xticks(np.arange(2025, 2051, 5))
ax1.tick_params(axis='x', rotation=30, labelcolor='darkblue')

ax1.annotate('Asian Growth Surge', xy=(2032, 22), xytext=(2037, 80), arrowprops=dict(facecolor='green', shrink=0.05), fontsize=9, color='green')
ax1.annotate('N. America Boost', xy=(2040, 33), xytext=(2044, 90), arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=9, color='blue')

ax2 = ax1.twinx()
growth_rate = ((asia + europe + north_america + africa + south_america) / (asia[0] + europe[0] + north_america[0] + africa[0] + south_america[0]) - 1) * 100
ax2.plot(years, growth_rate, 'r:', label='Delivery Growth Rate (%)')
ax2.set_ylabel('Growth (%)', fontsize=12)
ax2.yaxis.label.set_color('red')
ax2.spines['right'].set_color('red')
ax2.tick_params(axis='y', colors='red')
ax2.legend(loc='upper right', fontsize=10)

plt.grid(which='both', linestyle='--', linewidth='0.5', color='black')
plt.tight_layout()

plt.show()