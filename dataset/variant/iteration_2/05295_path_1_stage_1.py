import matplotlib.pyplot as plt
import numpy as np

# Defining the years
years = np.arange(2010, 2021)

# Altering the number of sightings for each species over the years while preserving the dimensionality
mammals = np.array([235, 245, 255, 255, 245, 225, 230, 220, 215, 230, 240])
birds = np.array([310, 330, 340, 380, 390, 425, 415, 420, 435, 455, 470])
reptiles = np.array([78, 86, 89, 91, 96, 91, 87, 93, 95, 95, 101])
amphibians = np.array([152, 158, 162, 168, 169, 172, 183, 182, 188, 196, 198])
insects = np.array([505, 525, 535, 555, 575, 610, 615, 650, 655, 675, 695])

# Stack data for the area chart
data = np.array([mammals, birds, reptiles, amphibians, insects])
data_stack = np.cumsum(data, axis=0)

# Create the plot
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the areas
ax.fill_between(years, 0, data_stack[0], label='Mammals', color='lightcoral', alpha=0.8)
ax.fill_between(years, data_stack[0], data_stack[1], label='Birds', color='gold', alpha=0.7)
ax.fill_between(years, data_stack[1], data_stack[2], label='Reptiles', color='lightgreen', alpha=0.6)
ax.fill_between(years, data_stack[2], data_stack[3], label='Amphibians', color='skyblue', alpha=0.5)
ax.fill_between(years, data_stack[3], data_stack[4], label='Insects', color='orchid', alpha=0.4)

# Add title and labels
ax.set_title("Annual Species Observation in the Grand Wildlife Reserve\n(2010-2020)", fontsize=16, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Number of Sightings", fontsize=12)

# Rotate x-axis labels to avoid overlapping
ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45, fontsize=10)

# Add gridlines for better readability
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Add legend with clear identification
ax.legend(loc='upper left', fontsize=10, title='Species', title_fontsize='12')

# Adjust layout to prevent overlap and improve visual appeal
plt.tight_layout()

# Display the chart
plt.show()