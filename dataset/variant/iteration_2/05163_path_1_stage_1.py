import numpy as np
import matplotlib.pyplot as plt

years = np.array([2010, 2012, 2014, 2016, 2018, 2020, 2022])
clay_yield = np.array([20, 22, 21, 24, 26, 25, 28])
loam_yield = np.array([30, 32, 33, 35, 36, 38, 40])
sandy_yield = np.array([15, 17, 16, 18, 20, 19, 21])

soil_types = ['Clay', 'Loam', 'Sandy']
average_ph = [6.5, 7.2, 6.8]

fig, axs = plt.subplots(1, 2, figsize=(15, 7))

axs[0].scatter(years, clay_yield, color='brown', s=100, alpha=0.7, edgecolors='k', marker='o')
axs[0].scatter(years, loam_yield, color='green', s=100, alpha=0.7, edgecolors='k', marker='s')
axs[0].scatter(years, sandy_yield, color='yellow', s=100, alpha=0.7, edgecolors='k', marker='D')

clay_coefs = np.polyfit(years, clay_yield, 1)
loam_coefs = np.polyfit(years, loam_yield, 1)
sandy_coefs = np.polyfit(years, sandy_yield, 1)

axs[0].plot(years, np.poly1d(clay_coefs)(years), color='brown', linestyle='--')
axs[0].plot(years, np.poly1d(loam_coefs)(years), color='green', linestyle='--')
axs[0].plot(years, np.poly1d(sandy_coefs)(years), color='yellow', linestyle='--')

axs[0].set_title('Crop Yield Over Time on Different Soil Types', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Crop Yield (tons per hectare)', fontsize=12)

axs[1].bar(soil_types, average_ph, color=['brown', 'green', 'yellow'], alpha=0.7)
axs[1].set_title('Average PH Values of Different Soil Types', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Soil Type', fontsize=12)
axs[1].set_ylabel('PH Value', fontsize=12)
axs[1].set_ylim(6, 8)
axs[1].set_yticks(np.arange(6, 8.5, 0.5))

plt.tight_layout()
plt.show()