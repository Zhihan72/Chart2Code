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

fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].plot(decades, solar_production, marker='o', linestyle='-', linewidth=3, color='orange')
axs[0].set_title("Solar Energy (GWh) by Decade", fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel("Decade", fontsize=14)
axs[0].set_ylabel("Production", fontsize=14)

for i, value in enumerate(solar_production):
    axs[0].annotate(f'{value} GWh', (decades[i], solar_production[i]),
                    textcoords="offset points", xytext=(0, 10), ha='center')

axs[1].plot(decades, growth_rates, marker='o', linestyle='-', linewidth=3, color='blue')
axs[1].set_xlabel("Decade", fontsize=14)
axs[1].set_ylabel("Growth (%)", fontsize=14)

for i, value in enumerate(growth_rates):
    axs[1].annotate(f'{value:.1f}%', (decades[i], growth_rates[i]), 
                    textcoords="offset points", xytext=(0, 10), ha='center')

plt.tight_layout()
plt.show()