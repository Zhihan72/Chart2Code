import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
wheat_harvest = np.array([500, 520, 530, 545, 560, 570, 590, 610, 625, 640, 660])
corn_harvest = np.array([450, 460, 480, 500, 515, 530, 550, 570, 590, 610, 630])
rice_harvest = np.array([380, 400, 420, 435, 455, 475, 490, 505, 520, 540, 560])
soybean_harvest = np.array([150, 160, 170, 175, 185, 195, 205, 220, 230, 240, 255])

fig, ax = plt.subplots(figsize=(14, 8))
ax.fill_between(years, 0, wheat_harvest, color='goldenrod', alpha=0.7)
ax.fill_between(years, wheat_harvest, wheat_harvest + corn_harvest, color='coral', alpha=0.7)
ax.fill_between(years, wheat_harvest + corn_harvest, wheat_harvest + corn_harvest + rice_harvest, color='khaki', alpha=0.7)
ax.fill_between(years, wheat_harvest + corn_harvest + rice_harvest, 
                wheat_harvest + corn_harvest + rice_harvest + soybean_harvest, 
                color='cadetblue', alpha=0.7)

ax.set_title("Annual Harvest Quantities of Selected Crops in AgroLand (2010-2020)", fontsize=16, fontweight='bold')
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Harvest Quantity (thousand tonnes)", fontsize=12)

plt.xticks(years, rotation=45, ha="right")
plt.tight_layout()
plt.show()