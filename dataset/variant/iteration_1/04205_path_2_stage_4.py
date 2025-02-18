import matplotlib.pyplot as plt
import numpy as np

years = np.arange(1970, 2021)

fossil_fuels = [12000, 12500, 13000, 13500, 14000, 14500, 15000, 15500, 16000, 16500,
                17000, 17000, 16800, 16600, 16400, 16000, 15800, 15600, 15500, 15400,
                15300, 15000, 14500, 14000, 13500, 13000, 12600, 12200, 11800, 11400,
                10800, 10300, 10000, 9800, 9600, 9400, 9200, 9000, 8800, 8600,
                8350, 8100, 7900, 7650, 7400, 7150, 6900, 6650, 6400, 6200, 6000]

solar = [0, 0, 0, 0, 0, 0, 0, 0, 0, 10,
         20, 30, 50, 70, 100, 150, 200, 270, 350, 450,
         600, 800, 1050, 1300, 1600, 2000, 2500, 3100, 3800, 4500,
         5200, 5900, 6500, 7400, 8200, 9000, 9800, 10500, 11200, 11900,
         12600, 13300, 14100, 14800, 15600, 16400, 17200, 18100, 19000, 20000, 21000]

wind = [0, 0, 0, 0, 0, 0, 0, 0, 0, 20,
        50, 80, 110, 160, 210, 260, 320, 400, 480, 580,
        700, 850, 1000, 1200, 1400, 1650, 1900, 2200, 2550, 2900,
        3300, 3700, 4150, 4700, 5300, 5900, 6500, 7150, 7850, 8600,
        9300, 10100, 11000, 11800, 12600, 13400, 14300, 15100, 16000, 17000, 18000]

hydro = [3000, 3100, 3200, 3300, 3400, 3500, 3600, 3700, 3750, 3800,
         3850, 3900, 4000, 4100, 4200, 4300, 4500, 4700, 4800, 4900,
         5000, 5100, 5200, 5400, 5600, 5700, 5800, 5900, 6000, 6100,
         6200, 6300, 6400, 6500, 6600, 6750, 6900, 7050, 7200, 7400,
         7600, 7800, 8000, 8200, 8400, 8600, 8800, 9000, 9200, 9400, 9600]

fossil_fuels = np.array(fossil_fuels)
solar = np.array(solar)
wind = np.array(wind)
hydro = np.array(hydro)

energy_data = np.row_stack([fossil_fuels, solar, wind, hydro])

sources = ['Breeze', 'Sunshine', 'Fossil Commodities', 'Water']
colors = ['#4682B4', '#FF8C00', '#FF6347', '#3CB371']

fig, ax = plt.subplots(figsize=(14, 8))
ax.stackplot(years, energy_data, labels=sources, colors=colors, alpha=0.85)

total_energy = energy_data.sum(axis=0)
ax.plot(years, total_energy, color='purple', linewidth=1.5, marker='s', linestyle='--', label='Total Energy')

ax.set_title("Evolution of Global Energy Sources (1970-2020)\nA Shift to Renewables", 
             fontsize=16, fontstyle='italic', wrap=True)
ax.set_xlabel('Year', fontsize=12, color='grey')
ax.set_ylabel('Energy Output (TWh)', fontsize=12, color='grey')

ax.grid(True, linestyle='-.', alpha=0.7)

ax.legend(loc='lower left', bbox_to_anchor=(-0.05, -0.2), fontsize=10, title='Sources')

plt.xticks(rotation=30)

plt.tight_layout()

plt.show()