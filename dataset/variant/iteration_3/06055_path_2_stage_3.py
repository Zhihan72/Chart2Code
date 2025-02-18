import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

wheat = np.array([60, 62, 65, 70, 75, 78, 80, 82, 85, 90, 95])
rice = np.array([40, 42, 43, 45, 47, 50, 53, 55, 58, 60, 62])
maize = np.array([30, 32, 34, 36, 39, 42, 45, 48, 52, 56, 60])
soy = np.array([20, 22, 23, 25, 27, 30, 32, 35, 37, 40, 45])

data = np.vstack([wheat, rice, maize, soy])

# Define a single color for all crops
consistent_color = ['#66c2a5']  # Greenish color

fig, ax = plt.subplots(figsize=(12, 8))
ax.stackplot(years, data, colors=consistent_color * len(data), alpha=0.8)

ax.set_title("A Decade of Harvest in Nutrivia:\nCrop Yield Trends from 2010-2020", fontsize=16, fontweight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Annual Yield (Million Metric Tons)", fontsize=14)

plt.xticks(years, rotation=45)
plt.tight_layout()

plt.show()