import matplotlib.pyplot as plt
import numpy as np

commodities = ['Martian Minerals', 'Earthly Technologies', 
               'Agricultural Products', 'Water Resources', 
               'Medical Supplies']
trade_volumes = [200, 150, 180, 120, 90]
trade_values = [50, 70, 55, 40, 30]

new_colors = ['#6495ED', '#FFD700', '#ADFF2F', '#FF69B4', '#00CED1']

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 7))

bars = ax1.bar(np.arange(len(commodities)), trade_volumes, color=new_colors)

ax1.set_title('Intergalactic Trade Commodities:\nEarth to Mars Exchange in 2150', fontsize=16, fontweight='bold')
ax1.set_xlabel('Commodities', fontsize=14)
ax1.set_ylabel('Trade Volume (in thousands of tons)', fontsize=14)
ax1.set_xticks(np.arange(len(commodities)))
ax1.set_xticklabels(commodities, rotation=45, ha='right')

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2, yval + 3, f'{yval}k', ha='center', va='bottom', fontsize=12)

ax2.pie(trade_values, labels=commodities, autopct='%1.1f%%', startangle=140, colors=new_colors)

plt.tight_layout()
plt.show()