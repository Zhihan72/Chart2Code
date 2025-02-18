import matplotlib.pyplot as plt
import numpy as np

# Backstory: Tracking the Environmental Sustainability Efforts in "EcoVille" city
# since 2005, highlighting contributions from various sustainability programs.
# The data includes waste reduction, water conservation, green energy adoption,
# community awareness projects, and urban greenery expansions.

# Years
years = np.arange(2005, 2021)

# Data for sustainability efforts in EcoVille (in arbitrary units)
waste_reduction = [5, 7, 9, 12, 15, 18, 22, 26, 30, 35, 40, 46, 52, 59, 65, 72]
water_conservation = [3, 4, 5, 7, 9, 12, 15, 19, 23, 28, 33, 39, 45, 52, 59, 67]
green_energy = [1, 2, 3, 5, 7, 10, 14, 19, 25, 32, 40, 49, 59, 70, 82, 95]
community_awareness = [2, 3, 4, 6, 8, 10, 13, 16, 20, 24, 29, 35, 41, 48, 56, 65]
urban_greenery = [2, 3, 5, 8, 11, 15, 19, 24, 30, 37, 44, 52, 61, 71, 82, 94]

# Aggregated data for the stacked area chart
sustainability_efforts = np.vstack([waste_reduction, water_conservation, green_energy, community_awareness, urban_greenery])

# Plotting setup
fig, ax = plt.subplots(figsize=(12, 8))

# Stacked area plot
ax.stackplot(years, sustainability_efforts,
             labels=['Waste Reduction', 'Water Conservation', 'Green Energy', 'Community Awareness', 'Urban Greenery'],
             colors=['#33A1C9', '#76C1A1', '#FFD33C', '#FF5733', '#C70039'], alpha=0.8)

# Customizing plot appearance
ax.set_title("EcoVille's Sustainability Efforts (2005-2020)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Impact Units (Arbitrary)', fontsize=14)

# Adding x-ticks and customizing y-ticks
ax.set_xticks(np.arange(2005, 2021, 1))
ax.set_yticks(np.arange(0, 301, 50))

# Rotate x-axis labels to avoid overlap
plt.xticks(rotation=45)

# Adding a legend
ax.legend(loc='upper left', fontsize=12, title="Sustainability Programs")

# Adding grid lines for better readability
ax.grid(True, linestyle='--', alpha=0.6)

# Adding annotations for major milestones
milestones = {
    2007: "Recycling Program Launched",
    2010: "Water Conservation Campaign",
    2014: "Major Solar Installations",
    2018: "Massive Tree Planting Drive"
}

for year, event in milestones.items():
    plt.annotate(event, xy=(year, 10), xytext=(year, 100),
                 arrowprops=dict(facecolor='black', shrink=0.05),
                 fontsize=10, ha='center', backgroundcolor='white')

# Automatically adjust layout to prevent label overlap
plt.tight_layout()

# Display the plot
plt.show()