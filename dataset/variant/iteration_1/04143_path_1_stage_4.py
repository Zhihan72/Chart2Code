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

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

single_color = 'gray'

bar_width = 0.15
index = np.arange(len(cities))
for i, event in enumerate(celestial_events):
    counts = [data[i] for data in observation_data]
    bars = ax1.bar(index + i * bar_width, counts, bar_width, color=single_color)

ax1.set_xticks(index + 2 * bar_width)
ax1.yaxis.grid(True, linestyle='-', which='major', color='blue', alpha=0.3)

bottom_values = np.zeros(len(months))
for city in cities:
    ax2.bar(months, monthly_sightings[city], bottom=bottom_values, color=single_color)
    bottom_values += monthly_sightings[city]

ax2.set_ylim(0, 10)
ax2.yaxis.grid(True, linestyle=':', which='major', color='green', alpha=0.5)

plt.tight_layout()
plt.show()