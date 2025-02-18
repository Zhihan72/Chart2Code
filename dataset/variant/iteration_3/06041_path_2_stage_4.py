import matplotlib.pyplot as plt

pollutants_data = {
    "City A": [22, 24, 21, 23, 25, 26, 29, 31, 30, 20, 22, 19, 18, 24, 27],
    "City B": [17, 18, 16, 20, 19, 15, 17, 16, 21, 22, 20, 21, 20, 22, 24],
    "City C": [34, 35, 33, 32, 34, 36, 39, 37, 38, 36, 35, 38, 32, 34, 33],
    "City D": [27, 28, 29, 30, 32, 31, 28, 29, 30, 27, 26, 25, 28, 29, 31],
    "City E": [14, 15, 13, 12, 16, 17, 13, 14, 12, 11, 10, 14, 15, 16, 17],
    "City F": [19, 23, 21, 22, 20, 18, 19, 21, 23, 20, 20, 21, 22, 19, 18]  # New data series
}

data = [pollutants_data[city] for city in pollutants_data]
cities = list(pollutants_data.keys())

fig, ax = plt.subplots(figsize=(8, 8))

ax.boxplot(data, vert=False, patch_artist=True)

ax.set_yticklabels(cities, fontsize=12)
ax.set_xlabel('PM2.5 Concentration (µg/m³)', fontsize=12)
ax.set_ylabel('Cities', fontsize=12)

plt.tight_layout(pad=3.0)
plt.show()