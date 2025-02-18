import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# This chart represents the growth of renewable energy storage solutions over the years. 
# We are focusing on four types of storage solutions: Batteries, Pumped-Storage Hydropower, Compressed Air, and Flywheels. 
# The data spans from 2015 to 2025, showcasing the advancements and scaling of these technologies.

# Define the years
years = np.arange(2015, 2026)

# Data for each storage type (in gigawatt hours)
batteries = [0.5, 1, 2, 4, 6, 10, 15, 22, 30, 40, 52]
pumped_storage = [5, 6, 7, 8, 10, 12, 14, 16, 18, 20, 22]
compressed_air = [0.2, 0.3, 0.5, 0.9, 1.2, 1.5, 2, 2.5, 3, 3.5, 4]
flywheels = [0.1, 0.12, 0.15, 0.18, 0.22, 0.26, 0.3, 0.35, 0.4, 0.46, 0.5]

# Compile the data into an array for stacking
storage_data = np.array([batteries, pumped_storage, compressed_air, flywheels])

# Define colors for each storage type
colors = ['#76C7C0', '#FFB74D', '#FF8A80', '#AED581']

# Create the stacked area chart
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, storage_data, labels=["Batteries", "Pumped-Storage Hydropower", "Compressed Air", "Flywheels"], 
             colors=colors, alpha=0.8)

# Customize the plot with title, labels, and legend
ax.set_title("Growth of Renewable Energy Storage Solutions\nfrom 2015 to 2025", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Energy Storage Capacity (Gigawatt Hours)", fontsize=12)
ax.set_xlim(years[0], years[-1])
ax.set_ylim(0, 90)
ax.set_xticks(years)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda y, _: f'{int(y)} GWh'))

# Add legend positioned outside the plot
ax.legend(loc='upper left', title="Storage Types", bbox_to_anchor=(1.02, 1), fontsize=10, frameon=False)

# Enable grid for y-axis
ax.grid(axis='y', linestyle='--', alpha=0.7)

# Adjust layout to prevent overlapping elements
plt.tight_layout()

# Display the plot
plt.show()