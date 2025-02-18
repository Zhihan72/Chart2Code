import numpy as np
import matplotlib.pyplot as plt

# Data
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
weekday_rides = np.array([50, 55, 60, 62, 67, 75, 85, 90, 95, 100])
weekend_rides = np.array([30, 35, 38, 40, 45, 50, 55, 60, 58, 62])
total_rides = weekday_rides + weekend_rides

# Initialize figure
fig, ax1 = plt.subplots(figsize=(8, 8))

# Plot
ax1.plot(years, weekday_rides, marker='*', linestyle='-.', color='blue', label='Weekday Rides')
ax1.plot(years, weekend_rides, marker='x', linestyle='--', color='red', label='Weekend Rides')
ax1.plot(years, total_rides, marker='h', linestyle='-', color='cyan', label='Total Rides')

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

# Display the plot
plt.show()