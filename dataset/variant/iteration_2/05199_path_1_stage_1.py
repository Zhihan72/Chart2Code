import matplotlib.pyplot as plt
import numpy as np

# Years
years = np.arange(2015, 2026)

# Data for each storage type (in gigawatt hours)
batteries = [0.5, 1, 2, 4, 6, 10, 15, 22, 30, 40, 52]
pumped_storage = [5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 22]
compressed_air = [0.2, 0.3, 0.5, 0.9, 1.2, 1.5, 2, 2.5, 3, 3.5, 4]

# Updated storage data (Removed "Flywheels")
storage_data = np.array([batteries, pumped_storage, compressed_air])

# Colors for each storage type
colors = ['#76C7C0', '#FFB74D', '#FF8A80']

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, storage_data, labels=["Batteries", "Pumped-Storage Hydropower", "Compressed Air"], 
             colors=colors, alpha=0.8)

# Title, labels, and legend
ax.set_title("Growth of Renewable Energy Storage Solutions\nfrom 2015 to 2025", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Storage Capacity (Gigawatt Hours)", fontsize=12)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 90)
ax.set_xticks(years)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)} GWh'))

# Add legend
ax.legend(loc='upper left', title="Storage Types", bbox_to_anchor=(1.02, 1), fontsize=10, frameon=False)

# Grid for y-axis
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plot
plt.show()