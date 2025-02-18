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

# Ax0 with altered styles
axs[0].plot(decades, solar_production, marker='s', linestyle='--', linewidth=2, color='blue', label='Production (GWh)')
axs[0].set_title("Solar Energy Surge", fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel("Decade", fontsize=14)
axs[0].set_ylabel("Production (GWh)", fontsize=14)
axs[0].legend(loc='lower right')
axs[0].yaxis.grid(False)  # Removed grid from the first plot

for i, value in enumerate(solar_production):
    axs[0].annotate(f'{value}', (decades[i], solar_production[i]), 
                    textcoords="offset points", xytext=(0, -15), ha='center')

# Ax1 with altered styles
axs[1].plot(decades, growth_rates, marker='*', linestyle='-.', linewidth=4, color='red', label='Growth (%)')
axs[1].set_title("Growth Rate", fontsize=16, fontweight='bold', pad=20)
axs[1].set_xlabel("Decade", fontsize=14)
axs[1].set_ylabel("Growth (%)", fontsize=14)
axs[1].legend(loc='upper right')
axs[1].xaxis.grid(True, linestyle=':', alpha=0.5)  # Changed grid lines on the x-axis

for i, value in enumerate(growth_rates):
    axs[1].annotate(f'{value:.1f}%', (decades[i], growth_rates[i]), 
                    textcoords="offset points", xytext=(0, 5), ha='right')

plt.tight_layout()
plt.show()