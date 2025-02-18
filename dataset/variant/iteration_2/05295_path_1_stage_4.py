import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

mammals = np.array([235, 245, 255, 255, 245, 225, 230, 220, 215, 230, 240])
birds = np.array([310, 330, 340, 380, 390, 425, 415, 420, 435, 455, 470])
reptiles = np.array([78, 86, 89, 91, 96, 91, 87, 93, 95, 95, 101])
amphibians = np.array([152, 158, 162, 168, 169, 172, 183, 182, 188, 196, 198])
insects = np.array([505, 525, 535, 555, 575, 610, 615, 650, 655, 675, 695])

data = np.array([mammals, birds, reptiles, amphibians, insects])
data_stack = np.cumsum(data, axis=0)

fig, ax = plt.subplots(figsize=(14, 8))

ax.fill_between(years, 0, data_stack[0], label='Mammals', color='lightblue', alpha=0.9)
ax.fill_between(years, data_stack[0], data_stack[1], label='Birds', color='peachpuff', alpha=0.6, hatch='/')
ax.fill_between(years, data_stack[1], data_stack[2], label='Reptiles', color='mediumpurple', alpha=0.5, hatch='\\')
ax.fill_between(years, data_stack[2], data_stack[3], label='Amphibians', color='salmon', alpha=0.6, hatch='-')
ax.fill_between(years, data_stack[3], data_stack[4], label='Insects', color='lightgreen', alpha=0.7, hatch='|')

ax.set_title("Wildlife Observation Trends (2010-2020)", fontsize=18, weight='heavy', pad=15)
ax.set_xlabel("Year", fontsize=13)
ax.set_ylabel("Count", fontsize=13)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=30, fontsize=12)

ax.grid(True, linestyle='dashdot', linewidth=0.8, alpha=0.5)

ax.legend(loc='lower right', fontsize=9, shadow=True, facecolor='whitesmoke')

plt.tight_layout()
plt.show()