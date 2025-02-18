import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
wheat_harvest = np.array([500, 520, 530, 545, 560, 570, 590, 610, 625, 640, 660])
corn_harvest = np.array([450, 460, 480, 500, 515, 530, 550, 570, 590, 610, 630])
rice_harvest = np.array([380, 400, 420, 435, 455, 475, 490, 505, 520, 540, 560])
soybean_harvest = np.array([150, 160, 170, 175, 185, 195, 205, 220, 230, 240, 255])

fig, ax = plt.subplots(figsize=(14, 8))
ax.fill_between(years, 0, wheat_harvest, color='steelblue', alpha=0.7)
ax.fill_between(years, wheat_harvest, wheat_harvest + corn_harvest, color='mediumseagreen', alpha=0.7)
ax.fill_between(years, wheat_harvest + corn_harvest, wheat_harvest + corn_harvest + rice_harvest, color='mediumpurple', alpha=0.7)
ax.fill_between(years, wheat_harvest + corn_harvest + rice_harvest, 
                wheat_harvest + corn_harvest + rice_harvest + soybean_harvest, 
                color='tomato', alpha=0.7)

plt.xticks(years, rotation=45, ha="right")
ax.set_xticklabels([])
ax.set_yticklabels([])
plt.tight_layout()
plt.show()