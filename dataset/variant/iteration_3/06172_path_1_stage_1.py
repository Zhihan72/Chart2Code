import matplotlib.pyplot as plt
import numpy as np

# Define years and energy consumption data
years = np.arange(2000, 2023)
traditional_energy = np.array([120, 118, 115, 113, 110, 107, 104, 100, 97, 94, 91, 88, 85, 83, 80, 78, 76, 74, 72, 70, 67, 65, 60])
solar_energy = np.array([0, 0, 0, 0, 0, 0, 0, 2, 4, 6, 8, 10, 12, 16, 20, 25, 30, 35, 40, 50, 55, 60, 65])
wind_energy = np.array([0, 0, 0, 0, 0, 0, 0, 1, 3, 5, 7, 10, 13, 18, 23, 30, 38, 47, 55, 60, 65, 70, 75])

# Plot setup
plt.figure(figsize=(14, 8))

# Plot the data with a single color
plt.plot(years, traditional_energy, label='Traditional Energy', color='green', linestyle='-', linewidth=2)
plt.plot(years, solar_energy, label='Solar Energy', color='green', linestyle='--', linewidth=2)
plt.plot(years, wind_energy, label='Wind Energy', color='green', linestyle='-.', linewidth=2)

# Title and labels
plt.title('Energy Consumption Evolution (2000-2022)\nThe Rise of Renewable Sources', fontsize=16)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Energy Consumption (GWh)', fontsize=12)

# Adding annotations for key years of change
key_years = {
    2007: 'Start of Solar Investment', 2013: 'Wind Farm Setup', 2020: 'Major Shift to Renewables'
}
for year, event in key_years.items():
    plt.annotate(event, xy=(year, (solar_energy[year-2000] + wind_energy[year-2000]) / 2), 
                 xytext=(year, (solar_energy[year-2000] + wind_energy[year-2000]) / 2 + 10),
                 arrowprops=dict(arrowstyle='->', color='grey'), fontsize=9, ha='center')

# Highlight Data Points with a single color
plt.scatter(years, traditional_energy, color='green', s=50, edgecolors='black', alpha=0.7)
plt.scatter(years, solar_energy, color='green', s=50, edgecolors='black', alpha=0.7)
plt.scatter(years, wind_energy, color='green', s=50, edgecolors='black', alpha=0.7)

# Legend and Grid
plt.legend(loc='upper right', fontsize=10, title='Energy Sources')
plt.grid(True, linestyle='--', alpha=0.7)

# Custom x-ticks for better visibility
plt.xticks(np.arange(2000, 2023, 2), fontsize=10, rotation=45)
plt.yticks(fontsize=10)

# Adjust layout to prevent overlap
plt.tight_layout()

# Show the plot
plt.show()