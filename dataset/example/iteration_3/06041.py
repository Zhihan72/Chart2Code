import matplotlib.pyplot as plt
import numpy as np

# Backstory: A local environmental agency is monitoring the levels of different pollutants in five major cities. 
# The data collected over a six-month period illustrates the variability and distribution of these pollutants.

# Pollutant data for each city (PM2.5 concentration in µg/m³)
pollutants_data = {
    "City A": [22, 24, 21, 23, 25, 26, 29, 31, 30, 20, 22, 19, 18, 24, 27],
    "City B": [17, 18, 16, 20, 19, 15, 17, 16, 21, 22, 20, 21, 20, 22, 24],
    "City C": [34, 35, 33, 32, 34, 36, 39, 37, 38, 36, 35, 38, 32, 34, 33],
    "City D": [27, 28, 29, 30, 32, 31, 28, 29, 30, 27, 26, 25, 28, 29, 31],
    "City E": [14, 15, 13, 12, 16, 17, 13, 14, 12, 11, 10, 14, 15, 16, 17]
}

# Convert pollutant data into a list format suitable for plotting
data = [pollutants_data[city] for city in pollutants_data]
cities = list(pollutants_data.keys())

# Create the box plot with additional subplot line plot for average pollutant levels over months
fig, ax = plt.subplots(1, 2, figsize=(16, 8))
fig.suptitle('Pollutant Level Monitoring Across Major Cities (Last 6 Months)', fontsize=16, weight='bold', y=1.02)

# Box plot
ax[0].boxplot(data, patch_artist=True, notch=True, vert=True, widths=0.6,
              boxprops=dict(facecolor='lightblue', color='blue'),
              whiskerprops=dict(color='darkblue'), capprops=dict(color='darkblue'),
              medianprops=dict(color='darkred', linewidth=2))

# Colors for each city’s box plot
colors = ['lightgreen', 'lightcoral', 'lightblue', 'lightsalmon', 'lightgoldenrodyellow']
for patch, color in zip(ax[0].boxplot(data, patch_artist=True)['boxes'], colors):
    patch.set_facecolor(color)

# Add individual data points for better visualization
for i, city_data in enumerate(data, start=1):
    x_values = np.full(len(city_data), i) + np.random.normal(0, 0.04, size=len(city_data))
    ax[0].scatter(x_values, city_data, alpha=0.6, color='gray', edgecolor='k', label='Individual Data Points' if i == 1 else "")

ax[0].set_title('Distribution of Pollutant Levels', fontsize=14, pad=20)
ax[0].set_xlabel('Cities', fontsize=12)
ax[0].set_ylabel('PM2.5 Concentration (µg/m³)', fontsize=12)
ax[0].set_xticks(np.arange(1, len(cities) + 1))
ax[0].set_xticklabels(cities, rotation=30)
ax[0].grid(True, linestyle='--', alpha=0.6)
ax[0].legend(loc='upper right')

# Average pollutant levels line plot
months = np.arange(1, 16)  # Assuming data points refer to weeks
average_levels = [np.mean(data[i]) for i in range(len(data))]
for i, city in enumerate(cities):
    ax[1].plot(months, data[i], label=city, marker='o', color=colors[i])

ax[1].set_title('Weekly Average Pollutant Levels', fontsize=14, pad=20)
ax[1].set_xlabel('Weeks', fontsize=12)
ax[1].set_ylabel('PM2.5 Concentration (µg/m³)', fontsize=12)
ax[1].legend(loc='upper left', fontsize=10)
ax[1].grid(True, linestyle='--', alpha=0.7)

# Tight layout to avoid overlapping
plt.tight_layout(pad=3.0)

# Show plot
plt.show()