import matplotlib.pyplot as plt
import numpy as np

# Cities observed
cities = ['San Francisco', 'New York', 'Chicago', 'Houston', 'Phoenix']

# Types of celestial events
celestial_events = ['Meteor Shower', 'Lunar Eclipse', 'Solar Eclipse', 'Comet Sighting', 'Aurora']

# Data: counts of each celestial event observed in each city
observation_data = [
    [12, 4, 1, 6, 2],    # San Francisco
    [8, 6, 2, 7, 1],     # New York
    [10, 3, 3, 5, 0],    # Chicago
    [7, 5, 2, 9, 3],     # Houston
    [9, 4, 2, 10, 1]     # Phoenix
]

# Months
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# Historical trend data: monthly sightings of meteor showers across cities in 2023
monthly_sightings = {
    'San Francisco': [1, 2, 1, 1, 1, 2, 3, 0, 0, 1, 0, 0],
    'New York': [1, 1, 1, 2, 1, 1, 2, 0, 1, 0, 1, 0],
    'Chicago': [0, 1, 1, 2, 1, 2, 2, 1, 1, 1, 0, 0],
    'Houston': [1, 1, 2, 2, 1, 0, 2, 1, 2, 1, 0, 0],
    'Phoenix': [0, 1, 1, 2, 2, 0, 2, 2, 1, 1, 0, 0]
}

# Initialize the plot with two subplots in a 1x2 grid
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

# Plot 1: Grouped bar chart
bar_width = 0.15
index = np.arange(len(cities))

for i, event in enumerate(celestial_events):
    counts = [data[i] for data in observation_data]
    bars = ax1.bar(index + i * bar_width, counts, bar_width, label=event)

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

# Plot 2: Stacked bar chart showing historical trends of meteor shower sightings
bottom_values = np.zeros(len(months))
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99', '#FF7F50']

for i, (city, color) in enumerate(zip(cities, colors)):
    ax2.bar(months, monthly_sightings[city], bottom=bottom_values, label=city, color=color)
    bottom_values += monthly_sightings[city]

ax2.set_xlabel('Month', fontsize=12)
ax2.set_ylabel('Total Sightings', fontsize=12)
ax2.set_title('Monthly Meteor Shower Sightings in 2023', fontsize=14, fontweight='bold', pad=10)
ax2.set_ylim(0, 10)
ax2.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
ax2.legend(title='Cities', fontsize=10, title_fontsize='12', loc='upper right')

# Adjust layout
plt.tight_layout()

# Show plot
plt.show()