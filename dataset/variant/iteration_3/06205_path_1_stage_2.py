import matplotlib.pyplot as plt
import numpy as np

regions = ['North', 'South', 'West']
years = ['2019', '2020', '2021', '2022']

north_generation = np.array([25, 30, 25, 35])
south_generation = np.array([20, 25, 30, 30])
west_generation = np.array([15, 20, 35, 40])

north_cumulative = np.cumsum(north_generation)
south_cumulative = np.cumsum(south_generation)
west_cumulative = np.cumsum(west_generation)

colors = ['#ff9999', '#66b3ff', '#99ff99']

fig, axs = plt.subplots(nrows=2, figsize=(12, 10), constrained_layout=True)

x = np.arange(len(years))
bar_width = 0.25

axs[0].bar(x - bar_width, north_generation, width=bar_width, color=colors[0], label='North')
axs[0].bar(x, south_generation, width=bar_width, color=colors[1], label='South')
axs[0].bar(x + bar_width, west_generation, width=bar_width, color=colors[2], label='West')

axs[0].set_xlabel('Year', fontsize=12)
axs[0].set_ylabel('Solar Power Generation (GWh)', fontsize=12)
axs[0].set_title('Annual Solar Power Generation by Region', fontsize=16, fontweight='bold', style='italic')
axs[0].set_xticks(x)
axs[0].set_xticklabels(years)
axs[0].legend(title='Regions', loc='upper left', frameon=False)
axs[0].yaxis.grid(True, linestyle=':', linewidth=1.5, alpha=0.5)

axs[1].bar(years, north_cumulative, color=colors[0], label='North', bottom=south_cumulative + west_cumulative)
axs[1].bar(years, south_cumulative, color=colors[1], label='South', bottom=west_cumulative)
axs[1].bar(years, west_cumulative, color=colors[2], label='West')

axs[1].set_xlabel('Year', fontsize=12)
axs[1].set_ylabel('Cumulative Solar Power Generation (GWh)', fontsize=12)
axs[1].set_title('Cumulative Solar Power Generation by Region', fontsize=16, fontweight='normal', style='oblique')

for i, (n, s, w) in enumerate(zip(north_cumulative, south_cumulative, west_cumulative)):
    axs[1].text(i, n + s + w + 2, f'{n+s+w} GWh', ha='center', va='bottom', fontsize=10, fontweight='normal', rotation=45)

axs[1].legend(title='Regions', bbox_to_anchor=(0.5, 1), loc='upper right', framealpha=0.5)

plt.show()