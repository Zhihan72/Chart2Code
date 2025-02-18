import matplotlib.pyplot as plt
import numpy as np

# Data representing daily energy consumption (in terajoules) over a month for each sector
residential = [22, 24, 19, 30, 25, 21, 23, 22, 24, 23, 21, 26, 22, 27, 24, 24, 29, 21, 28, 32, 25, 23, 21, 22, 30, 23, 28, 27, 24, 22]
agricultural = [33, 32, 31, 34, 35, 38, 37, 34, 36, 33, 35, 32, 33, 38, 31, 39, 40, 34, 36, 37, 38, 32, 33, 36, 31, 35, 32, 34, 33, 32]
research = [22, 19, 20, 21, 18, 17, 18, 19, 25, 20, 22, 24, 23, 26, 21, 21, 21, 22, 20, 19, 25, 24, 19, 22, 26, 20, 21, 18, 20, 19]
industrial = [53, 55, 56, 52, 53, 52, 60, 58, 57, 56, 54, 58, 53, 50, 51, 51, 55, 60, 54, 57, 58, 60, 59, 58, 59, 55, 50, 52, 55, 56]
commercial = [31, 29, 30, 34, 28, 32, 33, 30, 30, 29, 31, 28, 27, 35, 31, 32, 31, 34, 36, 30, 33, 32, 29, 30, 29, 32, 34, 28, 31, 30]

# Sector labels
sectors = ["Residential", "Agricultural", "Research", "Industrial", "Commercial"]

# Create a single subplot for the Box Plot
fig, ax = plt.subplots(figsize=(10, 8))

# Box Plot
box = ax.boxplot([residential, agricultural, research, industrial, commercial], vert=False, patch_artist=True, notch=False)

ax.set_yticks(np.arange(1, len(sectors) + 1))
ax.set_yticklabels(sectors)

# Display the plot
plt.show()