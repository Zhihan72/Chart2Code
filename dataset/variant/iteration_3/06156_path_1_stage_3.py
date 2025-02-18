import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2010, 2021)
salmon_catches = [150, 190, 140, 135, 165, 120, 180, 160, 155, 145, 130]
tuna_catches = [180, 200, 210, 230, 150, 160, 205, 220, 195, 175, 190]
cod_catches = [260, 295, 255, 250, 310, 320, 305, 270, 240, 300, 280]

fig, ax1 = plt.subplots(figsize=(14, 8))

# Shuffle the colors for each data group
ax1.plot(years, salmon_catches, marker='x', linestyle='--', linewidth=2, color='navy', label='Salmon')
ax1.plot(years, tuna_catches, marker='D', linestyle='-.', linewidth=2, color='darkgreen', label='Tuna')
ax1.plot(years, cod_catches, marker='*', linestyle='-', linewidth=2, color='salmon', label='Cod')

ax1.set_title("10-Year Seafood Catch Trends (2010-2020)", fontsize=18, fontweight='bold')
ax1.set_xlabel("Years", fontsize=14)
ax1.set_ylabel("Catch in Tons", fontsize=14)

ax1.grid(True, linestyle='-.', color='grey', alpha=0.5)

ax1.legend(title='Species', fontsize=10, loc='lower right', title_fontsize='13')

ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

plt.tight_layout()

plt.show()