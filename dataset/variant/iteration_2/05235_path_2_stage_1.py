import matplotlib.pyplot as plt
import numpy as np

# Define the years for the data
years = np.arange(2010, 2021)

# Number of EVs adopted in thousands in different regions
north_region = np.array([1, 2, 4, 8, 15, 25, 38, 50, 70, 85, 100])
south_region = np.array([0, 1, 2, 5, 10, 18, 28, 37, 50, 60, 75])
east_region = np.array([0, 0, 1, 4, 7, 12, 20, 28, 39, 49, 60])
west_region = np.array([0, 0, 0, 1, 4, 8, 14, 22, 32, 44, 55])

# Create an area chart
fig, ax = plt.subplots(figsize=(14, 8))

# Plotting the areas with varied marker types (not applicable to area chart, but simulated through hatch patterns)
ax.stackplot(years, north_region, south_region, east_region, west_region,
             labels=['North Region', 'South Region', 'East Region', 'West Region'],
             colors=['#FFD700', '#98FB98', '#AFEEEE', '#FF6347'], alpha=0.8, 
             edgecolor='black', linewidth=0.5, hatch=['/', '\\', '|', '-'])

# Set title and labels
ax.set_title("Adoption of Electric Vehicles in Greentopia (2010-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Years", fontsize=12)
ax.set_ylabel("EVs Adopted (in Thousands)", fontsize=12)
ax.set_xlim(years.min(), years.max())
ax.set_ylim(0, 220)

# Adding a grid with a different style
ax.grid(True, linestyle=':', color='gray', alpha=0.7)

# Randomly changing the legend style
ax.legend(title="Regions", loc="upper right", fontsize=11, frameon=True, shadow=True, facecolor='lightgray')

# Adding annotations for key milestones with varied style
ax.annotate('Green Transport Policy Launch', xy=(2015, 12), xytext=(2013, 70),
            arrowprops=dict(arrowstyle='->', connectionstyle='angle3', color='red'), fontsize=10)
ax.annotate('Significant Growth Phase', xy=(2018, 130), xytext=(2017, 180),
            arrowprops=dict(arrowstyle='-|>', connectionstyle='arc3', color='blue'), fontsize=10)

# Rotate x-axis labels if needed to avoid overlap
plt.xticks(rotation=45)

# Adjust layout to fit everything
plt.tight_layout()

# Show plot
plt.show()