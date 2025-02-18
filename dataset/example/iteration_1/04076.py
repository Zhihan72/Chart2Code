import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are visualizing the land area dedicated to different types of agriculture over time in a fictional country.
# The chart illustrates the shift in agricultural focus from traditional to more modern practices.

# Define the years for the x-axis
years = np.arange(1990, 2015)

# Define the amount of land in millions of hectares dedicated to each type of agriculture over the years
traditional_agriculture = np.array([50, 48, 45, 43, 40, 37, 35, 33, 30, 28, 25, 23, 20, 18, 15, 13, 10, 8, 6, 4, 2, 0, 0, 0, 0])
organic_farming = np.array([2, 3, 4, 5, 6, 7, 9, 11, 13, 15, 18, 20, 23, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 45, 47])
hydroponics = np.array([0, 0, 0, 1, 2, 3, 4, 6, 8, 10, 12, 14, 17, 19, 22, 24, 26, 28, 30, 32, 35, 38, 41, 44, 47])
vertical_farming = np.array([0, 0, 0, 0, 0, 1, 1, 2, 3, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 35])

# Calculate the total agricultural land over the years
total_agriculture = (traditional_agriculture + organic_farming + hydroponics + vertical_farming)

# Create a figure and multiple subplots
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the stacked area chart
ax.stackplot(years, traditional_agriculture, organic_farming, hydroponics, vertical_farming,
             labels=['Traditional Agriculture', 'Organic Farming', 'Hydroponics', 'Vertical Farming'],
             colors=['#ffcc99', '#66b3ff', '#99ff99', '#ff9999'], alpha=0.85)

# Overlay a line plot for the total agricultural land
ax.plot(years, total_agriculture, label='Total Agricultural Land', color='black', linestyle='--', marker='o')

# Add plot titles and labels
ax.set_title("Shifts in Agricultural Land Use\nFrom Traditional to Modern Practices (1990-2015)", fontsize=18, fontweight='bold')
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Agricultural Land (Millions of Hectares)", fontsize=14)

# Customize ticks and grid
ax.set_xticks(years[::2])
ax.set_yticks(np.arange(0, 101, 10))
ax.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

# Customize legend
ax.legend(loc='upper left', fontsize=12)

# Add annotations to highlight significant points
ax.annotate('Start of Hydroponics', xy=(2001, 2), xytext=(1995, 10),
            arrowprops=dict(arrowstyle='->', color='black'), fontsize=12, color='black')
ax.annotate('Rapid growth in Vertical Farming', xy=(2015, 16), xytext=(2012, 30),
            arrowprops=dict(arrowstyle='->', color='black'), fontsize=12, color='black')

# Automatically adjust layout for better readability
fig.tight_layout()

# Display the plot
plt.show()