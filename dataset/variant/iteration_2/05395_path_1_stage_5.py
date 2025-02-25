import numpy as np
import matplotlib.pyplot as plt

# Data
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
weekday_rides = np.array([50, 55, 60, 62, 67, 75, 85, 90, 95, 100])
total_rides = weekday_rides  # Remove calculation of total rides that includes weekend_rides

# Initialize figure
fig, ax1 = plt.subplots(figsize=(8, 8))

# Plot
ax1.plot(years, weekday_rides, marker='*', linestyle='-.', color='blue')

# Remove textual elements
ax1.set_xlabel('')
ax1.set_ylabel('')
ax1.set_title('')
ax1.legend().set_visible(False)
ax1.grid(visible=False)

# Display the plot
plt.show()