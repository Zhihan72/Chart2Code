import matplotlib.pyplot as plt
import numpy as np

countries = ['NOR', 'GER', 'USA', 'AUS', 'IND', 'BRA']
years = ['18', '19', '20', '21', '22']

norway_production = [50000, 51000, 52000, 53000, 55000]
germany_production = [200000, 210000, 220000, 230000, 250000]
usa_production = [300000, 315000, 320000, 335000, 360000]
australia_production = [150000, 160000, 170000, 180000, 195000]
india_production = [100000, 110000, 120000, 130000, 150000]
brazil_production = [80000, 85000, 90000, 95000, 100000]

data = [norway_production, germany_production, usa_production, australia_production, india_production, brazil_production]

fig, ax = plt.subplots(figsize=(14, 10))
height = 0.13
y = np.arange(len(years))

single_color = '#1f77b4'

for i, country_data in enumerate(data):
    rects = ax.barh(y + i * height, country_data, height, label=countries[i], color=single_color)
    for rect in rects:
        width = rect.get_width()
        ax.annotate(f'{width}', xy=(width, rect.get_y() + rect.get_height() / 2),
                    xytext=(3, 0), textcoords="offset points", ha='left', va='center', fontsize=10, color='black')

ax.set_ylabel('Yr', fontsize=12)
ax.set_xlabel('Prod. (GWh)', fontsize=12)
ax.set_title('Renewable Energy Prod.\n(18-22)', fontsize=18, fontweight='bold', pad=20)
ax.set_yticks(y + height * 2.5)
ax.set_yticklabels(years, fontsize=11)
ax.legend(title="Ctry", fontsize=9, loc='upper right')

ax.xaxis.grid(True, linestyle='-.', linewidth=1.0, alpha=0.7)
for spine in ax.spines.values():
    spine.set_edgecolor('#2ca02c')
    spine.set_linewidth(1.5)

plt.tight_layout()
plt.show()