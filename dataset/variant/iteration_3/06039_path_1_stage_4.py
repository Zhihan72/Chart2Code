import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

wheat_harvest = np.array([500, 520, 530, 545, 560, 570, 590, 610, 625, 640, 660])
corn_harvest = np.array([450, 460, 480, 500, 515, 530, 550, 570, 590, 610, 630])
rice_harvest = np.array([380, 400, 420, 435, 455, 475, 490, 505, 520, 540, 560])
barley_harvest = np.array([200, 210, 220, 225, 230, 240, 250, 260, 270, 280, 290])

fig, ax = plt.subplots(figsize=(14, 8))

color = 'steelblue'

ax.fill_between(years, 0, wheat_harvest, color=color, alpha=0.7)
ax.fill_between(years, wheat_harvest, wheat_harvest + corn_harvest, color=color, alpha=0.7)
ax.fill_between(years, wheat_harvest + corn_harvest, wheat_harvest + corn_harvest + rice_harvest, color=color, alpha=0.7)
ax.fill_between(years, wheat_harvest + corn_harvest + rice_harvest, 
                wheat_harvest + corn_harvest + rice_harvest + barley_harvest, 
                color=color, alpha=0.7)

plt.tight_layout()

plt.show()