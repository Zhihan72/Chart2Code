import matplotlib.pyplot as plt
import numpy as np

# Define the years for the x-axis
years = np.arange(2010, 2021)

# Data: Renewable energy production in TWh for various regions
north_america_renewable = [50, 70, 110, 150, 200, 260, 330, 410, 500, 600, 710]
europe_renewable = [60, 80, 100, 140, 200, 280, 360, 450, 550, 670, 800]
asia_renewable = [40, 60, 90, 130, 180, 240, 310, 390, 480, 580, 690]
south_america_renewable = [20, 30, 50, 75, 110, 150, 200, 260, 330, 410, 500]

data = np.array([
    north_america_renewable,
    europe_renewable,
    asia_renewable,
    south_america_renewable
])

# Creating the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))

# Stackplot for renewable energy sources
ax.stackplot(
    years, data, labels=[
        'North America', 'Europe', 'Asia', 'South America'
    ],
    colors=['#1f77b4', '#ff7f0e', '#2ca02c', '#9467bd'], alpha=0.85
)

# Titles, labels, and legend
ax.set_title(
    "A Decade of Renewable Energy Growth:\nContribution by Region (2010-2020)",
    fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Renewable Energy Production (TWh)", fontsize=14)
ax.legend(loc='upper left', title="Regions", fontsize=10, bbox_to_anchor=(1, 1))

# Adding grid lines
ax.grid(True, linestyle='--', alpha=0.6)

# Annotating significant growth points
ax.annotate('N. America surpasses 500 TWh', xy=(2019, 500), xytext=(2015, 350),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')
ax.annotate('Rapid growth in Asia', xy=(2016, 240), xytext=(2017, 400),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10, fontweight='bold')

# Ensuring a good layout to avoid overlap
fig.tight_layout()

# Displaying the plot
plt.show()