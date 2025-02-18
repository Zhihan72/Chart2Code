import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2012, 2023)

na_consumption = [500, 530, 560, 590, 620, 650, 680, 720, 750, 780, 820]
eu_consumption = [450, 470, 490, 520, 550, 580, 600, 630, 670, 700, 730]
asia_consumption = [700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]
africa_consumption = [200, 210, 220, 230, 250, 270, 290, 310, 330, 350, 370]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, na_consumption, marker='o', linestyle='-', color='b', linewidth=2)
ax.plot(years, eu_consumption, marker='^', linestyle='-', color='g', linewidth=2)
ax.plot(years, asia_consumption, marker='s', linestyle='-', color='r', linewidth=2)
ax.plot(years, africa_consumption, marker='d', linestyle='-', color='m', linewidth=2)

ax.set_title("Renewable Energy Trend (2012-2022)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Consumption (TWh)", fontsize=12)

plt.tight_layout()
plt.show()