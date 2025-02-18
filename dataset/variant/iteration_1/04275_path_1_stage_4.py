import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
solarland = np.array([118, 140, 155, 165, 195, 220, 235, 225, 205, 185, 155, 125])
ecotopia = np.array([85, 95, 115, 135, 155, 185, 205, 190, 180, 150, 125, 105])
sunstate = np.array([90, 115, 130, 140, 170, 190, 200, 195, 175, 165, 135, 120])

fig, ax = plt.subplots(figsize=(12, 7))

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

ax.legend(loc='lower right', title='Energy Sources')
ax2.legend(loc='upper left', title='Combined Total')

ax.grid(visible=True, linestyle='-', color='gray', alpha=0.3)
plt.tight_layout()

plt.show()