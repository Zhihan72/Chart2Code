import matplotlib.pyplot as plt
import numpy as np

cities = ['Oceanview', 'Mountain Peak', 'Sunnyvale', 'Lake Town', 'Desert Hues']
rainfall_data = [
    [85, 78, 92, 110, 125, 140, 155, 145, 130, 115, 100, 90],  # Oceanview
    [95, 88, 102, 120, 135, 150, 165, 155, 140, 125, 110, 100],  # Mountain Peak
    [45, 40, 52, 60, 75, 80, 85, 75, 65, 55, 50, 45],  # Sunnyvale
    [75, 68, 82, 90, 105, 120, 135, 125, 110, 95, 80, 70],  # Lake Town
    [15, 10, 22, 30, 35, 40, 45, 35, 25, 20, 15, 10],  # Desert Hues
]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
rainfall_data = np.array(rainfall_data)

fig, axs = plt.subplots(nrows=2, ncols=1, figsize=(14, 12))

bar_width = 0.15
y = np.arange(len(months))
color = '#1f77b4'

# Line plot
marker = 'o'
for i, city in enumerate(cities):
    axs[0].plot(months, rainfall_data[i], marker=marker, color=color)

axs[0].legend(loc='best')
axs[0].xaxis.set_tick_params(labelbottom=False)
axs[0].yaxis.set_tick_params(labelleft=False)

# Horizontal Bar plot
for i, city in enumerate(cities):
    axs[1].barh(y + i * bar_width, rainfall_data[i], bar_width, color=color)

axs[1].legend(loc='best')
axs[1].set_yticks(y + bar_width * (len(cities) / 2 - 0.5))
axs[1].set_yticklabels([])
axs[1].xaxis.set_tick_params(labelbottom=False)

plt.tight_layout()
plt.show()