import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = np.array([10, 40, 20, 150, 80, 600, 250, 400, 950, 1000, 800])
wind_energy = np.array([15, 50, 30, 140, 90, 450, 220, 320, 750, 900, 600])
solar_workforce = np.array([2, 6, 4, 16, 10, 50, 25, 35, 80, 90, 65])
wind_workforce = np.array([3, 8, 5, 18, 12, 52, 27, 38, 85, 100, 70])

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

bar_width = 0.35
bar1 = ax1.bar(years - bar_width/2, solar_energy, bar_width, label='Sunshine Power (GWh)', color='steelblue', alpha=0.7)
bar2 = ax1.bar(years + bar_width/2, wind_energy, bar_width, label='Breeze Power (GWh)', color='steelblue', alpha=0.7)

for bar in bar1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, height, f'{height}', ha='center', va='bottom')
for bar in bar2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, height, f'{height}', ha='center', va='bottom')

ax2.plot(years, solar_workforce, '-o', label='Sun Workers (Thousands)', color='steelblue', linewidth=2, markersize=8)
ax2.plot(years, wind_workforce, '-s', label='Wind Crew (Thousands)', color='steelblue', linewidth=2, markersize=8)

for x, y in zip(years, solar_workforce):
    ax2.annotate(f'{y}', xy=(x, y), xytext=(3, 3), textcoords='offset points', fontsize=9, color='steelblue')
for x, y in zip(years, wind_workforce):
    ax2.annotate(f'{y}', xy=(x, y), xytext=(3, -12), textcoords='offset points', fontsize=9, color='steelblue')

ax1.set_title("Renewable Power Rise (2010-2020)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Timeline", fontsize=12)
ax1.set_ylabel("Production (GWh)", fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.6)

ax2.set_title("Growing Energy Jobs (2010-2020)", fontsize=16, fontweight='bold')
ax2.set_xlabel("Timeline", fontsize=12)
ax2.set_ylabel("Job Count (Thousands)", fontsize=12)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()