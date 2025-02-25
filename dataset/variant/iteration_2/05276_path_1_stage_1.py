import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Participation rates (%)
hiking_east = [15, 18, 20, 22, 25, 28, 30, 35, 38, 40, 45]
cycling_east = [5, 7, 10, 12, 15, 20, 25, 28, 30, 33, 35]
running_east = [12, 15, 17, 20, 24, 28, 33, 37, 42, 45, 47]

# Create a single subplot for the Eastern Region
fig, ax = plt.subplots(figsize=(12, 6))

# Plot for the Eastern Region
ax.plot(years, hiking_east, marker='o', color='green', linestyle='-', linewidth=2,
        label='Hiking (East)')
ax.plot(years, cycling_east, marker='s', color='blue', linestyle='-', linewidth=2,
        label='Cycling (East)')
ax.plot(years, running_east, marker='^', color='red', linestyle='-', linewidth=2,
        label='Running (East)')
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Participation Rate (%)', fontsize=14)
ax.set_title('Outdoor Activity Participation in the Eastern Region (2010-2020)', fontsize=16, weight='bold')
ax.legend(loc='upper left')
ax.grid(True, alpha=0.3)

# Adjust layout and show the plot
plt.tight_layout(pad=2.0)
plt.show()