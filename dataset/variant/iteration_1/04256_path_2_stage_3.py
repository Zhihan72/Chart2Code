import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2020)

residential_population = [1.2, 1.3, 1.5, 1.6, 1.8, 2.0, 2.3, 2.5, 2.9, 3.1]
green_space = [50, 55, 60, 70, 75, 80, 85, 90, 95, 100]
public_transport_usage = [100, 110, 120, 150, 160, 170, 175, 180, 185, 190]
average_commute_time = [40, 38, 37, 35, 33, 32, 30, 29, 28, 27]

fig, ax = plt.subplots(figsize=(14, 8))

# Changed marker types and colors
ax.plot(years, residential_population, marker='v', color='red', linestyle='-', label='Residential Population (millions)')
ax.plot(years, green_space, marker='d', color='green', linestyle='-.', label='Green Space (sq. km)')
ax.plot(years, public_transport_usage, marker='h', color='purple', linestyle=':', label='Public Transport Usage (millions of rides/year)')
ax.plot(years, average_commute_time, marker='*', color='orange', linestyle='--', label='Average Commute Time (minutes)')

plt.title('Decade of Progress: Urban Development in Metropolis (2010-2019)', fontsize=18, fontweight='bold', pad=20)
plt.xlabel('Year', fontsize=14)
plt.ylabel('Metrics', fontsize=14)
plt.legend(loc='upper right', fontsize=12)  # Changed legend location
plt.xticks(years, fontsize=12, rotation=45)
plt.yticks(fontsize=12)
plt.grid(True, linestyle='-', alpha=0.5)  # Changed grid linestyle and alpha
ax.spines['top'].set_visible(False)  # Removed the top border
ax.spines['right'].set_visible(False)  # Removed the right border
plt.tight_layout()
plt.show()