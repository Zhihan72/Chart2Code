import matplotlib.pyplot as plt
import numpy as np

decades = ['1980s', '1990s', '2000s', '2010s', '2020s']

# Simulated data for greenhouse gas emissions from different sectors (in percentage)
transportation_emissions = [25, 27, 30, 28, 26]
industry_emissions = [40, 37, 35, 33, 32]
agriculture_emissions = [20, 22, 23, 25, 27]
residential_emissions = [15, 14, 12, 14, 15]

# Create a figure with two subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 7))
fig.suptitle('Greenhouse Gas Emissions Trends by Sector (1980s-2020s)', fontsize=16, fontweight='bold')

# First subplot: Line Plot for each sector's emissions over decades
axs[0].plot(decades, transportation_emissions, marker='o', linestyle='-', linewidth=2, color='green', label='Transportation')
axs[0].plot(decades, industry_emissions, marker='s', linestyle='-', linewidth=2, color='orange', label='Industry')
axs[0].plot(decades, agriculture_emissions, marker='^', linestyle='-', linewidth=2, color='red', label='Agriculture')
axs[0].plot(decades, residential_emissions, marker='d', linestyle='-', linewidth=2, color='blue', label='Residential')

axs[0].set_title('Emissions by Sector', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Decades', fontsize=12)
axs[0].set_ylabel('Percentage of Total Emissions', fontsize=12)
axs[0].legend(loc='upper right', fontsize=10, frameon=False)
axs[0].grid(True, linestyle='--', alpha=0.7)

# Annotations for the first subplot
for i, txt in enumerate(transportation_emissions):
    axs[0].annotate(f'{txt}%', (decades[i], transportation_emissions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(industry_emissions):
    axs[0].annotate(f'{txt}%', (decades[i], industry_emissions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(agriculture_emissions):
    axs[0].annotate(f'{txt}%', (decades[i], agriculture_emissions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(residential_emissions):
    axs[0].annotate(f'{txt}%', (decades[i], residential_emissions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

# Calculating averages for additional insights
average_emissions = np.mean([transportation_emissions, industry_emissions, agriculture_emissions, residential_emissions], axis=0)

# Second subplot: Trend of Average Emissions
axs[1].plot(decades, average_emissions, marker='o', color='purple', linewidth=2, linestyle='--', label='Average Emissions')
axs[1].set_title('Overall Emission Trends', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Decades', fontsize=12)
axs[1].set_ylabel('Average Percentage of Total Emissions', fontsize=12)
axs[1].legend(loc='upper right', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()