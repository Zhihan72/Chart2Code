import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

north_america_renewable = [50, 70, 110, 150, 200, 260, 330, 410, 500, 600, 710]
europe_renewable = [60, 80, 100, 140, 200, 280, 360, 450, 550, 670, 800]
asia_renewable = [40, 60, 90, 130, 180, 240, 310, 390, 480, 580, 690]
south_america_renewable = [20, 30, 50, 75, 110, 150, 200, 260, 330, 410, 500]

data = np.array([
    north_america_renewable,
    europe_renewable,
    asia_renewable,
    south_america_renewable
])

fig, ax = plt.subplots(figsize=(12, 8))

ax.stackplot(
    years, data, labels=[
        'North America', 'Europe', 'Asia', 'South America'
    ],
    colors=['#d62728', '#9467bd', '#1f77b4', '#2ca02c'], alpha=0.80
)

ax.set_title(
    "Renewable Energy Growth by Region (2010-2020)",
    fontsize=20, fontweight='bold')
ax.set_xlabel("Year", fontsize=15)
ax.set_ylabel("Energy Production (TWh)", fontsize=15)
ax.legend(loc='upper right', title="Regions", fontsize=11)

ax.grid(True, linestyle='-.', alpha=0.5)

ax.spines['top'].set_visible(False)
ax.spines['right'].set_linewidth(2)

ax.annotate('N. America surpasses 500 TWh', xy=(2019, 500), xytext=(2015, 350),
            arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=11, fontweight='bold')
ax.annotate('Rapid growth in Asia', xy=(2016, 240), xytext=(2011, 400),
            arrowprops=dict(facecolor='red', arrowstyle='-|>'), fontsize=11, fontweight='bold')

fig.tight_layout()

plt.show()