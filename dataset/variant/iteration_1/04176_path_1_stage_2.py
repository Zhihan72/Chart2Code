import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2023)
cities = ['New York', 'Los Angeles', 'Chicago']

voice_assistants = np.array([
    [40, 42, 45, 48, 52, 55, 58, 60],
    [35, 37, 40, 42, 45, 48, 50, 53],
    [30, 32, 35, 37, 40, 42, 44, 47]
])

smart_lighting = np.array([
    [25, 28, 31, 34, 38, 40, 43, 45],
    [22, 25, 28, 30, 33, 35, 37, 40],
    [18, 20, 23, 25, 28, 30, 32, 35]
])

smart_thermostats = np.array([
    [15, 18, 20, 23, 26, 28, 30, 33],
    [12, 15, 17, 20, 22, 25, 27, 30],
    [10, 12, 14, 17, 19, 21, 23, 26]
])

fig, axs = plt.subplots(3, 1, figsize=(12, 18), sharey=True)

bar_width = 0.25
position = np.arange(len(years))
new_colors = ['#ffcc99', '#99ccff', '#ccff99']  # Changed color set
titles = ['Voice Assistants Adoption Rate', 'Smart Lighting Adoption Rate', 'Smart Thermostats Adoption Rate']

for i, data in enumerate([voice_assistants, smart_lighting, smart_thermostats]):
    city1 = axs[i].barh(position - bar_width, data[0], bar_width, label=cities[0], color=new_colors[0])
    city2 = axs[i].barh(position, data[1], bar_width, label=cities[1], color=new_colors[1])
    city3 = axs[i].barh(position + bar_width, data[2], bar_width, label=cities[2], color=new_colors[2])
    
    for bar in city1 + city2 + city3:
        xval = bar.get_width()
        axs[i].text(xval + 0.5, bar.get_y() + bar.get_height()/2.0, f"{xval}%", va='center', fontsize=9)

    axs[i].set_title(titles[i], fontsize=14, fontweight='bold')
    axs[i].set_xlabel('Adoption Rate (%)', fontsize=12)
    axs[i].legend(title='City', fontsize=10, loc='lower right')

axs[-1].set_yticks(position)
axs[-1].set_yticklabels(years)
axs[-1].set_ylabel('Year', fontsize=12)

plt.tight_layout()
fig.suptitle('Annual Growth in Adoption of Smart Home Technologies (2015-2022)\nA Comparative Analysis Between New York, Los Angeles, and Chicago',
             fontsize=16, fontweight='bold')
fig.subplots_adjust(top=0.92)

plt.show()