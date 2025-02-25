import matplotlib.pyplot as plt
import numpy as np

decades = ['1980s', '1990s', '2000s', '2010s', '2020s']

transportation_emissions = [26, 28, 31, 27, 25]
industry_emissions = [41, 38, 34, 32, 33]
agriculture_emissions = [21, 24, 22, 26, 26]
residential_emissions = [14, 13, 13, 15, 14]

fig, axs = plt.subplots(2, 1, figsize=(10, 10))
fig.suptitle('Greenhouse Gas Emissions Trends by Sector (1980s-2020s)', fontsize=16, fontweight='bold')

axs[0].plot(decades, transportation_emissions, marker='o', linestyle='-', linewidth=2, color='red', label='Transportation')
axs[0].plot(decades, industry_emissions, marker='s', linestyle='-', linewidth=2, color='orange', label='Industry')
axs[0].plot(decades, agriculture_emissions, marker='^', linestyle='-', linewidth=2, color='blue', label='Agriculture')
axs[0].plot(decades, residential_emissions, marker='d', linestyle='-', linewidth=2, color='green', label='Residential')

axs[0].set_title('Emissions by Sector', fontsize=14, fontweight='bold')
axs[0].set_xlabel('Decades', fontsize=12)
axs[0].set_ylabel('Percentage of Total Emissions', fontsize=12)
axs[0].legend(loc='upper right', fontsize=10, frameon=False)
axs[0].grid(True, linestyle='--', alpha=0.7)

for i, txt in enumerate(transportation_emissions):
    axs[0].annotate(f'{txt}%', (decades[i], transportation_emissions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(industry_emissions):
    axs[0].annotate(f'{txt}%', (decades[i], industry_emissions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(agriculture_emissions):
    axs[0].annotate(f'{txt}%', (decades[i], agriculture_emissions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
for i, txt in enumerate(residential_emissions):
    axs[0].annotate(f'{txt}%', (decades[i], residential_emissions[i]), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)

average_emissions = np.mean([transportation_emissions, industry_emissions, agriculture_emissions, residential_emissions], axis=0)

axs[1].plot(decades, average_emissions, marker='o', color='purple', linewidth=2, linestyle='--', label='Average Emissions')
axs[1].set_title('Overall Emission Trends', fontsize=14, fontweight='bold')
axs[1].set_xlabel('Decades', fontsize=12)
axs[1].set_ylabel('Average Percentage of Total Emissions', fontsize=12)
axs[1].legend(loc='upper right', fontsize=10)
axs[1].grid(True, linestyle='--', alpha=0.7)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()