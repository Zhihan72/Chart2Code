import numpy as np
import matplotlib.pyplot as plt

# Backstory: Tracking the Progress of Self-Driving Car Technology Adoption
# The chart showcases the growth of autonomous vehicles on the road over a decade and the percentage of accidents reduction due to the technology.

# Define the years from 2010 to 2020
years = np.arange(2010, 2021)

# Number of self-driving cars on the road (in thousands)
self_driving_cars = np.array([0.5, 1, 2, 3, 5, 9, 15, 25, 38, 54, 75])

# Number of road accidents (in thousands)
road_accidents = np.array([35, 36, 37, 35, 34, 32, 30, 26, 23, 20, 17])

# Calculate the percentage of accidents reduction
base_accidents = 37  # assuming the highest number of accidents as base
accidents_reduction_percentage = ((base_accidents - road_accidents) / base_accidents) * 100

# Initialize the figure and create subplots
fig, ax1 = plt.subplots(figsize=(14, 8))

# Plot 1: Number of self-driving cars
ax1.plot(years, self_driving_cars, marker='o', color='blue', linewidth=2, label='Self-Driving Cars (in thousands)')
for (x, y) in zip(years, self_driving_cars):
    ax1.text(x, y + 2, f'{y}', ha='center', va='bottom', fontsize=10, color='blue')

# Plot annotations for major milestones
milestones = {2012: "First Large Scale Trials", 2016: "Government Regulations", 
              2018: "Highway Pilots", 2020: "Urban Mobility"}
for year, text in milestones.items():
    ax1.annotate(text, 
                 xy=(year, self_driving_cars[years.tolist().index(year)]),
                 xytext=(year, self_driving_cars[years.tolist().index(year)] + 20),
                 arrowprops=dict(facecolor='grey', shrink=0.05, width=1, headwidth=8),
                 fontsize=10, color='black')

# Add title and labels to the first plot
ax1.set_title('Adoption of Self-Driving Cars and Impact on Road Safety (2010-2020)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Self-Driving Cars (in thousands)', fontsize=12, color='blue')
ax1.set_xticks(years)
ax1.grid(axis='y', linestyle='--', alpha=0.7)

# Secondary Y-Axis for accidents reduction percentage
ax2 = ax1.twinx()
ax2.plot(years, accidents_reduction_percentage, 'r-', linewidth=2, label='Accidents Reduction (%)')
for (x, y) in zip(years, accidents_reduction_percentage):
    ax2.text(x, y - 2, f'{y:.1f}%', ha='center', va='top', fontsize=10, color='red')

ax2.set_ylabel('Accidents Reduction (%)', fontsize=12, color='red')
ax2.tick_params(axis='y', colors='red')

# Adding a legend
ax1.legend(loc='upper left', fontsize=10)
ax2.legend(loc='upper right', fontsize=10)

# Add vertical lines to signify important years
for milestone_year in milestones.keys():
    plt.axvline(x=milestone_year, color='grey', linestyle='--', alpha=0.6)

# Customize grid lines
ax1.grid(linestyle='--', linewidth=0.7, alpha=0.7)

# Automatically adjust the layout for better fit and visibility
plt.tight_layout()

# Show the plot
plt.show()