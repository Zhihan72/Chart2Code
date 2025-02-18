import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solar_energy = np.array([10, 20, 40, 80, 150, 250, 400, 600, 800, 950, 1000])
wind_energy = np.array([15, 30, 50, 90, 140, 220, 320, 450, 600, 750, 900])
solar_workforce = np.array([2, 4, 6, 10, 16, 25, 35, 50, 65, 80, 90])
wind_workforce = np.array([3, 5, 8, 12, 18, 27, 38, 52, 70, 85, 100])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# Energy production (bar chart) with consistent color
bar_width = 0.35
bar1 = ax1.bar(years - bar_width/2, solar_energy, bar_width, label='Solar Energy (GWh)', color='steelblue', alpha=0.7)
bar2 = ax1.bar(years + bar_width/2, wind_energy, bar_width, label='Wind Energy (GWh)', color='steelblue', alpha=0.7)

for bar in bar1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, height, f'{height}', ha='center', va='bottom')
for bar in bar2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2.0, height, f'{height}', ha='center', va='bottom')

# Workforce (line chart) with consistent color
ax2.plot(years, solar_workforce, '-o', label='Solar Workforce (Thousands)', color='steelblue', linewidth=2, markersize=8)
ax2.plot(years, wind_workforce, '-s', label='Wind Workforce (Thousands)', color='steelblue', linewidth=2, markersize=8)

for x, y in zip(years, solar_workforce):
    ax2.annotate(f'{y}', xy=(x, y), xytext=(3, 3), textcoords='offset points', fontsize=9, color='steelblue')
for x, y in zip(years, wind_workforce):
    ax2.annotate(f'{y}', xy=(x, y), xytext=(3, -12), textcoords='offset points', fontsize=9, color='steelblue')

ax1.set_title("Growth in Renewable Energy Production (2010-2020)", fontsize=16, fontweight='bold')
ax1.set_xlabel("Year", fontsize=12)
ax1.set_ylabel("Energy Production (GWh)", fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(True, linestyle='--', alpha=0.6)

ax2.set_title("Employment in Renewable Energy Sectors (2010-2020)", fontsize=16, fontweight='bold')
ax2.set_xlabel("Year", fontsize=12)
ax2.set_ylabel("Workforce (Thousands)", fontsize=12)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(True, linestyle='--', alpha=0.6)

plt.tight_layout()
plt.show()