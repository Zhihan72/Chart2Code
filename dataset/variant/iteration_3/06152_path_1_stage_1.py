import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solartech_production = [15, 22, 33, 40, 45, 50, 55, 60, 65, 70, 75]
sundrive_production = [10, 16, 25, 32, 38, 48, 52, 55, 58, 63, 67]
ecowheels_production = [5, 10, 18, 28, 36, 40, 45, 50, 55, 60, 65]

fig, ax = plt.subplots(figsize=(12, 8))

# Plot the production lines
ax.plot(years, solartech_production, marker='o', linestyle='-', linewidth=2, color='gold')
ax.plot(years, sundrive_production, marker='s', linestyle='-', linewidth=2, color='darkorange')
ax.plot(years, ecowheels_production, marker='^', linestyle='-', linewidth=2, color='forestgreen')

# Add titles and labels
ax.set_title("The Journey of Solar-Powered Car Production (2010-2020)", fontsize=18, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Number of Cars Produced (in thousands)", fontsize=14)

# Customize the x and y axis
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(0, 101, 10))
ax.set_yticklabels([f'{i}k' for i in range(0, 101, 10)])

# Annotate the data points
for i in range(len(years)):
    ax.text(years[i], solartech_production[i], f"{solartech_production[i]}k", ha='center', va='bottom', fontsize=10, color='gold')
    ax.text(years[i], sundrive_production[i], f"{sundrive_production[i]}k", ha='center', va='bottom', fontsize=10, color='darkorange')
    ax.text(years[i], ecowheels_production[i], f"{ecowheels_production[i]}k", ha='center', va='bottom', fontsize=10, color='forestgreen')

# Automatically adjust layout to avoid overlap
plt.tight_layout()

# Show the plot
plt.show()