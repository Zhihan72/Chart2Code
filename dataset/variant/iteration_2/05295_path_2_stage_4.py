import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

mammals = np.array([230, 240, 250, 260, 240, 230, 220, 210, 215, 225, 235])
birds = np.array([300, 325, 350, 375, 400, 420, 410, 430, 440, 460, 480])
reptiles = np.array([80, 85, 88, 92, 95, 90, 88, 92, 94, 96, 100])
# amphibians = np.array([150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200])
insects = np.array([500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700])

data = np.array([mammals, birds, reptiles, insects])
data_stack = np.cumsum(data, axis=0)

fig, ax = plt.subplots(figsize=(14, 8))

ax.fill_between(years, 0, data_stack[0], linewidth=2, linestyle='-', color='gold', alpha=0.8)  # mammals
ax.fill_between(years, data_stack[0], data_stack[1], linewidth=2, linestyle=':', color='lightgreen', alpha=0.7)  # birds
ax.fill_between(years, data_stack[1], data_stack[2], linewidth=2, linestyle='--', color='orchid', alpha=0.6)  # reptiles
ax.fill_between(years, data_stack[2], data_stack[3], linewidth=2, linestyle='-', color='skyblue', alpha=0.4)  # insects

ax.set_xticks(years)

ax.grid(True, linestyle='-', linewidth=0.8, alpha=0.3)

plt.tight_layout()
plt.show()