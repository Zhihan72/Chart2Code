import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Analyzing the change in outdoor activity participation rates over the years in different regions
# This study focuses on three popular activities: Hiking, Cycling, and Running.

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Participation rates (%)
hiking_east = [15, 18, 20, 22, 25, 28, 30, 35, 38, 40, 45]
hiking_west = [10, 12, 14, 16, 18, 21, 24, 27, 30, 33, 36]
cycling_east = [5, 7, 10, 12, 15, 20, 25, 28, 30, 33, 35]
cycling_west = [8, 10, 12, 15, 18, 22, 25, 28, 30, 32, 33]
running_east = [12, 15, 17, 20, 24, 28, 33, 37, 42, 45, 47]
running_west = [20, 22, 25, 28, 30, 35, 38, 40, 42, 45, 48]

# Create subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10), sharex=True)

# Plot for the Eastern Region
ax1.plot(years, hiking_east, marker='o', color='green', linestyle='-', linewidth=2,
         label='Hiking (East)')
ax1.plot(years, cycling_east, marker='s', color='blue', linestyle='-', linewidth=2,
         label='Cycling (East)')
ax1.plot(years, running_east, marker='^', color='red', linestyle='-', linewidth=2,
         label='Running (East)')
ax1.set_ylabel('Participation Rate (%)', fontsize=14)
ax1.set_title('Outdoor Activity Participation in the Eastern Region (2010-2020)', fontsize=16, weight='bold')
ax1.legend(loc='upper left')
ax1.grid(True, alpha=0.3)

# Plot for the Western Region
ax2.plot(years, hiking_west, marker='o', color='green', linestyle='-', linewidth=2,
         label='Hiking (West)')
ax2.plot(years, cycling_west, marker='s', color='blue', linestyle='-', linewidth=2,
         label='Cycling (West)')
ax2.plot(years, running_west, marker='^', color='red', linestyle='-', linewidth=2,
         label='Running (West)')
ax2.set_xlabel('Year', fontsize=14)
ax2.set_ylabel('Participation Rate (%)', fontsize=14)
ax2.set_title('Outdoor Activity Participation in the Western Region (2010-2020)', fontsize=16, weight='bold')
ax2.legend(loc='upper left')
ax2.grid(True, alpha=0.3)

# Adding footnotes and adjusting layout
plt.suptitle('Analysis of Outdoor Activity Participation Trends (East vs West)', fontsize=20, weight='bold', y=1.02)
plt.tight_layout(pad=2.0)
plt.show()