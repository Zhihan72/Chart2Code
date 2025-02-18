import matplotlib.pyplot as plt
import numpy as np

countries = ['Norway', 'Germany', 'USA', 'Australia', 'India']
years = ['2018', '2019', '2020', '2021', '2022']

norway_production = [50000, 51000, 52000, 53000, 55000]
germany_production = [200000, 210000, 220000, 230000, 250000]
usa_production = [300000, 315000, 320000, 335000, 360000]
australia_production = [150000, 160000, 170000, 180000, 195000]
india_production = [100000, 110000, 120000, 130000, 150000]

data = [norway_production, germany_production, usa_production, australia_production, india_production]

fig, ax = plt.subplots(figsize=(14, 8))

width = 0.15
x = np.arange(len(years))

# New colors for each country
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']

for i, (country_data, color) in enumerate(zip(data, colors)):
    rects = ax.bar(x + i * width, country_data, width, label=countries[i], color=color)
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}', xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3), textcoords="offset points", ha='center', va='bottom', fontsize=10, color='black')

ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Renewable Energy Production (GWh)', fontsize=12)
ax.set_title('Annual Renewable Energy Production\n(2018-2022)', fontsize=18, fontweight='bold', pad=20)
ax.set_xticks(x + width * 2)
ax.set_xticklabels(years, fontsize=11)
ax.legend(title="Country", fontsize=10, loc='upper left')

ax.yaxis.grid(True, linestyle='--', linewidth=0.7, alpha=0.7)

plt.tight_layout()
plt.show()