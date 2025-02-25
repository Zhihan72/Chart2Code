import numpy as np
import matplotlib.pyplot as plt

# Backstory: This line chart shows the annual number of bicycle rides in a hypothetical city, 
# representing the transition towards eco-friendly transportation methods over a decade.

# Years from 2013 to 2022
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])

# Number of bicycle rides in thousands
weekday_rides = np.array([50, 55, 60, 62, 67, 75, 85, 90, 95, 100])
weekend_rides = np.array([30, 35, 38, 40, 45, 50, 55, 60, 58, 62])
total_rides = weekday_rides + weekend_rides

# Cumulative weekday rides
cumulative_weekday = np.cumsum(weekday_rides)
cumulative_weekend = np.cumsum(weekend_rides)

# Initialize the figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# First subplot: Line chart of annual rides
ax1.plot(years, weekday_rides, marker='o', linestyle='-', color='#1f77b4', label='Weekday Rides')
ax1.plot(years, weekend_rides, marker='s', linestyle='-', color='#ff7f0e', label='Weekend Rides')
ax1.plot(years, total_rides, marker='^', linestyle='-', color='#2ca02c', label='Total Rides')

ax1.set_title('Annual Bicycle Rides in EcoCity (2013-2022)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Rides (in thousands)', fontsize=12)
ax1.legend(loc='upper left', fontsize=10)
ax1.grid(visible=True, linestyle='--', alpha=0.5)

# Annotate significant milestones
ax1.annotate('Launch of bike-sharing program', xy=(2015, 60), xytext=(2016, 80),
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white'),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='darkred', horizontalalignment='left')

ax1.annotate('COVID-19 Pandemic', xy=(2020, 90), xytext=(2017, 120),
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white'),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='darkblue', horizontalalignment='center')

# Second subplot: Cumulative rides
ax2.plot(years, cumulative_weekday, marker='o', linestyle='-', color='#1f77b4', label='Cumulative Weekday Rides')
ax2.plot(years, cumulative_weekend, marker='s', linestyle='-', color='#ff7f0e', label='Cumulative Weekend Rides')

ax2.set_title('Cumulative Bicycle Rides in EcoCity (2013-2022)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Cumulative Rides (in thousands)', fontsize=12)
ax2.legend(loc='upper left', fontsize=10)
ax2.grid(visible=True, linestyle='--', alpha=0.5)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()