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
    ax2.bar(index_months + i * bar_width, monthly_sightings[city], bar_width, label=city, color=color)

ax2.set_xlabel('Month', fontsize=12)
ax2.set_ylabel('Total Sightings', fontsize=12)
ax2.set_title('Monthly Meteor Shower Sightings in 2023', fontsize=14, fontweight='bold', pad=10)
ax2.set_xticks(index_months + 2 * bar_width)
ax2.set_xticklabels(months, fontsize=11)
ax2.set_ylim(0, 10)
ax2.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax2.legend(title='Cities', fontsize=10, title_fontsize='12', loc='upper right')

for i, event in enumerate(celestial_events):
    counts = [data[i] for data in observation_data]
    bars = ax1.bar(index + i * bar_width, counts, bar_width, label=event, color=event_colors[i])

    for bar in bars:
        height = bar.get_height()
        ax1.annotate(f'{height}', 
                     xy=(bar.get_x() + bar.get_width() / 2, height),
                     xytext=(0, 3),
                     textcoords="offset points",
                     ha='center', va='bottom', fontsize=8, fontweight='bold')

ax1.set_xlabel('Cities', fontsize=12)
ax1.set_ylabel('Number of Sightings', fontsize=12)
ax1.set_title('Celestial Event Sightings in Various Cities (2023)', fontsize=14, fontweight='bold', pad=10)
ax1.set_xticks(index + 2 * bar_width)
ax1.set_xticklabels(cities, fontsize=11)
ax1.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax1.legend(title='Celestial Events', fontsize=10, title_fontsize='12', loc='upper right')

plt.tight_layout()
plt.show()