import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)

residential_population = [1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.3, 2.5, 2.9, 3.1]
green_space = [50, 55, 60, 70, 75, 80, 85, 90, 95, 100]
public_transport_usage = [100, 110, 120, 150, 160, 170, 175, 180, 185, 190]
energy_consumption = [5.0, 5.1, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6]
average_commute_time = [40, 38, 37, 35, 33, 32, 30, 29, 28, 27]

fig, ax = plt.subplots(figsize=(14, 8))

# Applying the same color 'blue' to all data groups
ax.plot(years, residential_population, marker='o', color='blue', label='Residential Population (millions)')
ax.plot(years, green_space, marker='s', color='blue', label='Green Space (sq. km)')
ax.plot(years, public_transport_usage, marker='^', color='blue', label='Public Transport Usage (millions of rides/year)')
ax.plot(years, energy_consumption, marker='d', color='blue', label='Energy Consumption (terawatt-hours)')
ax.plot(years, average_commute_time, marker='x', color='blue', label='Average Commute Time (minutes)')

plt.title('Decade of Progress: Urban Development in Metropolis (2010-2019)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Metrics', fontsize=14)
plt.legend(loc='upper left', fontsize=12)
plt.xticks(years, fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()