import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

# Alter the data groups manually while maintaining size
reading = np.array([50, 55, 53, 54, 52, 56, 58, 59, 61, 62, 64])
gaming = np.array([22, 20, 26, 30, 34, 39, 44, 51, 54, 60, 66])
sports = np.array([32, 30, 36, 35, 37, 40, 41, 43, 45, 47, 49])
traveling = np.array([12, 10, 16, 19, 23, 25, 30, 37, 41, 44, 49])
cooking = np.array([16, 15, 19, 18, 21, 20, 24, 26, 29, 27, 31])
crafting = np.array([6, 5, 8, 7, 9, 11, 10, 13, 12, 14, 16])

hobbies_data = np.vstack([reading, gaming, sports, traveling, cooking, crafting])

colors = ['#F28C8C', '#72A1FF', '#8DEF8D', '#FFD98E', '#B6B6FF', '#FF89A1']

plt.figure(figsize=(14, 8))
plt.stackplot(years, hobbies_data, colors=colors, alpha=0.8)

plt.grid(visible=True, which='major', linestyle='-.', linewidth=0.8, alpha=0.6)
plt.tight_layout()

plt.show()