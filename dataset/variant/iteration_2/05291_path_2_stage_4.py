import matplotlib.pyplot as plt
import numpy as np

years = np.array([2010, 2011, 2012, 2013, 2014, 2016, 2017, 2018, 2019])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
visitors = [
    [105, 120, 150, 200, 300, 320, 450, 430, 280, 200, 150, 110],  # 2010
    [108, 125, 155, 205, 305, 330, 460, 440, 290, 210, 160, 115],  # 2011
    [110, 130, 160, 210, 310, 340, 470, 450, 300, 220, 170, 120],  # 2012
    [115, 135, 165, 215, 315, 350, 480, 460, 310, 230, 175, 125],  # 2013
    [120, 140, 170, 220, 320, 360, 490, 470, 320, 240, 180, 130],  # 2014
    [130, 150, 180, 230, 330, 380, 510, 490, 340, 260, 190, 140],  # 2016
    [135, 155, 185, 235, 335, 390, 520, 500, 350, 270, 195, 145],  # 2017
    [140, 160, 190, 240, 340, 400, 530, 510, 360, 280, 200, 150],  # 2018
    [145, 165, 195, 245, 345, 410, 540, 520, 370, 290, 205, 155],  # 2019
]

# Manually shuffled styles
shuffled_colors = ['purple', 'b', 'y', 'c', 'm', 'g', 'red', 'orange', 'k']
shuffled_markers = ['s', 'D', '*', 'v', '^', '<', '>', 'h', 'p']
shuffled_linestyles = ['--', '-.', ':', '-', '--', '-.', ':', '-', '--']

fig, ax = plt.subplots(figsize=(14, 8))

for i, year in enumerate(years):
    ax.plot(months, visitors[i], marker=shuffled_markers[i], color=shuffled_colors[i], linestyle=shuffled_linestyles[i], label=str(year))

ax.grid(True, linestyle='-.', alpha=0.5)

# Set border color and thickness
for spine in ax.spines.values():
    spine.set_edgecolor('dimgray')
    spine.set_linewidth(2)

ax.legend(title='Year', loc='upper left', fontsize='small')
plt.tight_layout()
plt.show()