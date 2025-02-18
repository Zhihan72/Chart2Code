import matplotlib.pyplot as plt
import numpy as np

# Years of data collection
years = np.arange(2010, 2021)

# Simulated data for different types of crops (in thousand tonnes)
wheat_harvest = np.array([500, 520, 530, 545, 560, 570, 590, 610, 625, 640, 660])
corn_harvest = np.array([450, 460, 480, 500, 515, 530, 550, 570, 590, 610, 630])
rice_harvest = np.array([380, 400, 420, 435, 455, 475, 490, 505, 520, 540, 560])
barley_harvest = np.array([200, 210, 220, 225, 230, 240, 250, 260, 270, 280, 290])

# Creating the figure and subplot
fig, ax = plt.subplots(figsize=(14, 8))

# Consistent single color for all stacks
color = 'steelblue'

# Stacked area plot
ax.fill_between(years, 0, wheat_harvest, color=color, alpha=0.7, label='Wheat')
ax.fill_between(years, wheat_harvest, wheat_harvest + corn_harvest, color=color, alpha=0.7, label='Corn')
ax.fill_between(years, wheat_harvest + corn_harvest, wheat_harvest + corn_harvest + rice_harvest, color=color, alpha=0.7, label='Rice')
ax.fill_between(years, wheat_harvest + corn_harvest + rice_harvest, 
                wheat_harvest + corn_harvest + rice_harvest + barley_harvest, 
                color=color, alpha=0.7, label='Barley')

# Set title and labels
ax.set_title("Annual Harvest Quantities of Various Crops in AgroLand (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Harvest Quantity (thousand tonnes)", fontsize=12)

# Configure x-axis ticks
plt.xticks(years, rotation=45, ha="right")

# Add legend
ax.legend(loc='upper left', title='Crop Types')

# Improve readability with grid lines
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.grid(axis='y', linestyle='--', alpha=0.3)

# Automatically adjust layout
plt.tight_layout()

# Display the plot
plt.show()