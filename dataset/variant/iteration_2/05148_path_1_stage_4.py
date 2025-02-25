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
ax1.plot(years, weekday_rides, marker='*', linestyle='-.', color='blue')
ax1.plot(years, weekend_rides, marker='x', linestyle='--', color='red')
ax1.plot(years, total_rides, marker='h', linestyle='-', color='cyan')

# Remove textual elements
ax1.set_xlabel('')
ax1.set_ylabel('')
ax1.set_title('')
ax1.legend().set_visible(False)
ax1.grid(visible=False)

# Remove annotations
# Display the plot
plt.show()