import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
solarland = np.array([120, 135, 150, 170, 190, 215, 240, 230, 210, 190, 160, 130])
ecotopia = np.array([80, 100, 120, 140, 160, 180, 200, 195, 175, 155, 130, 100])
sunstate = np.array([95, 110, 125, 145, 165, 185, 205, 200, 180, 160, 140, 115])

fig, ax = plt.subplots(figsize=(12, 7))

# Random changes to the line styles, colors, and markers
ax.plot(months, solarland, label='Sol', marker='D', linestyle='-.', color='#FF33AA', linewidth=2)
ax.plot(months, ecotopia, label='Eco', marker='x', linestyle=':', color='#AA33FF', linewidth=2)
ax.plot(months, sunstate, label='Sun', marker='+', linestyle='-', color='#33AADD', linewidth=2)

total_kWh = solarland + ecotopia + sunstate
ax2 = ax.twinx()
ax2.plot(months, total_kWh, label='Total', color='black', linestyle='-', linewidth=2)

significant_months = [2, 6, 10]
for i in significant_months:
    ax.annotate(f'{solarland[i]}', xy=(months[i], solarland[i]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='#FF33AA')
    ax.annotate(f'{ecotopia[i]}', xy=(months[i], ecotopia[i]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='#AA33FF')
    ax.annotate(f'{sunstate[i]}', xy=(months[i], sunstate[i]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='#33AADD')
    ax2.annotate(f'{total_kWh[i]}', xy=(months[i], total_kWh[i]), xytext=(0, -20), textcoords='offset points', fontsize=9, color='black')

ax.set_title('Solar Power Surge', fontsize=16, pad=20, weight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('kWh Produced (Countries)', fontsize=12)
ax2.set_ylabel('Total kWh', fontsize=12, color='black')

# Randomly change the legend's position and title
ax.legend(loc='lower right', title='Energy Sources')
ax2.legend(loc='upper left', title='Combined Total')

# Modify the grid style
ax.grid(visible=True, linestyle='-', color='gray', alpha=0.3)
plt.tight_layout()

plt.show()