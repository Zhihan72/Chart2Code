import matplotlib.pyplot as plt
import numpy as np

# Years from 2010 to 2020
years = np.arange(2010, 2021)

# Resource usage data (in thousands of units)
moon_crystals = np.array([5, 7, 9, 11, 14, 17, 20, 25, 30, 35, 40])
sun_gemstones = np.array([3, 4, 5, 6, 8, 9, 11, 13, 15, 17, 20])
star_dust = np.array([2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20])
sky_pearls = np.array([1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Aggregated data for the stacked area plot
resource_data = np.vstack([moon_crystals, sun_gemstones, star_dust, sky_pearls])

# Create the stacked area plot
fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, resource_data, labels=['Moon Crystals', 'Sun Gemstones', 'Star Dust', 'Sky Pearls'],
             colors=['#FF5733', '#33FF57', '#3357FF', '#FF33A1'], alpha=0.8)

# Title and labels
ax.set_title('Fantasy World Natural Resource Usage in Mythica (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Resource Usage (Thousands of Units)', fontsize=14)

# Add the legend
ax.legend(loc='upper left', fontsize=12, title='Resource Type')

# Customize x and y ticks
ax.set_xticks(years)
ax.set_yticks(np.arange(0, 101, 10))

# Add grid for better readability
ax.yaxis.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Annotate significant points
ax.annotate('Introduction of Moon Crystals', xy=(2015, 14), xytext=(2012, 50),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', backgroundcolor='white')

ax.annotate('Discovery of Star Dust', xy=(2017, 24), xytext=(2018, 60),
            arrowprops=dict(facecolor='black', shrink=0.05),
            fontsize=10, ha='center', backgroundcolor='white')

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()