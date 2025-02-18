import matplotlib.pyplot as plt
import numpy as np

# Backstory: The data represents the atmospheric CO2 concentration measured at Mauna Loa Observatory from 1960 to 2020.
# This period captures the steady increase in CO2 concentration over the years, demonstrating the effect of human activities on climate change.

# Define the years (1960 to 2020)
years = np.arange(1960, 2021)

# CO2 concentrations (measured in parts per million) - fictional, hand-crafted data following an upward trend
co2_levels = [
    316, 317, 318, 319, 320, 321, 322, 323, 325, 326,
    327, 329, 330, 331, 332, 333, 335, 336, 337, 338,
    339, 340, 341, 342, 344, 345, 347, 348, 350, 351,
    353, 355, 356, 358, 359, 361, 363, 365, 367, 369,
    371, 373, 375, 377, 379, 381, 384, 386, 388, 390,
    392, 395, 397, 400, 403, 405, 407, 410, 412, 415,
    417
]

# Create subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the CO2 levels as a line
ax.plot(years, co2_levels, color='darkred', linestyle='-', marker='o', markersize=5, linewidth=2, label='CO2 Levels')

# Setting the title and labels
ax.set_title('Atmospheric CO2 Concentration\nMeasured at Mauna Loa Observatory (1960-2020)', fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('CO2 Concentration (ppm)', fontsize=14)

# Legend for the line plot
ax.legend(loc='upper left', fontsize=12)

# Adding grid lines for better visualization
ax.grid(True, linestyle='--', alpha=0.6)

# Highlighting specific milestones with vertical lines and annotations
milestones = {
    1960: 'Start of Measurements',
    1992: 'Earth Summit',
    1997: 'Kyoto Protocol',
    2015: 'Paris Agreement',
    2020: 'Recent Measurement'
}

for year, event in milestones.items():
    plt.axvline(x=year, color='grey', linestyle='--', linewidth=1.5, alpha=0.7)
    plt.text(year + 0.5, co2_levels[years.tolist().index(year)] + 3, event, rotation=90, verticalalignment='center', fontsize=10, color='grey', alpha=0.7)

# Set tick parameters for better clarity
ax.set_xticks(np.arange(1960, 2021, 5))
ax.set_yticks(np.arange(300, 450, 10))

# Automatically adjust layout to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()