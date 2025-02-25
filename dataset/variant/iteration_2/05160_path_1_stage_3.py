import matplotlib.pyplot as plt
import numpy as np

decades = ['1990s', '2000s', '2010s', '2020s']
solar_production = np.array([10, 50, 500, 3000])

def calculate_growth(data):
    growth = []
    for i in range(1, len(data)):
        growth.append((data[i] - data[i-1]) / data[i-1] * 100)
    growth.insert(0, 0)
    return growth

growth_rates = calculate_growth(solar_production)

fig, axs = plt.subplots(1, 2, figsize=(15, 6))

axs[0].plot(decades, solar_production, marker='o', linestyle='-', linewidth=3, color='green', label='Production (GWh)')
axs[0].set_title("Solar Energy Surge", fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel("Decade", fontsize=14)
axs[0].set_ylabel("Production (GWh)", fontsize=14)
axs[0].legend(loc='upper left')
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)

for i, value in enumerate(solar_production):
    axs[0].annotate(f'{value}', (decades[i], solar_production[i]),
                    textcoords="offset points", xytext=(0, 10), ha='center')

axs[1].plot(decades, growth_rates, marker='o', linestyle='-', linewidth=3, color='green', label='Growth (%)')
axs[1].set_title("Growth Rate", fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel("Decade", fontsize=14)
axs[1].set_ylabel("Growth (%)", fontsize=14)
axs[1].legend(loc='upper left')
axs[1].yaxis.grid(True, linestyle='--', alpha=0.7)

for i, value in enumerate(growth_rates):
    axs[1].annotate(f'{value:.1f}%', (decades[i], growth_rates[i]), 
                    textcoords="offset points", xytext=(0, 10), ha='center')

plt.tight_layout()
plt.show()