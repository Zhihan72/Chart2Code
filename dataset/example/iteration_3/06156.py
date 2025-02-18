import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# Imagine analyzing the growth and decline in seafood catches over a decade (2010-2020) for three different fish species in a small coastal town.
# This data visualization hopes to shed light on changes in catch yields due to environmental, economic, and social factors.

# Define years
years = np.arange(2010, 2021)

# Artificial data representing catches in tons for three species of fish
salmon_catches = [120, 135, 150, 160, 155, 140, 130, 145, 165, 180, 190]
tuna_catches = [200, 230, 220, 210, 205, 195, 190, 180, 175, 160, 150]
cod_catches = [300, 320, 310, 305, 295, 280, 270, 260, 255, 250, 240]

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

# Annotation for notable events, e.g., a significant drop in tuna catches
ax1.annotate('Significant drop in Tuna Catches', xy=(2017, 180), xytext=(2014, 250),
             arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
             fontsize=12, color='black')

# Adding some contextual notes on the plot
ax1.text(2011, 190, 'Improved Salmon\nFishing Methods', fontsize=10, ha='center', color='salmon', backgroundcolor='white')
ax1.text(2014, 270, 'Slight Decrease\nDue to Overfishing', fontsize=10, ha='center', color='darkgreen', backgroundcolor='white')

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()