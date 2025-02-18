import matplotlib.pyplot as plt
import numpy as np

pollutants_data = {
    "City A": [22, 24, 21, 23, 25, 26, 29, 31, 30, 20, 22, 19, 18, 24, 27],
    "City B": [17, 18, 16, 20, 19, 15, 17, 16, 21, 22, 20, 21, 20, 22, 24],
    "City C": [34, 35, 33, 32, 34, 36, 39, 37, 38, 36, 35, 38, 32, 34, 33],
    "City D": [27, 28, 29, 30, 32, 31, 28, 29, 30, 27, 26, 25, 28, 29, 31],
    "City E": [14, 15, 13, 12, 16, 17, 13, 14, 12, 11, 10, 14, 15, 16, 17],
    "City F": [42, 40, 43, 41, 44, 45, 43, 46, 44, 45, 47, 41, 42, 45, 43],
    "City G": [10, 9, 11, 8, 12, 13, 9, 10, 9, 7, 8, 11, 10, 12, 13],
    "City H": [30, 32, 31, 33, 35, 34, 36, 37, 34, 33, 32, 31, 36, 35, 37]
}

data = [pollutants_data[city] for city in pollutants_data]
cities = list(pollutants_data.keys())

fig, ax = plt.subplots(figsize=(10, 10))
fig.suptitle('Pollutant Level Monitoring Across Major Cities (Last 6 Months)', fontsize=16, weight='bold', y=1.02)

ax.boxplot(data, patch_artist=True, notch=False, vert=False, widths=0.7,
           boxprops=dict(facecolor='lavender', color='purple'),
           whiskerprops=dict(color='purple'), capprops=dict(color='purple'),
           medianprops=dict(color='red', linewidth=1))

colors = ['cyan', 'lightgoldenrodyellow', 'lightgreen', 'lightcoral', 'lightblue', 'lightsalmon', 'lightgray', 'lightpink']

for patch, color in zip(ax.boxplot(data, patch_artist=True, vert=False)['boxes'], colors):
    patch.set_facecolor(color)

for i, city_data in enumerate(data, start=1):
    y_values = np.full(len(city_data), i) + np.random.normal(0, 0.04, size=len(city_data))
    ax.scatter(city_data, y_values, alpha=0.7, color='red', edgecolor='none', label='Data Points' if i == 1 else "")

ax.set_title('Distribution of Pollutant Levels', fontsize=14, pad=20)
ax.set_ylabel('Cities', fontsize=12)
ax.set_xlabel('PM2.5 Concentration (µg/m³)', fontsize=12)
ax.set_yticks(np.arange(1, len(cities) + 1))
ax.set_yticklabels(cities, rotation=45)
ax.grid(False)
ax.legend(loc='lower right')

plt.tight_layout(pad=3.0)
plt.show()