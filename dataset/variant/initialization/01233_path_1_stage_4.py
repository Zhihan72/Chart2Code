import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2023, 2029)
countries = ['Country A', 'Country B', 'Country C', 'Country D', 'Country E', 'Country F', 'Country G']

solar = np.array([
    [10, 15, 20, 25, 30, 35],
    [5, 10, 15, 20, 25, 30],
    [8, 12, 18, 23, 28, 34],
    [12, 17, 22, 28, 33, 38],
    [7, 13, 19, 24, 30, 36],
    [11, 16, 21, 27, 32, 37],
    [6, 11, 17, 22, 27, 33]   
])

wind = np.array([
    [15, 20, 25, 30, 35, 40],
    [12, 16, 22, 27, 32, 37],
    [10, 15, 20, 27, 33, 38],
    [18, 24, 30, 35, 40, 45],
    [11, 17, 23, 28, 33, 39],
    [13, 18, 24, 30, 35, 41],
    [9, 14, 18, 24, 30, 35]   
])

hydro = np.array([
    [20, 25, 28, 32, 35, 40],
    [18, 23, 28, 32, 36, 41],
    [14, 20, 24, 30, 36, 42],
    [16, 21, 27, 33, 38, 44],
    [19, 24, 29, 34, 38, 44],
    [17, 22, 26, 31, 37, 43],
    [12, 17, 22, 27, 32, 38]   
])

total_renewable = solar + wind + hydro
annual_totals = total_renewable.sum(axis=0)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))

bar_width = 0.1
new_colors = ['#FF7F50', '#2E8B57', '#8A2BE2']  # New colors for solar, wind, and hydroelectric energy

for year_index, year in enumerate(years):
    year_totals = total_renewable[:, year_index]
    sorted_indices = np.argsort(year_totals)

    for i, index in enumerate(sorted_indices):
        ax1.bar(year + i * bar_width, solar[index][year_index], width=bar_width, color=new_colors[0], alpha=0.8)
        ax1.bar(year + i * bar_width, wind[index][year_index], width=bar_width, bottom=solar[index][year_index], color=new_colors[1], alpha=0.8)
        ax1.bar(year + i * bar_width, hydro[index][year_index], width=bar_width, bottom=solar[index][year_index] + wind[index][year_index], color=new_colors[2], alpha=0.8)

ax1.set_xlabel('Timeline', fontsize=12)
ax1.set_ylabel('Usage of Renewables (%)', fontsize=12)
ax1.set_title('Renewable Energy Forecasted Trends\n(2023-2028)', fontsize=14, fontweight='bold')
ax1.set_xticks(years + bar_width * 3)

handles = [plt.Rectangle((0,0),1,1, color=color, alpha=0.8) for color in new_colors]
ax1.legend(handles, ['Solar Power', 'Wind Energy', 'Hydroelectric'], loc='upper left', fontsize=10, title='Types of Energy')
ax1.grid(True, linestyle='--', linewidth=0.5, alpha=0.7)

ax2.plot(years, annual_totals, marker='o', color='#FF6347', linewidth=2, label='Overall Renewable Usage')

for (year, total) in zip(years, annual_totals):
    ax2.text(year, total + 2, f'{total}', ha='center', fontsize=9, color='#FF6347')

ax2.set_xlabel('Yearly Timeline', fontsize=12)
ax2.set_ylabel('Total Usage of Renewables (%)', fontsize=12)
ax2.set_title('Overall Growth in Renewable Energy\n(2023-2028)', fontsize=14, fontweight='bold')

ax2.set_xticks(years)
ax2.set_xticklabels(years)
ax2.legend(loc='upper left', fontsize=10)

plt.tight_layout()
plt.show()