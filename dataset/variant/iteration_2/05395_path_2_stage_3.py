import numpy as np
import matplotlib.pyplot as plt

years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
weekday_rides = np.array([50, 55, 60, 62, 67, 75, 85, 90, 95, 100])
cumulative_weekday = np.cumsum(weekday_rides)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))

ax1.plot(years, weekday_rides, marker='o', linestyle='-', color='#ff7f0e')
ax1.set_title('Annual Weekday Bicycle Rides in EcoCity (2013-2022)', fontsize=14, fontweight='bold')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Number of Rides (in thousands)', fontsize=12)

ax1.annotate('Launch of bike-sharing program', xy=(2015, 60), xytext=(2016, 80),
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white'),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='darkred', horizontalalignment='left')

ax1.annotate('COVID-19 Pandemic', xy=(2020, 90), xytext=(2017, 120),
             bbox=dict(boxstyle='round,pad=0.3', edgecolor='gray', facecolor='white'),
             arrowprops=dict(facecolor='black', arrowstyle='->'),
             fontsize=10, color='darkblue', horizontalalignment='center')

ax2.plot(years, cumulative_weekday, marker='o', linestyle='-', color='#ff7f0e')
ax2.set_title('Cumulative Weekday Bicycle Rides in EcoCity (2013-2022)', fontsize=14, fontweight='bold')
ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Cumulative Rides (in thousands)', fontsize=12)

plt.tight_layout()
plt.show()