import matplotlib.pyplot as plt
import numpy as np

countries = ['Australia', 'India', 'Germany', 'USA', 'Norway']
years = ['2022', '2019', '2020', '2018', '2021']

norway_production = [53000, 51000, 52000, 50000, 55000]
germany_production = [230000, 210000, 220000, 200000, 250000]
usa_production = [320000, 315000, 300000, 335000, 360000]
australia_production = [150000, 195000, 160000, 180000, 170000]
india_production = [130000, 150000, 100000, 110000, 120000]

data = [australia_production, india_production, germany_production, usa_production, norway_production]

fig, ax = plt.subplots(figsize=(14, 8))

width = 0.15
x = np.arange(len(years))

colors = ['#ffcc99', '#c2c2f0', '#66b3ff', '#99ff99', '#ff9999']

for i, (country_data, color) in enumerate(zip(data, colors)):
    rects = ax.bar(x + i * width, country_data, width, label=countries[i], color=color)
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

ax.set_xlabel('Year of Production', fontsize=12)
ax.set_ylabel('Energy Output (GWh)', fontsize=12)
ax.set_title('Renewable Output per Year\n(2018-2022)', fontsize=18, fontweight='bold', pad=20)
ax.set_xticks(x + width * 2)
ax.set_xticklabels(years, fontsize=11)
ax.legend(title="Nations", fontsize=10, loc='upper left')

ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()