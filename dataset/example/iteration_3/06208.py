import matplotlib.pyplot as plt
import numpy as np

# Backstory: Monitoring Renewable Energy Adoption Over a Decade
# This plot analyzes the percentage of energy generated from renewable sources in four countries over a decade (2011-2020).

# Years from 2011 to 2020
years = np.arange(2011, 2021)

# Percentage of energy from renewable sources for four fictional countries: Solarlandia, Windtopia, Hydroville, and Geothermia
solarlandia_renewables = [15, 17, 19, 22, 25, 28, 31, 34, 37, 40]
windtopia_renewables = [10, 11, 13, 15, 18, 22, 25, 28, 30, 35]
hydroville_renewables = [20, 21, 23, 25, 26, 28, 30, 32, 34, 36]
geothermia_renewables = [5, 7, 9, 12, 15, 18, 22, 25, 28, 30]

# Plot the data
plt.figure(figsize=(14, 8))

# Plot each line with different styles
plt.plot(years, solarlandia_renewables, marker='o', linestyle='-', linewidth=2, color='orange', label='Solarlandia')
plt.plot(years, windtopia_renewables, marker='s', linestyle='--', linewidth=2, color='blue', label='Windtopia')
plt.plot(years, hydroville_renewables, marker='^', linestyle='-.', linewidth=2, color='green', label='Hydroville')
plt.plot(years, geothermia_renewables, marker='d', linestyle=':', linewidth=2, color='purple', label='Geothermia')

# Titles, labels, and legend
plt.title("Decadal Growth in Renewable Energy Adoption (2011-2020)\nAcross Four Countries", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Percentage of Energy from Renewables (%)', fontsize=12)
plt.xticks(years, rotation=45)
plt.yticks(np.arange(0, 45, 5))
plt.legend(title="Countries", loc='upper left', fontsize=10)

# Add grid for better readability
plt.grid(True, linestyle='--', alpha=0.6)

# Add annotations to highlight max values
max_solarlandia = max(solarlandia_renewables)
max_windtopia = max(windtopia_renewables)
max_hydroville = max(hydroville_renewables)
max_geothermia = max(geothermia_renewables)

plt.annotate(f'{max_solarlandia}%', xy=(years[-1], max_solarlandia), xytext=(years[-1]+0.3, max_solarlandia+1),
             arrowprops=dict(facecolor='orange', shrink=0.05), fontsize=10, color='orange')
plt.annotate(f'{max_windtopia}%', xy=(years[-1], max_windtopia), xytext=(years[-1]-2.5, max_windtopia+2),
             arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=10, color='blue')
plt.annotate(f'{max_hydroville}%', xy=(years[-1], max_hydroville), xytext=(years[-1]+0.3, max_hydroville+1),
             arrowprops=dict(facecolor='green', shrink=0.05), fontsize=10, color='green')
plt.annotate(f'{max_geothermia}%', xy=(years[-1], max_geothermia), xytext=(years[-1]+0.3, max_geothermia+1),
             arrowprops=dict(facecolor='purple', shrink=0.05), fontsize=10, color='purple')

# Automatically adjust layout to avoid text overlapping
plt.tight_layout()

# Show the plot
plt.show()