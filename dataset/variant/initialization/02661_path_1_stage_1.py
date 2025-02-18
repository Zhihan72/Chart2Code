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
              colors=['#FFD700', '#87CEEB', '#32CD32', '#8B4513'], alpha=0.8)

plt.title("Eco Power Progress (2010-2020)\nTowards Greener Pastures", fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Timeline', fontsize=12)
plt.ylabel('Share of Eco Energy (%)', fontsize=12)

plt.legend(loc='upper left', title="Power Types", fontsize=10, title_fontsize=11)

plt.grid(True, linestyle='--', alpha=0.5)
plt.xticks(years, rotation=45)
plt.tight_layout()

plt.show()