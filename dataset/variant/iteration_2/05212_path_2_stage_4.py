import matplotlib.pyplot as plt
import numpy as np

countries = ['NOR', 'GER', 'USA', 'AUS', 'IND', 'BRA']
years = ['18', '19', '20', '21', '22']

# Renewable energy production in Gigawatt-hours (GWh)
norway_production = [50000, 51000, 52000, 53000, 55000]
germany_production = [200000, 210000, 220000, 230000, 250000]
usa_production = [300000, 315000, 320000, 335000, 360000]
australia_production = [150000, 160000, 170000, 180000, 195000]
india_production = [100000, 110000, 120000, 130000, 150000]
brazil_production = [80000, 85000, 90000, 95000, 100000]

data = [norway_production, germany_production, usa_production, australia_production, india_production, brazil_production]

fig, ax = plt.subplots(figsize=(14, 8))
width = 0.13
x = np.arange(len(years))

# Single consistent color for all data groups
single_color = '#1f77b4'

# Plot each country's data with a consistent color
for i, country_data in enumerate(data):
    rects = ax.bar(x + i * width, country_data, width, label=countries[i], color=single_color)
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

ax.set_xlabel('Yr', fontsize=12)
ax.set_ylabel('Prod. (GWh)', fontsize=12)
ax.set_title('Renewable Energy Prod.\n(18-22)', fontsize=18, fontweight='bold', pad=20)
ax.set_xticks(x + width * 2.5)
ax.set_xticklabels(years, fontsize=11)
ax.legend(title="Ctry", fontsize=9, loc='lower center')

ax.yaxis.grid(True, linestyle='-.', linewidth=1.0, alpha=0.7)
for spine in ax.spines.values():
    spine.set_edgecolor('#2ca02c')
    spine.set_linewidth(1.5)

# Removing multiple colors/lines, using the same color and markers
marker_style = 'o'
linestyle = '-'

for i, country_data in enumerate(data):
    ax.plot(x + i * width, country_data, marker=marker_style, linestyle=linestyle, color=single_color)

plt.tight_layout()
plt.show()