import matplotlib.pyplot as plt
import numpy as np

# Backstory: We are analyzing the usage of different modes of transportation over the past decade in the city of Metroville.
# The modes of transportation we are tracking include: Cars, Bicycles, Public Transit, and Walking.

# Define the years
years = np.arange(2013, 2023)

# Transportation usage data (in thousands of trips)
cars_usage = [700, 720, 740, 760, 750, 740, 730, 720, 710, 700]
bicycles_usage = [120, 130, 150, 170, 200, 230, 250, 270, 290, 300]
public_transit_usage = [300, 310, 320, 340, 350, 370, 400, 430, 450, 470]
walking_usage = [150, 160, 170, 180, 190, 200, 210, 220, 230, 250]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(14, 8))

# Plot the data
ax.plot(years, cars_usage, label='Cars', marker='o', linestyle='-', linewidth=2, color='royalblue')
ax.plot(years, bicycles_usage, label='Bicycles', marker='s', linestyle='-', linewidth=2, color='forestgreen')
ax.plot(years, public_transit_usage, label='Public Transit', marker='^', linestyle='-', linewidth=2, color='firebrick')
ax.plot(years, walking_usage, label='Walking', marker='d', linestyle='-', linewidth=2, color='goldenrod')

# Set chart titles and labels
ax.set_title('Trends in Transportation Mode Usage in Metroville\n(2013-2022)', fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel('Year', fontsize=14)
ax.set_ylabel('Number of Trips (Thousands)', fontsize=14)
ax.set_xticks(years)
ax.set_ylim(0, 800)

# Add gridlines
ax.grid(True, linestyle='--', alpha=0.5)

# Add legends
ax.legend(title='Modes of Transportation', loc='upper left')

# Annotate significant trends
ax.annotate('Surge in Bicycle Usage', xy=(2017, 200), xytext=(2015, 300),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Steady Growth in Public Transit', xy=(2018, 430), xytext=(2017, 550),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)
ax.annotate('Decrease in Car Trips', xy=(2016, 740), xytext=(2014, 780),
            arrowprops=dict(facecolor='black', arrowstyle='->'), fontsize=10)

# Adjust layout to prevent overlapping
plt.tight_layout()

# Display the plot
plt.show()