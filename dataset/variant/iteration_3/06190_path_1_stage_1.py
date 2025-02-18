import matplotlib.pyplot as plt
import numpy as np

regions = ["NA", "EU", "Asia", "Africa"]
years = np.arange(2012, 2023)

na_consumption = [500, 530, 560, 590, 620, 650, 680, 720, 750, 780, 820]
eu_consumption = [450, 470, 490, 520, 550, 580, 600, 630, 670, 700, 730]
asia_consumption = [700, 750, 800, 850, 900, 950, 1000, 1050, 1100, 1150, 1200]
africa_consumption = [200, 210, 220, 230, 250, 270, 290, 310, 330, 350, 370]

fig, ax = plt.subplots(figsize=(14, 8))

ax.plot(years, na_consumption, label='NA', marker='o', linestyle='-', color='b', linewidth=2)
ax.plot(years, eu_consumption, label='EU', marker='^', linestyle='-', color='g', linewidth=2)
ax.plot(years, asia_consumption, label='Asia', marker='s', linestyle='-', color='r', linewidth=2)
ax.plot(years, africa_consumption, label='Africa', marker='d', linestyle='-', color='m', linewidth=2)

ax.set_title("Renewable Energy Trend (2012-2022)", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=12)
ax.set_ylabel("Consumption (TWh)", fontsize=12)

ax.legend(loc='upper left', fontsize=10, title="Region", frameon=True)
ax.grid(True, which='major', linestyle='--', linewidth=0.5, alpha=0.7)

ax.annotate('Increase',
            xy=(2018, 950), 
            xytext=(2016, 1100),
            arrowprops=dict(facecolor='black', arrowstyle='->', lw=1.5),
            fontsize=10, fontweight='bold', color='darkred')

ax.axvline(x=2022, color='gray', linestyle='--', linewidth=1.5, alpha=0.7)
ax.text(2022.1, 400, '2022 End', rotation=90, verticalalignment='center', fontsize=10, color='gray')

plt.tight_layout()
plt.show()