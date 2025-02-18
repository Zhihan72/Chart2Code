import matplotlib.pyplot as plt
import numpy as np

pollutants_data = {
    "City A": [22, 24, 21, 23, 25, 26, 29, 31, 30, 20, 22, 19, 18, 24, 27],
    "City B": [17, 18, 16, 20, 19, 15, 17, 16, 21, 22, 20, 21, 20, 22, 24],
    "City C": [34, 35, 33, 32, 34, 36, 39, 37, 38, 36, 35, 38, 32, 34, 33],
    "City D": [27, 28, 29, 30, 32, 31, 28, 29, 30, 27, 26, 25, 28, 29, 31],
    "City E": [14, 15, 13, 12, 16, 17, 13, 14, 12, 11, 10, 14, 15, 16, 17]
}

data = [pollutants_data[city] for city in pollutants_data]
cities = list(pollutants_data.keys())

fig, ax = plt.subplots(figsize=(8, 8))

months = np.arange(1, 16)
colors = ['lightgreen', 'lightcoral', 'lightblue', 'lightsalmon', 'lightgoldenrodyellow']
for i, city in enumerate(cities):
    ax.plot(months, data[i], marker='o', color=colors[i], label=city)

ax.set_xlabel('Weeks', fontsize=12)
ax.set_ylabel('PM2.5 Concentration (µg/m³)', fontsize=12)
ax.legend()

plt.tight_layout(pad=3.0)
plt.show()