import matplotlib.pyplot as plt
import numpy as np

brightness_bins = ['0-2', '2-4', '4-6', '6-8', '8-10']
stars_jan = [30, 45, 50, 35, 20]
stars_jun = [20, 30, 55, 40, 25]
stars_dec = [25, 35, 45, 50, 30]

fig, axs = plt.subplots(1, 3, figsize=(18, 6), sharey=True)

# Applied single color across all data groups
common_color = 'mediumseagreen'

axs[0].bar(brightness_bins, stars_dec, color=common_color, edgecolor='orange', hatch='/')
axs[0].set_title('Star Brightness in Dec')
axs[0].set_xlabel('Brightness Range')
axs[0].set_ylabel('Stars Count')
axs[0].grid(axis='x', linestyle='-', alpha=0.3)

axs[1].bar(brightness_bins, stars_jan, color=common_color, edgecolor='orange', hatch='/')
axs[1].set_title('Star Brightness in Jan')
axs[1].set_xlabel('Brightness Range')
axs[1].grid(axis='x', linestyle='-', alpha=0.3)

axs[2].bar(brightness_bins, stars_jun, color=common_color, edgecolor='orange', hatch='/')
axs[2].set_title('Star Brightness in Jun')
axs[2].set_xlabel('Brightness Range')
axs[2].grid(axis='x', linestyle='-', alpha=0.3)

fig.suptitle('Star Brightness Observation\nData for Selected Months', fontsize=16, fontweight='bold', color='indigo')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()