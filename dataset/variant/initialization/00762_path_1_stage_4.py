import matplotlib.pyplot as plt
import numpy as np

commodities = ['Martian Minerals']
trade_volumes = [200]

# Shuffled color for the bar
# Original color was ['#FF5733']
shuffled_colors = ['#32CD32']  # Swapped with a new color

fig, ax1 = plt.subplots(1, 1, figsize=(8, 7))
bars = ax1.bar(np.arange(len(commodities)), trade_volumes, color=shuffled_colors, edgecolor='black')

ax1.set_title('Intergalactic Trade Commodities:\nEarth to Mars Exchange in 2150', fontsize=16, fontweight='bold')
ax1.set_xlabel('Commodity', fontsize=14)
ax1.set_ylabel('Trade Volume (in thousands of tons)', fontsize=14)
ax1.set_xticks(np.arange(len(commodities)))
ax1.set_xticklabels(commodities, rotation=45, ha='right')

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 3, f'{yval}k', ha='center', va='bottom', fontsize=12)

ax1.legend(bars, ['Rich Martian ore deposits'], title='Commodity Description', loc='upper right')
ax1.yaxis.grid(True, linestyle='--', alpha=0.6)

plt.show()