import matplotlib.pyplot as plt
import numpy as np

# Backstory: Analysis of annual productivity of different tea plantations in the serene region of Misty Valleys.
# The productivity is measured in terms of kilograms of tea produced over the last five years.

# Plantations and their corresponding tea production in kilograms for the years 2018-2022
plantations = ['Greenleaf', 'Sunrise Estates', 'Whispering Pines', 'Mountain View', 'Golden Harvest']
years = ['2018', '2019', '2020', '2021', '2022']

# Production data in kg (rows: plantations, columns: years)
production_data = np.array([
    [1100, 1150, 1200, 1180, 1250],  # Greenleaf
    [950, 1020, 980, 1050, 1100],    # Sunrise Estates
    [750, 780, 800, 810, 850],       # Whispering Pines
    [1300, 1280, 1330, 1350, 1400],  # Mountain View
    [890, 920, 950, 980, 1000]       # Golden Harvest
])

# Sum the total production for each plantation
total_production = np.sum(production_data, axis=1)

# Calculate the average annual production
average_production = np.mean(production_data, axis=1)

# Create the plot
fig, ax1 = plt.subplots(figsize=(14, 8))

# Bar chart for total production
colors = ['#4c7b7b', '#6a9e9e', '#84bab8', '#a1cfde', '#d2e3e4']
bars = ax1.barh(plantations, total_production, color=colors, edgecolor='black', height=0.6)

# Annotate bars with total production
for bar in bars:
    width = bar.get_width()
    ax1.text(width + 10, bar.get_y() + bar.get_height()/2, f'{width} kg', va='center', fontsize=10, fontweight='bold')

# Set titles and labels
ax1.set_title("Tea Production in Misty Valleys (2018-2022)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel("Total Production (kg)", fontsize=12)
ax1.xaxis.grid(True, linestyle='--', alpha=0.6)
ax1.set_xlim(0, 7000)

# Create secondary axis for average annual production
ax2 = ax1.twiny()
ax2.plot(average_production, plantations, color='navy', marker='o', linestyle='--', label='Avg Annual Production (kg)')
ax2.set_xlabel('Average Annual Production (kg)', fontsize=12)
ax2.set_xlim(700, 1500)  # Adjust limits based on average production values

# Add a legend
ax2.legend(loc='upper right', fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()