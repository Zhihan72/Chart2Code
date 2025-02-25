import matplotlib.pyplot as plt
import numpy as np

decades = ['1990s', '2000s', '2010s', '2020s']
solar_production = np.array([10, 50, 500, 3000])
wind_production = np.array([5, 20, 200, 2500])  # Made-up data for wind energy production

def calculate_growth(data):
    growth = []
    for i in range(1, len(data)):
        growth.append((data[i] - data[i-1]) / data[i-1] * 100)
    growth.insert(0, 0)
    return growth

solar_growth_rates = calculate_growth(solar_production)
wind_growth_rates = calculate_growth(wind_production)

fig, axs = plt.subplots(1, 2, figsize=(15, 6))

axs[0].plot(decades, solar_production, marker='s', linestyle='--', linewidth=2, color='blue', label='Solar (GWh)')
axs[0].plot(decades, wind_production, marker='o', linestyle='-', linewidth=2, color='green', label='Wind (GWh)')
axs[0].set_title("Energy Production Comparison", fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel("Decade", fontsize=14)
axs[0].set_ylabel("Production (GWh)", fontsize=14)
axs[0].legend(loc='upper left')
axs[0].yaxis.grid(False)

for i, value in enumerate(solar_production):
    axs[0].annotate(f'{value}', (decades[i], solar_production[i]), 
                    textcoords="offset points", xytext=(0, -15), ha='center')
for i, value in enumerate(wind_production):
    axs[0].annotate(f'{value}', (decades[i], wind_production[i]), 
                    textcoords="offset points", xytext=(0, 10), ha='center')

axs[1].plot(decades, solar_growth_rates, marker='*', linestyle='-.', linewidth=4, color='red', label='Solar Growth (%)')
axs[1].plot(decades, wind_growth_rates, marker='d', linestyle=':', linewidth=2, color='purple', label='Wind Growth (%)')
axs[1].set_title("Growth Rate Comparison", fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel("Decade", fontsize=14)
axs[1].set_ylabel("Growth (%)", fontsize=14)
axs[1].legend(loc='upper right')
axs[1].xaxis.grid(True, linestyle=':', alpha=0.5)

for i, value in enumerate(solar_growth_rates):
    axs[1].annotate(f'{value:.1f}%', (decades[i], solar_growth_rates[i]), 
                    textcoords="offset points", xytext=(0, 5), ha='right')
for i, value in enumerate(wind_growth_rates):
    axs[1].annotate(f'{value:.1f}%', (decades[i], wind_growth_rates[i]), 
                    textcoords="offset points", xytext=(0, -10), ha='right')

plt.tight_layout()
plt.show()