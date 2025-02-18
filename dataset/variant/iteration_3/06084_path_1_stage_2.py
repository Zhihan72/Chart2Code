import matplotlib.pyplot as plt
import numpy as np

divisions = ['Eurasia', 'Oceania', 'Pan Africa', 'Latin America', 'USA-Canada', 'EuroZone']
years = [2018, 2019, 2020, 2021, 2022]

production = np.array([
    [20, 21, 23, 24, 26],  
    [18, 19, 22, 23, 25],  
    [15, 17, 20, 21, 23],  
    [12, 14, 16, 18, 19],  
    [10, 13, 15, 17, 18],  
    [8, 10, 12, 13, 14],   
])

fig, ax = plt.subplots(figsize=(14, 8))

bar_width = 0.15
common_color = 'skyblue'  # Single color for all bars

for i, year in enumerate(years):
    bar_positions = np.arange(len(divisions)) + i * bar_width
    ax.bar(bar_positions, production[:, i], bar_width, label=f'{year}', color=common_color)

ax.set_title("Power Generation by Global Clusters (2018-2022)\nSub-Global Contributions", fontsize=16, fontweight='bold')
ax.set_xlabel("Global Clusters", fontsize=14)
ax.set_ylabel("Output (GW)", fontsize=14)

ax.legend(title='Calendar Year', fontsize=12)

ax.set_xticks(np.arange(len(divisions)) + 2 * bar_width)
ax.set_xticklabels(divisions, rotation=45, ha='right', fontsize=12)

ax.yaxis.grid(True, linestyle='--', alpha=0.7)

total_production_start = production.sum(axis=0)[0]
total_production_end = production.sum(axis=0)[-1]
ax.annotate(f'Overall Rise: {total_production_end - total_production_start} GW', 
             xy=(2.5, total_production_end), xytext=(3, total_production_end + 10),
             arrowprops=dict(facecolor='black', shrink=0.05),
             fontsize=13, color='black', fontweight='bold')

plt.tight_layout()
plt.show()