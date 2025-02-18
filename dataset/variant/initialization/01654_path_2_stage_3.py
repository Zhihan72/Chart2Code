import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

years = np.arange(2010, 2021)
wind_power = np.array([140, 170, 220, 290, 360, 450, 560, 690, 850, 950, 1100])
total_power = wind_power
wind_percentage = 100

fig, ax = plt.subplots(figsize=(14, 8))

ax.barh(years, wind_power, height=0.4, color='black', alpha=0.7, label='Wind Power')

ax.set_title('The Rise of Renewable Energy:\nWind Power Trends (2010-2020)', fontsize=16, pad=20)
ax.set_xlabel('Energy Generation (TWh)', fontsize=12)
ax.set_ylabel('Year', fontsize=12)
ax.set_yticks(years)
ax.set_xticks(np.arange(0, 1201, 100))

ax.legend(title='Energy Source', loc='upper right')

ax.annotate('Wind Milestone:\n1,000 TWh', xy=(1100, 2020), xytext=(1000, 2018),
            arrowprops=dict(facecolor='black', arrowstyle='->'),
            fontsize=10, color='black')

ax.grid(True, linestyle='--', alpha=0.7)

for i, y_wind in enumerate(wind_power):
    ax.text(y_wind + 20, years[i], f'{y_wind}', va='center', fontsize=9, color='gray')

ax2 = ax.twiny()
ax2.barh(years, total_power, height=0.8, color='gray', alpha=0.3, label='Total Renewable')
ax2.set_xlabel('Total Energy Generation (TWh)', fontsize=12)
ax2.legend(loc='lower right')

ax_inset = inset_axes(ax, width="30%", height="30%", loc='lower right', borderpad=2)
ax_inset.plot([wind_percentage] * len(years), years, color='gray', linewidth=1.5, label='Wind %')
ax_inset.set_title('Share of Total (%)', fontsize=10)
ax_inset.set_yticks([2010, 2015, 2020])
ax_inset.set_xticks(np.arange(0, 101, 20))
ax_inset.grid(True, linestyle='--', alpha=0.5)
ax_inset.legend(fontsize=8, loc='upper right')

plt.tight_layout()

plt.show()