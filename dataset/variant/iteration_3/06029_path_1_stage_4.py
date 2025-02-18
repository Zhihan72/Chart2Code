import matplotlib.pyplot as plt
import numpy as np

months = ['Feb', 'Jan', 'Apr', 'Mar', 'Jun', 'May', 'Aug', 'Jul', 'Sep', 'Dec', 'Oct', 'Nov']
colony_alpha = [5.2, 5.5, 5.7, 5.6, 5.8, 5.9, 6.1, 6.0, 5.9, 5.8, 5.7, 5.6]
colony_beta = [4.8, 4.9, 5.0, 5.1, 5.4, 5.6, 5.7, 5.8, 5.7, 5.6, 5.5, 5.3]

fig, axs = plt.subplots(2, 1, figsize=(12, 8), gridspec_kw={'height_ratios': [1, 2]})

ax1 = axs[1]
ax1.hist(colony_alpha, bins=10, edgecolor='black', color='#FF9999', alpha=0.5, label='Alpha Group')
ax1.hist(colony_beta, bins=10, edgecolor='black', color='#66B3FF', alpha=0.5, label='Beta Settlement')
ax1.set_title('Mars Colonies Energy Usage (GWh)', fontsize=16, fontweight='bold', pad=20)
ax1.set_xlabel('Energy Output (GWh)', fontsize=14)
ax1.set_ylabel('Occurrences', fontsize=14)
ax1.legend(title='Settlement', loc='upper right', fontsize=10)

ax2 = axs[0]
width = 0.3
months_indices = np.arange(len(months))

ax2.bar(months_indices - width / 2, colony_alpha, width, label='Alpha Group', edgecolor='black', color='#FF9999', alpha=0.7)
ax2.bar(months_indices + width / 2, colony_beta, width, label='Beta Settlement', edgecolor='black', color='#66B3FF', alpha=0.7)

ax2.set_title('Colony Monthly Power Usage', fontsize=14, fontweight='bold', pad=20)
ax2.set_xticks(months_indices)
ax2.set_xticklabels(months, fontsize=12)
ax2.set_ylabel('Power Consumption (GWh)', fontsize=14)
ax2.legend(title='Settlement', loc='upper left', fontsize=10, edgecolor='gray', facecolor='lightgrey', framealpha=0.7)

plt.tight_layout()
plt.show()