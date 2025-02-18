import matplotlib.pyplot as plt
import numpy as np

years = np.arange(2000, 2021)

country_data = {
    'LandEcono': [50, 55, 70, 60, 95, 80, 110, 145, 170, 125, 200, 265, 235, 320, 370, 425, 490, 565, 650, 745, 850],
    'VilleGreen': [45, 40, 50, 55, 80, 65, 95, 110, 155, 130, 185, 260, 220, 305, 355, 410, 545, 475, 620, 705, 800],
    'TainiaSus': [40, 35, 30, 55, 70, 45, 100, 120, 85, 145, 175, 250, 210, 295, 345, 400, 465, 535, 610, 695, 790]
}

global_growth_rate = np.array([46, 43, 40, 55, 60, 50, 72, 79, 66, 87, 96, 105, 115, 138, 126, 151, 165, 180, 196, 213, 231])

fig, ax1 = plt.subplots(figsize=(14, 8))

# New set of colors
colors = ['#8e44ad', '#e74c3c', '#3498db']

for country, color in zip(country_data.keys(), colors):
    ax1.plot(years, country_data[country], color=color, linewidth=2.5, label=country)

ax2 = ax1.twinx()
ax2.plot(years, global_growth_rate, color='black', linestyle='--', linewidth=2, label='Worldwide Growth Rate')

ax1.set_title("Analyzing Renewable Power Generation Trends\nAmong Nations (2000-2020)", fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Time (Year)', fontsize=12)
ax1.set_ylabel('Output in MegaWatts', fontsize=12)
ax2.set_ylabel('World Growth Rate Index', fontsize=12, color='black')

ax1.set_xticks(np.arange(2000, 2021, 2))
ax1.set_xticklabels(np.arange(2000, 2021, 2), fontsize=10, rotation=45)

ax1.legend(loc='upper left', fontsize=10, title='Nation Data')
ax2.legend(loc='upper right', fontsize=10, title='Rate Metrics')

ax1.grid(True, linestyle='--', which='both', axis='both', alpha=0.6)

milestones = {
    2008: 'LandEcono reaches 100MW',
    2016: 'VilleGreen achieves 400MW',
    2020: 'TainiaSus nears 800MW'
}

for year, text in milestones.items():
    ax1.annotate(text, 
                xy=(year, country_data['LandEcono'][year-2000]), 
                xytext=(year-3, country_data['LandEcono'][year-2000]+50),
                arrowprops=dict(facecolor='black', arrowstyle='->'),
                fontsize=10, color='brown')

plt.tight_layout()
plt.show()