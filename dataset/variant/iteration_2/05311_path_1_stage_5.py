import matplotlib.pyplot as plt
import numpy as np

decades = ['1980s', '1990s', '2000s', '2010s', '2020s']

transportation_emissions = [26, 28, 31, 27, 25]
industry_emissions = [41, 38, 34, 32, 33]
agriculture_emissions = [21, 24, 22, 26, 26]
residential_emissions = [14, 13, 13, 15, 14]

fig, axs = plt.subplots(2, 1, figsize=(10, 10))

axs[0].plot(decades, transportation_emissions, marker='x', linestyle=':', linewidth=2, color='red')
axs[0].plot(decades, industry_emissions, marker='o', linestyle='--', linewidth=2, color='orange')
axs[0].plot(decades, agriculture_emissions, marker='s', linestyle='-.', linewidth=2, color='blue')
axs[0].plot(decades, residential_emissions, marker='^', linestyle='-', linewidth=2, color='green')

axs[0].grid(True, linestyle=':', alpha=0.5)

average_emissions = np.mean([transportation_emissions, industry_emissions, agriculture_emissions, residential_emissions], axis=0)

axs[1].plot(decades, average_emissions, marker='d', color='purple', linewidth=2, linestyle='-')
axs[1].grid(True, linestyle=':', alpha=0.5)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()