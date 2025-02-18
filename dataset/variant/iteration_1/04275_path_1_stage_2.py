import matplotlib.pyplot as plt
import numpy as np

months = np.array(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
solarland = np.array([120, 135, 150, 170, 190, 215, 240, 230, 210, 190, 160, 130])
ecotopia = np.array([80, 100, 120, 140, 160, 180, 200, 195, 175, 155, 130, 100])
sunstate = np.array([95, 110, 125, 145, 165, 185, 205, 200, 180, 160, 140, 115])

fig, ax = plt.subplots(figsize=(12, 7))

ax.plot(months, solarland, label='Sol', marker='o', linestyle='-', color='#33FF57', linewidth=2)
ax.plot(months, ecotopia, label='Eco', marker='s', linestyle='-', color='#3357FF', linewidth=2)
ax.plot(months, sunstate, label='Sun', marker='^', linestyle='-', color='#FF5733', linewidth=2)

total_kWh = solarland + ecotopia + sunstate
ax2 = ax.twinx()
ax2.plot(months, total_kWh, label='Total', color='gray', linestyle='--', linewidth=1.5)

significant_months = [2, 6, 10]
for i in significant_months:
    ax.annotate(f'{solarland[i]}', xy=(months[i], solarland[i]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='#33FF57')
    ax.annotate(f'{ecotopia[i]}', xy=(months[i], ecotopia[i]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='#3357FF')
    ax.annotate(f'{sunstate[i]}', xy=(months[i], sunstate[i]), xytext=(5, 5), textcoords='offset points', fontsize=9, color='#FF5733')
    ax2.annotate(f'{total_kWh[i]}', xy=(months[i], total_kWh[i]), xytext=(0, -20), textcoords='offset points', fontsize=9, color='gray')

ax.set_title('Solar Power Surge', fontsize=16, pad=20, weight='bold')
ax.set_xlabel('Month', fontsize=12)
ax.set_ylabel('kWh Produced (Countries)', fontsize=12)
ax2.set_ylabel('Total kWh', fontsize=12, color='gray')

ax.legend(loc='upper left', bbox_to_anchor=(0.05, 1), title='Countries')
ax2.legend(loc='upper right', bbox_to_anchor=(0.95, 1), title='Total')

ax.grid(visible=True, linestyle='--', alpha=0.6)
plt.tight_layout()

plt.show()