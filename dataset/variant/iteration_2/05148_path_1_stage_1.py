import numpy as np
import matplotlib.pyplot as plt

# Data
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
weekday_rides = np.array([50, 55, 60, 62, 67, 75, 85, 90, 95, 100])
weekend_rides = np.array([30, 35, 38, 40, 45, 50, 55, 60, 58, 62])
total_rides = weekday_rides + weekend_rides

cumulative_weekday = np.cumsum(weekday_rides)
cumulative_weekend = np.cumsum(weekend_rides)

# Initialize figure and subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

# First subplot
ax1.plot(years, weekday_rides, marker='*', linestyle='-.', color='purple', label='Weekday Rides')
ax1.plot(years, weekend_rides, marker='x', linestyle='--', color='orange', label='Weekend Rides')
ax1.plot(years, total_rides, marker='h', linestyle='-', color='green', label='Total Rides')

ax1.set_title('Annual Bicycle Rides in EcoCity (2013-2022)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Rides (in thousands)', fontsize=12)
ax1.legend(loc='best', fontsize=10)
ax1.grid(visible=False)

# Annotations
ax1.annotate('Launch of bike-sharing program', xy=(2015, 60), xytext=(2016, 80),
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='red', facecolor='yellow'),
             arrowprops=dict(facecolor='grey', arrowstyle='->'),
             fontsize=10, color='brown')

ax1.annotate('COVID-19 Pandemic', xy=(2020, 90), xytext=(2017, 120),
             bbox=dict(boxstyle='round,pad=0.6', edgecolor='black', facecolor='pink'),
             arrowprops=dict(facecolor='purple', arrowstyle='->'),
             fontsize=10, color='blue')

# Second subplot
ax2.plot(years, cumulative_weekday, marker='v', linestyle='-', color='blue', label='Cumulative Weekday Rides')
ax2.plot(years, cumulative_weekend, marker='D', linestyle=':', color='red', label='Cumulative Weekend Rides')

ax2.set_title('Cumulative Bicycle Rides in EcoCity (2013-2022)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Cumulative Rides (in thousands)', fontsize=12)
ax2.legend(loc='upper center', fontsize=10)
ax2.grid(visible=True, linestyle='-.', alpha=0.7)

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()