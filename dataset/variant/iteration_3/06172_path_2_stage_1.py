import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2000, 2023)

# Energy consumption data (in GWh)
traditional_energy = np.array([120, 118, 115, 113, 110, 107, 104, 100, 97, 94, 91, 88, 85, 83, 80, 78, 76, 74, 72, 70, 67, 65, 60])
solar_energy = np.array([0, 0, 0, 0, 0, 0, 0, 2, 4, 6, 8, 10, 12, 16, 20, 25, 30, 35, 40, 50, 55, 60, 65])
wind_energy = np.array([0, 0, 0, 0, 0, 0, 0, 1, 3, 5, 7, 10, 13, 18, 23, 30, 38, 47, 55, 60, 65, 70, 75])

# Plot setup
plt.figure(figsize=(14, 8))

# Plot the data
plt.plot(years, traditional_energy, color='brown', linestyle='-', linewidth=2)
plt.plot(years, solar_energy, color='orange', linestyle='--', linewidth=2)
plt.plot(years, wind_energy, color='cyan', linestyle='-.', linewidth=2)

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

# Highlight Data Points
plt.scatter(years, traditional_energy, color='brown', s=50, edgecolors='black', alpha=0.7)
plt.scatter(years, solar_energy, color='orange', s=50, edgecolors='black', alpha=0.7)
plt.scatter(years, wind_energy, color='cyan', s=50, edgecolors='black', alpha=0.7)

# Custom x-ticks for better visibility
plt.xticks(np.arange(2000, 2023, 2), fontsize=10, rotation=45)
plt.yticks(fontsize=10)

# Remove borders
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_visible(False)

# Show the plot
plt.show()