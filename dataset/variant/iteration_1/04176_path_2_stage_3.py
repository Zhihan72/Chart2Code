import matplotlib.pyplot as plt
import numpy as np

# Values for the years and cities
years = np.arange(2015, 2023)
cities = ['New York', 'Los Angeles']

# Data for the adoption rates of smart home technologies
voice_assistants = np.array([
    [40, 42, 45, 48, 52, 55, 58, 60],  # New York
    [35, 37, 40, 42, 45, 48, 50, 53]   # Los Angeles
])

smart_lighting = np.array([
    [25, 28, 31, 34, 38, 40, 43, 45],  # New York
    [22, 25, 28, 30, 33, 35, 37, 40]   # Los Angeles
])

smart_thermostats = np.array([
    [15, 18, 20, 23, 26, 28, 30, 33],  # New York
    [12, 15, 17, 20, 22, 25, 27, 30]   # Los Angeles
])

# Set up the figure and axes
fig, axs = plt.subplots(3, 1, figsize=(12, 18), sharey=True)

# Define the bar height
bar_height = 0.35
position = np.arange(len(years))

# Colors for cities
colors = ['#ff9999','#66b3ff']

# Titles for subplots
titles = ['Smart Thermostats Adoption Rate', 'Smart Lighting Adoption Rate', 'Voice Assistants Adoption Rate']

# Plotting data
for i, data in enumerate([smart_thermostats, smart_lighting, voice_assistants]):
    city1 = axs[i].barh(position - bar_height/2, data[0], bar_height, label=cities[0], color=colors[0])
    city2 = axs[i].barh(position + bar_height/2, data[1], bar_height, label=cities[1], color=colors[1])
    
    # Adding data labels
    for bar in city1 + city2:
        xval = bar.get_width()
        axs[i].text(xval + 1, bar.get_y() + bar.get_height()/2.0, f"{xval}%", va='center', fontsize=9)

    axs[i].set_title(titles[i], fontsize=14, fontweight='bold')
    axs[i].set_xlabel('Adoption Rate (%)', fontsize=12)
    axs[i].legend(title='City', fontsize=10, loc='upper right')

# Set the y-axis on the last subplot
axs[-1].set_yticks(position)
axs[-1].set_yticklabels(years, rotation=45)
axs[-1].set_ylabel('Year', fontsize=12)

# Enhance layout and visual clarity
plt.tight_layout()

# Set the main title for the entire figure
fig.suptitle('Annual Growth in Adoption of Smart Home Technologies (2015-2022)\nA Comparative Analysis Between New York and Los Angeles',
             fontsize=16, fontweight='bold')
fig.subplots_adjust(top=0.92)

# Show the plot
plt.show()