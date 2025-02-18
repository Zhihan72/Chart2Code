import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2023)
cities = ['New York', 'Los Angeles']

voice_assistants = np.array([
    [40, 42, 45, 48, 52, 55, 58, 60],
    [35, 37, 40, 42, 45, 48, 50, 53]
])

smart_lighting = np.array([
    [25, 28, 31, 34, 38, 40, 43, 45],
    [22, 25, 28, 30, 33, 35, 37, 40]
])

smart_thermostats = np.array([
    [15, 18, 20, 23, 26, 28, 30, 33],
    [12, 15, 17, 20, 22, 25, 27, 30]
])

fig, axs = plt.subplots(3, 1, figsize=(12, 18), sharey=True)

bar_height = 0.35
position = np.arange(len(years))

# New set of colors for the cities
colors = ['#4daf4a', '#ff7f00']

titles = ['Smart Thermostats Adoption Rate', 'Smart Lighting Adoption Rate', 'Voice Assistants Adoption Rate']

for i, data in enumerate([smart_thermostats, smart_lighting, voice_assistants]):
    city1 = axs[i].barh(position - bar_height/2, data[0], bar_height, label=cities[0], color=colors[0])
    city2 = axs[i].barh(position + bar_height/2, data[1], bar_height, label=cities[1], color=colors[1])
    
    for bar in city1 + city2:
        xval = bar.get_width()
        axs[i].text(xval + 1, bar.get_y() + bar.get_height()/2.0, f"{xval}%", va='center', fontsize=9)

    axs[i].set_title(titles[i], fontsize=14, fontweight='bold')
    axs[i].set_xlabel('Adoption Rate (%)', fontsize=12)
    axs[i].legend(title='City', fontsize=10, loc='upper right')

axs[-1].set_yticks(position)
axs[-1].set_yticklabels(years, rotation=45)
axs[-1].set_ylabel('Year', fontsize=12)

plt.tight_layout()

fig.suptitle('Annual Growth in Adoption of Smart Home Technologies (2015-2022)\nA Comparative Analysis Between New York and Los Angeles',
             fontsize=16, fontweight='bold')
fig.subplots_adjust(top=0.92)

plt.show()