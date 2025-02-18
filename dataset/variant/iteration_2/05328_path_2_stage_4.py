import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2005, 2021)
co2_emissions = [335, 325, 315, 310, 305, 295, 280, 270, 260, 250, 240, 235, 229, 225, 220, 210]

fig, ax1 = plt.subplots(figsize=(14, 6))
ax1.plot(years, co2_emissions, color='red', linewidth=2, marker='o', linestyle='-', markersize=6)
ax1.set_xlabel('Yr', fontsize=12)
ax1.set_ylabel('CO2 (Mil Tons)', fontsize=12)

plt.xticks(years, rotation=45)
plt.show()