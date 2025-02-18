import matplotlib.pyplot as plt
import numpy as np

cities = ['San Francisco', 'New York', 'Chicago', 'Houston', 'Phoenix']
celestial_events = ['Meteor Shower', 'Lunar Eclipse', 'Solar Eclipse', 'Comet Sighting', 'Aurora']
observation_data = [
    [12, 4, 1, 6, 2],
    [8, 6, 2, 7, 1],
    [10, 3, 3, 5, 0],
    [7, 5, 2, 9, 3],
    [9, 4, 2, 10, 1]
]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
monthly_sightings = {
    'San Francisco': [1, 2, 1, 1, 1, 2, 3, 0, 0, 1, 0, 0],
    'New York': [1, 1, 1, 2, 1, 1, 2, 0, 1, 0, 1, 0],
    'Chicago': [0, 1, 1, 2, 1, 2, 2, 1, 1, 1, 0, 0],
    'Houston': [1, 1, 2, 2, 1, 0, 2, 1, 2, 1, 0, 0],
    'Phoenix': [0, 1, 1, 2, 2, 0, 2, 2, 1, 1, 0, 0]
}

fig, (ax2, ax1) = plt.subplots(nrows=2, ncols=1, figsize=(12, 10))
bar_width = 0.15
index = np.arange(len(cities))

event_colors = ['#66B3FF', '#FF7F50', '#FFCC99', '#99FF99', '#FF9999']

city_colors = ['#FFCC99', '#FF9999', '#FF7F50', '#66B3FF', '#99FF99']

index_months = np.arange(len(months))
for i, (city, color) in enumerate(zip(cities, city_colors)):
    ax2.bar(index_months + i * bar_width, monthly_sightings[city], bar_width, color=color)

ax2.set_xticks(index_months + 2 * bar_width)
ax2.set_xticklabels([])
ax2.set_yticklabels([])
ax2.set_ylim(0, 10)
ax2.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

for i, event in enumerate(celestial_events):
    counts = [data[i] for data in observation_data]
    ax1.bar(index + i * bar_width, counts, bar_width, color=event_colors[i])

ax1.set_xticks(index + 2 * bar_width)
ax1.set_xticklabels([])
ax1.set_yticklabels([])
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)

plt.tight_layout()
plt.show()