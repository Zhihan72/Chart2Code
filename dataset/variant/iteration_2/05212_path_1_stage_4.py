import matplotlib.pyplot as plt
import numpy as np

countries = ['Australia', 'India', 'Germany', 'USA', 'Norway', 'Brazil']
years = ['2022', '2019', '2020', '2018', '2021']

norway_production = [53000, 51000, 52000, 50000, 55000]
germany_production = [230000, 210000, 220000, 200000, 250000]
usa_production = [320000, 315000, 300000, 335000, 360000]
australia_production = [150000, 195000, 160000, 180000, 170000]
india_production = [130000, 150000, 100000, 110000, 120000]
brazil_production = [110000, 105000, 115000, 120000, 125000]  # New data for Brazil

data = [australia_production, india_production, germany_production, usa_production, norway_production, brazil_production]

fig, ax = plt.subplots(figsize=(14, 8))

width = 0.13  # Adjusted bar width due to additional data series
y = np.arange(len(years))

colors = ['#ffcc99', '#c2c2f0', '#66b3ff', '#99ff99', '#ff9999', '#ffb3e6']  # Added color for Brazil

for i, (country_data, color) in enumerate(zip(data, colors)):
    rects = ax.barh(y + i * width, country_data, height=width, label=countries[i], color=color)
    for rect in rects:
        width = rect.get_width()
        ax.annotate(f'{width}', xy=(width, rect.get_y() + rect.get_height() / 2),
                    xytext=(3, 0), textcoords="offset points", ha='left', va='center', fontsize=10, color='black')

ax.set_ylabel('Year of Production', fontsize=12)
ax.set_xlabel('Energy Output (GWh)', fontsize=12)
ax.set_title('Renewable Output per Year\n(2018-2022)', fontsize=18, fontweight='bold', pad=20)
ax.set_yticks(y + width * 2.5)  # Adjusted y-ticks to center the labels
ax.set_yticklabels(years, fontsize=11)
ax.legend(title="Nations", fontsize=10, loc='lower right')

ax.xaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()