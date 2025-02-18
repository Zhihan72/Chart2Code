import matplotlib.pyplot as plt
import numpy as np

# Data for different sectors
residential = [24, 30, 23, 22, 27, 32, 22, 23, 19, 24, 25, 21, 21, 23, 24, 24, 29, 25, 30, 18, 28, 23, 21, 22, 23, 24, 28, 27, 22, 24]
agricultural = [34, 38, 39, 34, 31, 38, 37, 34, 35, 32, 36, 38, 33, 31, 33, 34, 32, 40, 36, 37, 35, 34, 33, 32, 31, 35, 36, 34, 33, 32]
research = [20, 25, 20, 21, 22, 17, 18, 19, 18, 24, 23, 26, 20, 21, 18, 19, 22, 21, 20, 19, 25, 26, 21, 22, 20, 19, 28, 22, 20, 19]
industrial = [51, 58, 52, 52, 51, 58, 60, 59, 57, 56, 53, 52, 53, 55, 50, 51, 55, 58, 60, 57, 56, 58, 59, 60, 55, 53, 52, 54, 55, 56]
commercial = [29, 34, 32, 31, 29, 32, 31, 30, 33, 34, 28, 29, 27, 30, 31, 32, 36, 34, 33, 35, 31, 30, 29, 32, 34, 30, 29, 28, 31, 30]

# Calculate total consumption by sector
total_consumption = [sum(residential), sum(agricultural), sum(research), sum(industrial), sum(commercial)]

# Sector labels changed
sectors = ["Household", "Farming", "Studies", "Factories", "Business"]

fig, axs = plt.subplots(1, 2, figsize=(15, 8), gridspec_kw={'width_ratios': [2, 1]})

# Boxplot with altered labels
axs[0].boxplot([residential, agricultural, research, industrial, commercial], vert=False, patch_artist=True, notch=True,
               boxprops=dict(facecolor='lightblue'),
               whiskerprops=dict(),
               capprops=dict(),
               flierprops=dict(marker='o', color='red', markersize=8, alpha=0.6),
               medianprops=dict(color='orange', linewidth=2))

axs[0].set_title("Distribution of Power Usage by Group", fontsize=14)  # Changed title
axs[0].set_yticks(np.arange(1, len(sectors) + 1))
axs[0].set_yticklabels(sectors, fontsize=12)

# Bar chart with altered labels
axs[1].barh(sectors, total_consumption, color=['#FFDDC1', '#FFABAB', '#FFC3A0', '#FF677D', '#D4A5A5'])
axs[1].set_title("Total Power Usage", fontsize=14)  # Changed title

axs[1].set_xlim(0, max(total_consumption) * 1.1)

plt.tight_layout()
plt.show()