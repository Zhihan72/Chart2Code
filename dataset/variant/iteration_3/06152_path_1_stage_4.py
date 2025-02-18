import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
solartech_production = [60, 15, 50, 65, 75, 55, 33, 45, 22, 40, 70]
sundrive_production = [38, 48, 32, 67, 55, 10, 63, 16, 25, 58, 52]
ecowheels_production = [40, 36, 28, 45, 10, 5, 50, 60, 55, 65, 18]

fig, ax = plt.subplots(figsize=(12, 8))

ax.plot(years, solartech_production, marker='o', linestyle='-', linewidth=2, color='royalblue')
ax.plot(years, sundrive_production, marker='s', linestyle='-', linewidth=2, color='crimson')
ax.plot(years, ecowheels_production, marker='^', linestyle='-', linewidth=2, color='limegreen')

ax.set_title("Solar Car Production (2010-2020)", fontsize=18, weight='bold', pad=20)
ax.set_xlabel("Year", fontsize=14)
ax.set_ylabel("Cars Produced (k)", fontsize=14)

ax.set_xticks(years)
ax.set_xticklabels(years, rotation=45)
ax.set_yticks(np.arange(0, 101, 10))
ax.set_yticklabels([f'{i}k' for i in range(0, 101, 10)])

# Annotate the data points
for i in range(len(years)):
    ax.text(years[i], solartech_production[i], f"{solartech_production[i]}k", ha='center', va='bottom', fontsize=10, color='royalblue')
    ax.text(years[i], sundrive_production[i], f"{sundrive_production[i]}k", ha='center', va='bottom', fontsize=10, color='crimson')
    ax.text(years[i], ecowheels_production[i], f"{ecowheels_production[i]}k", ha='center', va='bottom', fontsize=10, color='limegreen')

plt.tight_layout()
plt.show()