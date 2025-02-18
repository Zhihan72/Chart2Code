import matplotlib.pyplot as plt
import numpy as np

# Data construction for the following series:
years = np.arange(2010, 2021)
solar_energy = np.array([12, 18, 45, 78, 140, 230, 410, 610, 790, 930, 980])  # Altered Solar energy production in GWh
wind_energy = np.array([18, 28, 55, 85, 135, 210, 330, 460, 590, 730, 880])   # Altered Wind energy production in GWh
solar_workforce = np.array([3, 5, 7, 9, 15, 26, 36, 49, 67, 79, 92])         # Altered Solar workforce in thousands
wind_workforce = np.array([4, 6, 9, 13, 19, 28, 37, 53, 68, 83, 98])         # Altered Wind workforce in thousands

# Create the plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))

# First subplot: Energy production (bar chart)
bar_width = 0.35
bar1 = ax1.bar(years - bar_width/2, solar_energy, bar_width, label='Solar Energy (GWh)', color='goldenrod', alpha=0.7)
bar2 = ax1.bar(years + bar_width/2, wind_energy, bar_width, label='Wind Energy (GWh)', color='steelblue', alpha=0.7)

for bar in bar1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height}', ha='center', va='bottom')
for bar in bar2:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2.0, height, f'{height}', ha='center', va='bottom')

# Second subplot: Workforce (line chart)
ax2.plot(years, solar_workforce, '-o', label='Solar Workforce (Thousands)', color='darkorange', linewidth=2, markersize=8)
ax2.plot(years, wind_workforce, '-s', label='Wind Workforce (Thousands)', color='dodgerblue', linewidth=2, markersize=8)

for x, y in zip(years, solar_workforce):
    ax2.annotate(f'{y}', xy=(x, y), xytext=(3, 3), textcoords='offset points', fontsize=9, color='darkorange')
for x, y in zip(years, wind_workforce):
    ax2.annotate(f'{y}', xy=(x, y), xytext=(3, -12), textcoords='offset points', fontsize=9, color='dodgerblue')

# Customizing the plot
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