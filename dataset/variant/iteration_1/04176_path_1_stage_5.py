import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2015, 2023)

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

fig, axs = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

bar_width = 0.25
position = np.arange(len(years))
new_colors = ['#ffcc99', '#99ccff', '#ccff99']

for i, data in enumerate([voice_assistants, smart_lighting, smart_thermostats]):
    city1 = axs[i].barh(position - bar_width, data[0], bar_width, color=new_colors[0])
    city2 = axs[i].barh(position, data[1], bar_width, color=new_colors[1])
    city3 = axs[i].barh(position + bar_width, data[2], bar_width, color=new_colors[2])
    
    for bar in city1 + city2 + city3:
        xval = bar.get_width()
        axs[i].text(xval + 0.5, bar.get_y() + bar.get_height()/2.0, f"{xval}%", va='center', fontsize=9)

    axs[i].set_frame_on(False)  # Removing border

axs[0].set_yticks(position)
axs[0].set_yticklabels([])  # Remove year labels on y-axis

plt.tight_layout()

plt.show()