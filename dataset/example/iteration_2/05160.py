import matplotlib.pyplot as plt
import numpy as np

# Backstory:
# The chart represents the journey of "Solar Energy Production Over Decades," highlighting how solar energy production
# has grown significantly over the past few decades. Additionally, a subplot shows percentage growth to provide 
# further insights into the increase of solar energy production.

# Defining decades and corresponding solar energy production data (in GWh)
decades = ['1990s', '2000s', '2010s', '2020s']
solar_production = np.array([10, 50, 500, 3000])

# Calculate percentage growth between decades
def calculate_growth(data):
    growth = []
    for i in range(1, len(data)):
        growth.append((data[i] - data[i-1]) / data[i-1] * 100)
    growth.insert(0, 0)  # 0 growth for the first decade
    return growth

growth_rates = calculate_growth(solar_production)

# Setting up the subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 10), gridspec_kw={'height_ratios': [3, 1]})

# Primary plot: Solar Energy Production Over Decades
axs[0].plot(decades, solar_production, marker='o', linestyle='-', linewidth=3, color='orange', label='Solar Production (GWh)')

# Set titles and labels for the primary plot
axs[0].set_title("The Solar Energy Surge: Production Over Decades", fontsize=16, fontweight='bold', pad=20)
axs[0].set_xlabel("Decade", fontsize=14)
axs[0].set_ylabel("Solar Energy Production (GWh)", fontsize=14)
axs[0].legend(loc='upper left')
axs[0].yaxis.grid(True, linestyle='--', alpha=0.7)

# Annotations for each data point
for i, value in enumerate(solar_production):
    axs[0].annotate(f'{value} GWh', (decades[i], solar_production[i]),
                    textcoords="offset points", xytext=(0, 10), ha='center')

# Secondary plot: Percentage Growth of Solar Energy Production
axs[1].plot(decades, growth_rates, marker='o', linestyle='-', linewidth=3, color='blue', label='Growth Rate (%)')
axs[1].set_xlabel("Decade", fontsize=14)
axs[1].set_ylabel("Growth Rate (%)", fontsize=14)
axs[1].legend(loc='upper left')
axs[1].yaxis.grid(True, linestyle='--', alpha=0.7)

# Annotations for each growth point
for i, value in enumerate(growth_rates):
    axs[1].annotate(f'{value:.1f}%', (decades[i], growth_rates[i]), 
                    textcoords="offset points", xytext=(0, 10), ha='center')

# Adjust layout
plt.tight_layout()

# Display the plots
plt.show()