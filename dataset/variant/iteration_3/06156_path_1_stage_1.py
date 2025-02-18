import matplotlib.pyplot as plt
import numpy as np

# Define years
years = np.arange(2010, 2021)

# Artificial data representing catches in tons for three species of fish
salmon_catches = [150, 190, 140, 135, 165, 120, 180, 160, 155, 145, 130]
tuna_catches = [180, 200, 210, 230, 150, 160, 205, 220, 195, 175, 190]
cod_catches = [260, 295, 255, 250, 310, 320, 305, 270, 240, 300, 280]

# Creating figure and axis objects
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plotting the data for each species
ax1.plot(years, salmon_catches, marker='o', linestyle='-', linewidth=2, color='salmon', label='Salmon Catches')
ax1.plot(years, tuna_catches, marker='s', linestyle='-', linewidth=2, color='dodgerblue', label='Tuna Catches')
ax1.plot(years, cod_catches, marker='^', linestyle='-', linewidth=2, color='darkgreen', label='Cod Catches')

# Title and labels, formatting accordingly
ax1.set_title("Decadal Analysis of Seafood Catches in Coastal Town (2010-2020)\nUnderstanding Yield Fluctuations", fontsize=18, fontweight='bold', pad=20)
ax1.set_xlabel("Year", fontsize=14)
ax1.set_ylabel("Catch Yield (tons)", fontsize=14)

# Adding grid lines for better readability
ax1.grid(True, linestyle='--', alpha=0.6)

# Displaying legends
ax1.legend(title='Fish Species', fontsize=12, loc='upper left')

# Annotation for notable events
ax1.annotate('Significant drop in Tuna Catches', xy=(2016, 150), xytext=(2013, 250),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=12, color='black')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()