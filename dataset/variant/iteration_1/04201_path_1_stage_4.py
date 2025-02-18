import matplotlib.pyplot as plt
import numpy as np

brightness_bins = ['0-2', '2-4', '4-6', '6-8', '8-10']
stars_jun = [20, 30, 55, 40, 25]
stars_dec = [25, 35, 45, 50, 30]
stars_sep = [30, 40, 60, 45, 35]
stars_mar = [15, 25, 50, 35, 20]

fig, axs = plt.subplots(1, 4, figsize=(18, 6), sharey=True)

axs[0].bar(brightness_bins, stars_jun, color='lightcoral')
axs[0].set_title('Star Brightness in Jun')
axs[0].set_xlabel('Brightness Range (Magnitude)')
axs[0].set_ylabel('Number of Stars')

axs[1].bar(brightness_bins, stars_dec, color='lightgreen')
axs[1].set_title('Star Brightness in Dec')
axs[1].set_xlabel('Brightness Range (Magnitude)')

axs[2].bar(brightness_bins, stars_sep, color='lightblue')
axs[2].set_title('Star Brightness in Sep')
axs[2].set_xlabel('Brightness Range (Magnitude)')

axs[3].bar(brightness_bins, stars_mar, color='lightyellow')
axs[3].set_title('Star Brightness in Mar')
axs[3].set_xlabel('Brightness Range (Magnitude)')

fig.suptitle('Brightness of Stars in Different Constellations:\nObservation Data for Selected Months', fontsize=16, fontweight='bold')
plt.tight_layout(rect=[0, 0.03, 1, 0.95])

plt.show()