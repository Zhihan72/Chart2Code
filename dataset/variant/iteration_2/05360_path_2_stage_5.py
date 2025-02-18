import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)

campaign_A = np.array([2, 3, 5, 7, 11, 13, 15, 20, 23, 30, 35])
campaign_B = np.array([1, 2, 3, 5, 8, 12, 17, 25, 31, 38, 45])
campaign_C = np.array([0, 1, 2, 4, 7, 10, 13, 18, 22, 29, 33])
campaign_D = np.array([1, 3, 4, 6, 9, 14, 19, 27, 32, 40, 47])
campaign_E = np.array([2, 4, 4, 5, 9, 11, 16, 22, 29, 35, 39])

fig, ax1 = plt.subplots(figsize=(12, 5))

ax1.plot(years, campaign_A, marker='v', linestyle='--', color='blue', label='Camp A', linewidth=1.5)
ax1.plot(years, campaign_B, marker='x', linestyle='-.', color='magenta', label='Sector B', linewidth=1.5)
ax1.plot(years, campaign_C, marker='p', linestyle='-', color='cyan', label='Initiative C', linewidth=1.5)
ax1.plot(years, campaign_D, marker='h', linestyle='--', color='lime', label='Team D', linewidth=1.5)
ax1.plot(years, campaign_E, marker='D', linestyle=':', color='brown', label='Drive E', linewidth=1.5)

ax1.set_title('Yearly Planting in EcoVille (2010-2020)', fontsize=16, fontweight='bold', pad=15)
ax1.set_xlabel('Year', fontsize=14)
ax1.set_ylabel('Planted Trees (K)', fontsize=14)
ax1.legend(title='Groups', loc='lower right', fontsize=10, title_fontsize=11)
ax1.grid(True, linestyle='-', alpha=0.5)

# Changed border style of plot
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

plt.tight_layout()
plt.show()