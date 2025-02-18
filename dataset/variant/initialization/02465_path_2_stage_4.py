import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2025, 2051)

asia = np.array([0.5, 1.2, 2.5, 4.0, 6.5, 9.3, 13.5, 17.5, 22.0, 27.0, 33.0, 40.0, 48.5, 58.0, 68.5, 80.0, 92.5, 105.0, 120.0, 135.0, 150.0, 170.0, 190.0, 210.0, 235.0, 260.0])
europe = np.array([0.3, 0.8, 1.5, 2.5, 4.0, 6.0, 8.5, 11.0, 14.0, 17.5, 21.5, 26.0, 31.0, 36.5, 42.5, 49.0, 56.0, 64.0, 72.5, 81.5, 91.0, 102.0, 114.0, 127.0, 140.5, 155.5])
africa = np.array([0.1, 0.3, 0.5, 0.8, 1.2, 1.8, 2.5, 3.3, 4.2, 5.3, 6.5, 8.0, 9.5, 11.0, 13.0, 15.0, 17.5, 20.0, 23.0, 26.5, 30.0, 34.0, 38.5, 43.0, 48.5, 54.5])

fig, ax1 = plt.subplots(figsize=(14, 8))

new_colors = ['#32cd32', '#4682b4', '#dda0dd']

ax1.stackplot(years, asia, europe, africa, labels=['Asien', 'Europæ', 'Afrique'], colors=new_colors, alpha=0.75)

ax1.set_title("Drone Delivery Surging Worldwide:\nGeographic Patterns (2025-2050)", fontsize=18, fontweight='bold')
ax1.set_xlabel('Timeline', fontsize=14)
ax1.set_ylabel('Packages in Millions', fontsize=14)
ax1.legend(loc='upper center', fontsize=12, bbox_to_anchor=(0.5, 1.15), ncol=3, frameon=False)
ax1.grid(True, linestyle='-', alpha=0.3)

ax1.set_xlim(2024, 2051)
ax1.set_xticks(np.arange(2025, 2051, 5))
ax1.tick_params(axis='x', rotation=45)

ax1.annotate('Asian Regulatory Surge', xy=(2034, 22), xytext=(2037, 48),
             arrowprops=dict(facecolor='grey', arrowstyle='->'), fontsize=10, color='blue')

# Updating growth rate calculation without north_america and south_america
growth_rate = ((asia + europe + africa) /
               (asia[0] + europe[0] + africa[0]) - 1) * 100
ax2 = ax1.twinx()
ax2.plot(years, growth_rate, 'g-.', label='Growth Metrics')
ax2.set_ylabel('Increase (%)', fontsize=14)
ax2.yaxis.label.set_color('blue')
ax2.spines['right'].set_color('blue')
ax2.tick_params(axis='y', colors='blue')
ax2.legend(loc='upper left', fontsize=12)

plt.grid(which='both', linestyle=':', linewidth='1', color='black')
plt.tight_layout()

plt.show()