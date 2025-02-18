import matplotlib.pyplot as plt
import numpy as np

# Years from 2000 to 2020
years = np.arange(2000, 2021)

# Artificial data for renewable energy production (MegaWatts) for three countries
country_data = {
    'EcoLand': [50, 55, 60, 70, 80, 95, 110, 125, 145, 170, 200, 235, 275, 320, 370, 425, 490, 565, 650, 745, 850],
    'GreenVille': [40, 45, 50, 55, 65, 80, 95, 110, 130, 155, 185, 220, 260, 305, 355, 410, 475, 545, 620, 705, 800],
    'Sustainia': [30, 35, 40, 45, 55, 70, 85, 100, 120, 145, 175, 210, 250, 295, 345, 400, 465, 535, 610, 695, 790]
}

global_growth_rate = np.array([40, 43, 46, 50, 55, 60, 66, 72, 79, 87, 96, 105, 115, 126, 138, 151, 165, 180, 196, 213, 231])

fig, ax1 = plt.subplots(figsize=(14, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99']

for country, color in zip(country_data.keys(), colors):
    ax1.plot(years, country_data[country], color=color, linewidth=2.5)

ax2 = ax1.twinx()
ax2.plot(years, global_growth_rate, color='black', linestyle='--', linewidth=2)

ax1.set_xticks(np.arange(2000, 2021, 2))
ax1.grid(True, linestyle='--', which='both', axis='both', alpha=0.6)

plt.tight_layout()
plt.show()