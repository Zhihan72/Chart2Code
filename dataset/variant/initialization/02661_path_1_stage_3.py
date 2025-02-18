import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

solar = [5, 7, 10, 15, 20, 25, 30, 35, 38, 42, 45]
wind = [30, 28, 27, 25, 22, 20, 18, 17, 17, 16, 15]
hydroelectric = [50, 48, 45, 42, 40, 38, 35, 33, 32, 31, 30]
biomass = [15, 17, 18, 18, 18, 17, 17, 15, 13, 11, 10]

data = np.vstack([solar, wind, hydroelectric, biomass])

plt.figure(figsize=(12, 8))
plt.stackplot(years, data, 
              labels=['Radiance', 'Gale', 'Water Power', 'Biofuel'], 
              colors=['#33A1FF', '#FF5733', '#FF33A1', '#33FF57'], alpha=0.7)

plt.title("Eco Power Progress (2010-2020)\nEmbracing Clean Energy", fontsize=16, fontweight='light', pad=15)
plt.xlabel('Timeline', fontsize=12, fontweight='light')
plt.ylabel('Share of Eco Energy (%)', fontsize=12, fontweight='light')

plt.legend(loc='upper right', title="Power Sources", fontsize=9, title_fontsize=10)

plt.grid(True, linestyle=':', linewidth=0.7, alpha=0.6)
plt.xticks(years, rotation=30)
plt.tight_layout()

plt.show()