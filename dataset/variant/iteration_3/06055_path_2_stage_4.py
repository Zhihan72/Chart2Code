import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

wheat = np.array([60, 62, 65, 70, 75, 78, 80, 82, 85, 90, 95])
rice = np.array([40, 42, 43, 45, 47, 50, 53, 55, 58, 60, 62])
maize = np.array([30, 32, 34, 36, 39, 42, 45, 48, 52, 56, 60])
soy = np.array([20, 22, 23, 25, 27, 30, 32, 35, 37, 40, 45])

bar_width = 0.2
index = np.arange(len(years))

fig, ax = plt.subplots(figsize=(12, 8))

ax.bar(index - bar_width*1.5, wheat, bar_width, label='Wheat', color='#66c2a5')  # Green-wheat
ax.bar(index - bar_width*0.5, rice, bar_width, label='Rice', color='#fc8d62')   # Orange-rice
ax.bar(index + bar_width*0.5, maize, bar_width, label='Maize', color='#8da0cb')  # Blue-maize
ax.bar(index + bar_width*1.5, soy, bar_width, label='Soy', color='#e78ac3')     # Pink-soy

ax.set_xticks(index)
ax.set_xticklabels(years, rotation=45)

ax.set_title("A Decade of Harvest in Nutrivia:\nCrop Yield Trends from 2010-2020", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Annual Yield (Million Metric Tons)", fontsize=14)
ax.legend()

plt.tight_layout()
plt.show()