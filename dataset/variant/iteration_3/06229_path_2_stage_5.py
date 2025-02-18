import matplotlib.pyplot as plt
import numpy as np

cities = ['Springfield', 'Shelbyville', 'Ogdenville', 'N. Haverbrook', 'Capital City']
years = ['2019', '2020', '2021', '2022', '2023']

gardens_setup = np.array([
    [12, 15, 19, 20, 24],
    [10, 12, 15, 18, 22],
    [7, 10, 13, 15, 20],
    [5, 8, 10, 12, 16],
    [14, 18, 21, 22, 25]
])

harvest_yield = np.array([
    [1200, 1350, 1500, 1600, 1800],
    [1100, 1225, 1375, 1475, 1600],
    [700, 900, 1000, 1100, 1250],
    [500, 750, 850, 950, 1100],
    [1400, 1500, 1600, 1700, 1800]
])

total_harvest_yield = harvest_yield.sum(axis=1)

fig, (ax2, ax1) = plt.subplots(1, 2, figsize=(14, 7), constrained_layout=True)

# Subplot 2: Bar chart for total harvest yield now ax2 is first
bars = ax2.bar(cities, total_harvest_yield, color='skyblue')

for bar, yield_amount in zip(bars, total_harvest_yield):
    ax2.annotate(f'{yield_amount} kg', 
                 xy=(bar.get_x() + bar.get_width() / 2, bar.get_height()),
                 xytext=(0, 5), textcoords="offset points",
                 ha='center', va='bottom', fontsize=10, color='black')

ax2.set_xlabel("Cities", fontsize=12)
ax2.set_ylabel("Yield (kg)", fontsize=12)

# Subplot 1: Bar chart for gardens setup now ax1 is second
bar_width = 0.15
indices = np.arange(len(cities))

for i, year in enumerate(years):
    bars = ax1.bar(indices + i * bar_width, gardens_setup[:, i], width=bar_width, color='skyblue')
    
    for bar in bars:
        height = bar.get_height()
        if height > 5: 
            ax1.annotate(f'{int(height)}', 
                         xy=(bar.get_x() + bar.get_width() / 2, bar.get_height() / 2),
                         xytext=(0, 0), textcoords="offset points",
                         ha='center', va='center', fontsize=8, color='white')

ax1.set_xlabel("Cities", fontsize=12)
ax1.set_ylabel("Number of Gardens", fontsize=12)

ax1.set_xticks(indices + bar_width * (len(years) - 1) / 2)
ax1.set_xticklabels(cities)

plt.show()