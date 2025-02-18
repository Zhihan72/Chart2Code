import matplotlib.pyplot as plt
import numpy as np

# Values for the years and cities
years = np.arange(2015, 2023)
cities = ['New York', 'Los Angeles', 'Chicago']

# Data for the adoption rates (in percentage) of smart home technologies
voice_assistants = np.array([
    [40, 42, 45, 48, 52, 55, 58, 60],  # New York
    [35, 37, 40, 42, 45, 48, 50, 53],  # Los Angeles
    [30, 32, 35, 37, 40, 42, 44, 47]   # Chicago
])

smart_lighting = np.array([
    [25, 28, 31, 34, 38, 40, 43, 45],  # New York
    [22, 25, 28, 30, 33, 35, 37, 40],  # Los Angeles
    [18, 20, 23, 25, 28, 30, 32, 35]   # Chicago
])

smart_thermostats = np.array([
    [15, 18, 20, 23, 26, 28, 30, 33],  # New York
    [12, 15, 17, 20, 22, 25, 27, 30],  # Los Angeles
    [10, 12, 14, 17, 19, 21, 23, 26]   # Chicago
])

# Set up the figure and axes
fig, axs = plt.subplots(3, 1, figsize=(12, 18), sharex=True)

# Define the bar width
bar_width = 0.25
position = np.arange(len(years))

# Colors for cities
colors = ['#ff9999','#66b3ff','#99ff99']

# Titles for subplots
titles = ['Smart Thermostats Adoption Rate', 'Smart Lighting Adoption Rate', 'Voice Assistants Adoption Rate']

# Plotting data - swap the order of the data
for i, data in enumerate([smart_thermostats, smart_lighting, voice_assistants]):
    city1 = axs[i].bar(position - bar_width, data[0], bar_width, label=cities[0], color=colors[0])
    city2 = axs[i].bar(position, data[1], bar_width, label=cities[1], color=colors[1])
    city3 = axs[i].bar(position + bar_width, data[2], bar_width, label=cities[2], color=colors[2])
    
    # Adding data labels
    for bar in city1 + city2 + city3:
        yval = bar.get_height()
        axs[i].text(bar.get_x() + bar.get_width()/2.0, yval + 0.5, f"{yval}%", ha='center', va='bottom', fontsize=9)

    axs[i].set_title(titles[i], fontsize=14, fontweight='bold')
    axs[i].set_ylabel('Adoption Rate (%)', fontsize=12)
    axs[i].legend(title='City', fontsize=10, loc='upper left')

# Set the x-axis on the last subplot
axs[-1].set_xticks(position)
axs[-1].set_xticklabels(years, rotation=45)
axs[-1].set_xlabel('Year', fontsize=12)

# Enhance layout and visual clarity
plt.tight_layout()

# Set the main title for the entire figure
fig.suptitle('Annual Growth in Adoption of Smart Home Technologies (2015-2022)\nA Comparative Analysis Between New York, Los Angeles, and Chicago',
             fontsize=16, fontweight='bold')
fig.subplots_adjust(top=0.92)

# Show the plot
plt.show()