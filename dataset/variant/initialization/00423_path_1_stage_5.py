import matplotlib.pyplot as plt
import numpy as np

# Data representing daily energy consumption (in terajoules) over a month for each sector
residential = sorted([22, 24, 19, 30, 25, 21, 23, 22, 24, 23, 21, 26, 22, 27, 24, 24, 29, 21, 28, 32, 25, 23, 21, 22, 30, 23, 28, 27, 24, 22], reverse=True)
agricultural = sorted([33, 32, 31, 34, 35, 38, 37, 34, 36, 33, 35, 32, 33, 38, 31, 39, 40, 34, 36, 37, 38, 32, 33, 36, 31, 35, 32, 34, 33, 32], reverse=True)
research = sorted([22, 19, 20, 21, 18, 17, 18, 19, 25, 20, 22, 24, 23, 26, 21, 21, 21, 22, 20, 19, 25, 24, 19, 22, 26, 20, 21, 18, 20, 19], reverse=True)
industrial = sorted([53, 55, 56, 52, 53, 52, 60, 58, 57, 56, 54, 58, 53, 50, 51, 51, 55, 60, 54, 57, 58, 60, 59, 58, 59, 55, 50, 52, 55, 56], reverse=True)
commercial = sorted([31, 29, 30, 34, 28, 32, 33, 30, 30, 29, 31, 28, 27, 35, 31, 32, 31, 34, 36, 30, 33, 32, 29, 30, 29, 32, 34, 28, 31, 30], reverse=True)

# Sector labels and data
sectors = ["Residential", "Agricultural", "Research", "Industrial", "Commercial"]
data = [residential, agricultural, research, industrial, commercial]
colors = ["blue", "green", "red", "purple", "orange"]  # Colors assigned manually to be shuffled

fig, ax = plt.subplots(figsize=(10, 8))

# Bar chart with shuffled color assignment
for i, sector_data in enumerate(data):
    ax.barh(np.arange(len(sector_data)) + i * (len(sector_data) + 1), sector_data, color=colors[i])

ax.set_yticks([(len(residential) / 2) + (i * (len(residential) + 1)) for i in range(len(sectors))])
ax.set_yticklabels(sectors)

plt.show()